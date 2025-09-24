"""
Nova-3 STT Service for backend
"""
import os
from deepgram import DeepgramClient, PrerecordedOptions, FileSource
from .file_path_mapper import FilePathMapper

class Nova3STTService:
    """Nova-3 Speech-to-Text service with all features"""
    
    def __init__(self, api_key: str = None, monitored_path: str = "."):
        """Initialize Nova-3 STT service"""
        if api_key is None:
            api_key = os.getenv('DEEPGRAM_API_KEY')
        
        if not api_key:
            raise ValueError("Deepgram API key is required. Set DEEPGRAM_API_KEY environment variable.")
        
        self.client = DeepgramClient(api_key)
        self.file_mapper = FilePathMapper(monitored_path)
    
    def transcribe_file(self, file_path: str) -> dict:
        """
        Transcribe audio file using Nova-3 with all features
        
        Args:
            file_path: Path to audio file
            
        Returns:
            Dictionary with transcript and confidence
        """
        try:
            # Read audio file
            with open(file_path, "rb") as file:
                buffer_data = file.read()

            payload: FileSource = {
                "buffer": buffer_data,
            }

            # Nova-3 with all features
            options = PrerecordedOptions(
                model="nova-3",
                smart_format=True,
                punctuate=True,
                numerals=True,
                filler_words=True
            )

            # Transcribe
            response = self.client.listen.rest.v("1").transcribe_file(payload, options)
            
            # Extract results
            transcript = response['results']['channels'][0]['alternatives'][0]['transcript']
            confidence = response['results']['channels'][0]['alternatives'][0]['confidence']
            
            # Apply smart file path replacement
            enhanced_transcript = self.file_mapper.replace_filenames_in_text(transcript)
            
            return {
                'success': True,
                'transcript': enhanced_transcript,
                'original_transcript': transcript,  # Keep original for comparison
                'confidence': confidence,
                'model': 'nova-3',
                'file_replacements_applied': enhanced_transcript != transcript
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'model': 'nova-3'
            }
    
    def update_monitored_path(self, new_path: str):
        """Update the monitored path for file mapping"""
        self.file_mapper.update_monitored_path(new_path)
    
    def get_folder_structure(self) -> dict:
        """Get the current folder structure being monitored"""
        return self.file_mapper.get_folder_structure_summary()
