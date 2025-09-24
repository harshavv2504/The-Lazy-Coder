"""
Audio Handler Service for in-memory audio processing
"""
import os
import tempfile
from datetime import datetime
import uuid

class AudioHandler:
    """Service for handling audio file operations in memory"""
    
    def __init__(self):
        # Create temp directory inside backend folder
        self.temp_dir = os.path.join(os.path.dirname(__file__), '..', 'temp')
        os.makedirs(self.temp_dir, exist_ok=True)
    
    def process_uploaded_file(self, file_storage) -> tuple[str, str]:
        """
        Process uploaded audio file in memory and return temporary file path
        
        Args:
            file_storage: Werkzeug FileStorage object
            
        Returns:
            Tuple of (temp_file_path, filename)
        """
        if not file_storage:
            raise ValueError("No file_storage object provided.")
        
        # Generate unique filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        unique_id = uuid.uuid4().hex[:8]
        filename = f"temp_recording_{timestamp}_{unique_id}.webm"
        
        # Read the uploaded file data
        file_data = file_storage.read()
        
        # Create temporary file in backend/temp directory
        temp_fd, temp_path = tempfile.mkstemp(suffix='.webm', prefix='audio_', dir=self.temp_dir)
        
        try:
            # Write data to temporary file
            with os.fdopen(temp_fd, 'wb') as temp_file:
                temp_file.write(file_data)
        except Exception:
            # If writing fails, close the file descriptor
            os.close(temp_fd)
            raise
        
        return temp_path, filename
    
    def cleanup_temp_file(self, file_path: str):
        """
        Clean up temporary audio file
        
        Args:
            file_path: Path to temporary file to delete
        """
        try:
            if os.path.exists(file_path):
                os.unlink(file_path)
        except Exception as e:
            # Log error but don't raise - cleanup failures shouldn't break the flow
            print(f"Warning: Failed to cleanup temp file {file_path}: {e}")
    
    def get_saved_files(self) -> list[str]:
        """Return empty list since we don't save files permanently"""
        return []
    
    def cleanup_temp_directory(self):
        """Clean up all temporary files in the temp directory"""
        try:
            if os.path.exists(self.temp_dir):
                for filename in os.listdir(self.temp_dir):
                    file_path = os.path.join(self.temp_dir, filename)
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
        except Exception as e:
            print(f"Warning: Failed to cleanup temp directory {self.temp_dir}: {e}")
