"""
File Path Mapper Service for smart file name replacement in transcriptions
"""
import os
import re
from typing import Dict, List, Optional, Tuple

class FilePathMapper:
    """Service for mapping spoken filenames to actual file paths"""
    
    def __init__(self, monitored_path: str = "."):
        self.monitored_path = monitored_path
        self.file_map: Dict[str, str] = {}  # filename -> full_path
        
        # Common directories to ignore (junk/auto-generated folders)
        self.ignored_dirs = {
            '__pycache__', 'node_modules', '.git', '.vscode', '.idea',
            'dist', 'build', 'target', 'out', 'bin', 'obj',
            '.next', '.nuxt', 'coverage', '.nyc_output',
            'logs', 'tmp', 'temp', 'cache', '.cache',
            'venv', 'env', '.env', 'envs', '.venv',
            'site-packages', '.pytest_cache', '.mypy_cache',
            'vendor', 'bower_components', 'jspm_packages',
            'typings', 'lib', 'libs', 'packages',
            '.gradle', '.mvn', 'node', 'npm-debug.log*',
            'yarn-error.log', 'yarn-debug.log*', '.yarn',
            'android', 'ios', 'platforms', 'plugins',
            '.expo', '.expo-shared', 'web-build',
            'public', 'static', 'assets', 'media'
        }
        
        self.scan_folder_structure()
    
    def scan_folder_structure(self):
        """Scan the monitored folder and build filename to path mapping"""
        self.file_map.clear()
        
        if not os.path.exists(self.monitored_path):
            return
        
        for root, dirs, files in os.walk(self.monitored_path):
            # Filter out ignored directories
            dirs[:] = [d for d in dirs if d not in self.ignored_dirs]
            
            for file in files:
                # Skip hidden files and common junk files
                if file.startswith('.') or file.endswith(('.log', '.tmp', '.temp', '.cache')):
                    continue
                
                full_path = os.path.join(root, file)
                relative_path = os.path.relpath(full_path, self.monitored_path)
                clean_path = relative_path.replace(os.sep, '/')
                
                # Store exact filename mapping
                self.file_map[file] = clean_path
                
                # Create spoken version (replace underscores with spaces) - only if different and meaningful
                spoken_name = file.replace('_', ' ')
                if (spoken_name != file and 
                    spoken_name not in self.file_map and 
                    not file.startswith('__') and  # Skip __init__.py files
                    len(spoken_name.strip()) > 0):
                    self.file_map[spoken_name] = clean_path
    
    def find_file_path(self, spoken_filename: str) -> Optional[str]:
        """
        Find the actual file path for a spoken filename
        
        Args:
            spoken_filename: The filename mentioned in speech (e.g., "app.py", "app")
            
        Returns:
            Full relative path if found, None otherwise
        """
        # Clean the spoken filename
        clean_name = spoken_filename.strip().lower()
        
        # Direct match
        for filename, path in self.file_map.items():
            if filename.lower() == clean_name:
                return f"@{path}"
        
        # Partial match (in case of slight pronunciation differences)
        for filename, path in self.file_map.items():
            if clean_name in filename.lower() or filename.lower() in clean_name:
                return f"@{path}"
        
        return None
    
    def replace_filenames_in_text(self, text: str) -> str:
        """
        Replace filenames in transcription text with full paths
        
        Args:
            text: The transcribed text
            
        Returns:
            Text with filenames replaced by full paths
        """
        result_text = text
        
        # First, handle STT transcription issues with file extensions dynamically
        # Get all unique file extensions from the tracked files
        extensions = set()
        for filename in self.file_map.keys():
            if '.' in filename:
                ext = filename.split('.')[-1]
                extensions.add(ext)
        
        # Create dynamic patterns for each extension found
        for ext in extensions:
            # Convert extension to spoken form (e.g., "py" -> "p y", "tsx" -> "t s x")
            spoken_ext = ' '.join(ext)
            
            # Handle multi-word filenames with extensions
            # Pattern: "filename dot p y" -> "filename.py"
            pattern = r'\b(\w+(?:\s+\w+)*)\s+dot\s+' + spoken_ext.replace(' ', r'\s+') + r'\b'
            replacement = r'\1.' + ext
            result_text = re.sub(pattern, replacement, result_text, flags=re.IGNORECASE)
            
            # Handle single-word filenames with extensions
            # Pattern: "filename dot p y" -> "filename.py"
            pattern = r'\b(\w+)\s+dot\s+' + spoken_ext.replace(' ', r'\s+') + r'\b'
            replacement = r'\1.' + ext
            result_text = re.sub(pattern, replacement, result_text, flags=re.IGNORECASE)
            
            # Handle alternative spoken forms for common extensions
            if ext == 'json':
                # Handle "dot j son" -> ".json"
                pattern = r'\b(\w+(?:\s+\w+)*)\s+dot\s+j\s+son\b'
                replacement = r'\1.' + ext
                result_text = re.sub(pattern, replacement, result_text, flags=re.IGNORECASE)
                
                pattern = r'\b(\w+)\s+dot\s+j\s+son\b'
                replacement = r'\1.' + ext
                result_text = re.sub(pattern, replacement, result_text, flags=re.IGNORECASE)
            
            elif ext == 'html':
                # Handle "dot h t m l" and "dot h t m l" variations
                # Also handle "dot h t m l" -> ".html"
                pattern = r'\b(\w+(?:\s+\w+)*)\s+dot\s+h\s+t\s+m\s+l\b'
                replacement = r'\1.' + ext
                result_text = re.sub(pattern, replacement, result_text, flags=re.IGNORECASE)
                
                pattern = r'\b(\w+)\s+dot\s+h\s+t\s+m\s+l\b'
                replacement = r'\1.' + ext
                result_text = re.sub(pattern, replacement, result_text, flags=re.IGNORECASE)
            
            elif ext == 'tsx':
                # Handle "dot t s x" and "dot t s x" variations
                pattern = r'\b(\w+(?:\s+\w+)*)\s+dot\s+t\s+s\s+x\b'
                replacement = r'\1.' + ext
                result_text = re.sub(pattern, replacement, result_text, flags=re.IGNORECASE)
                
                pattern = r'\b(\w+)\s+dot\s+t\s+s\s+x\b'
                replacement = r'\1.' + ext
                result_text = re.sub(pattern, replacement, result_text, flags=re.IGNORECASE)
        
        # Sort all filenames by length (longest first) to avoid partial replacements
        sorted_filenames = sorted(self.file_map.keys(), key=len, reverse=True)
        
        for filename in sorted_filenames:
            # Use word boundaries to avoid partial matches, case-insensitive
            pattern = r'\b' + re.escape(filename) + r'\b'
            
            # Check if the filename appears as a whole word (case-insensitive)
            if re.search(pattern, result_text, re.IGNORECASE):
                file_path = f"@{self.file_map[filename]}"
                # Replace only whole word matches (case-insensitive)
                result_text = re.sub(pattern, file_path, result_text, flags=re.IGNORECASE)
        
        return result_text
    
    def get_folder_structure_summary(self) -> Dict[str, List[str]]:
        """Get a summary of the folder structure"""
        structure = {}
        
        for filename, path in self.file_map.items():
            directory = os.path.dirname(path)
            if directory not in structure:
                structure[directory] = []
            structure[directory].append(filename)
        
        return structure
    
    def get_ignored_directories(self) -> List[str]:
        """Get list of ignored directories"""
        return sorted(list(self.ignored_dirs))
    
    def add_ignored_directory(self, directory: str):
        """Add a directory to the ignored list"""
        self.ignored_dirs.add(directory)
    
    def remove_ignored_directory(self, directory: str):
        """Remove a directory from the ignored list"""
        self.ignored_dirs.discard(directory)
    
    def update_monitored_path(self, new_path: str):
        """Update the monitored path and rescan"""
        self.monitored_path = new_path
        self.scan_folder_structure()
