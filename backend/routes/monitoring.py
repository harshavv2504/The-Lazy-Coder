"""
Monitoring routes for file system monitoring
"""
from flask import Blueprint, request, jsonify
from datetime import datetime

from ..services.session_manager import SessionManager
from ..services.audio_handler import AudioHandler
from ..services.nova3_stt import Nova3STTService

monitoring_bp = Blueprint('monitoring', __name__, url_prefix='/api/v1/monitoring')

def create_monitoring_routes(session_manager: SessionManager, audio_handler: AudioHandler = None, stt_service: Nova3STTService = None):
    """Create monitoring routes with injected dependencies"""
    
    @monitoring_bp.route('/set-context', methods=['POST'])
    def set_context():
        """Set the project context and start monitoring"""
        try:
            data = request.get_json()
            if not data or 'projectContext' not in data:
                return jsonify({'error': 'Missing projectContext in request body'}), 400
            
            project_path = data['projectContext'].strip()
            if not project_path:
                return jsonify({'error': 'Project context cannot be empty'}), 400
            
            # End any existing session
            session_manager.end_current_session()
            
            # Create new session
            session = session_manager.create_session(project_path)
            
            # Update STT service with the new monitored path (no continuous monitoring needed)
            if stt_service:
                stt_service.update_monitored_path(project_path)
            
            return jsonify({
                'message': f'Folder structure loaded: {project_path}',
                'path': project_path,
                'monitoring': True,
                'session_id': session.session_id
            }), 200
            
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        except Exception as e:
            return jsonify({'error': f'Failed to start monitoring: {str(e)}'}), 500
    
    @monitoring_bp.route('/status', methods=['GET'])
    def get_monitoring_status():
        """Get current monitoring status and recent events"""
        session_status = session_manager.get_session_status()
        
        return jsonify({
            'session': session_status
        })
    
    @monitoring_bp.route('/stop', methods=['POST'])
    def stop_monitoring():
        """Stop current session"""
        try:
            ended_session = session_manager.end_current_session()
            
            return jsonify({
                'message': 'Session ended',
                'ended_session': ended_session.to_dict() if ended_session else None
            }), 200
        except Exception as e:
            return jsonify({'error': f'Failed to end session: {str(e)}'}), 500
    
    
    @monitoring_bp.route('/sessions', methods=['GET'])
    def get_all_sessions():
        """Get all monitoring sessions"""
        sessions = session_manager.get_all_sessions()
        return jsonify({
            'sessions': [session.to_dict() for session in sessions],
            'total': len(sessions)
        })
    
    @monitoring_bp.route('/transcribe', methods=['POST'])
    def transcribe_audio():
        """Transcribe audio using Nova-3 STT"""
        try:
            # Check if audio file is in request
            if 'audio' not in request.files:
                return jsonify({'error': 'No audio file provided'}), 400
            
            audio_file = request.files['audio']
            if audio_file.filename == '':
                return jsonify({'error': 'No audio file selected'}), 400
            
            # Process audio file in memory (temporary file)
            if audio_handler:
                temp_file_path, filename = audio_handler.process_uploaded_file(audio_file)
            else:
                return jsonify({'error': 'Audio handler not available'}), 500
            
            try:
                # Refresh folder structure before transcription (on-demand scanning)
                if stt_service:
                    # Get current session path or default to current directory
                    current_session = session_manager.get_current_session()
                    current_path = current_session.path if current_session else "."
                    stt_service.update_monitored_path(current_path)
                    
                    # Transcribe using Nova-3 STT
                    result = stt_service.transcribe_file(temp_file_path)
                    
                    if result['success']:
                        response_data = {
                            'transcription': result['transcript'],
                            'confidence': result['confidence'],
                            'model': result['model'],
                            'filename': filename,
                            'message': 'Audio transcribed successfully'
                        }
                        
                        # Add file replacement information if available
                        if 'original_transcript' in result:
                            response_data['original_transcript'] = result['original_transcript']
                            response_data['file_replacements_applied'] = result.get('file_replacements_applied', False)
                        
                        return jsonify(response_data), 200
                    else:
                        return jsonify({'error': f'Transcription failed: {result["error"]}'}), 500
                else:
                    return jsonify({'error': 'STT service not available'}), 500
                    
            finally:
                # Always clean up the temporary file
                audio_handler.cleanup_temp_file(temp_file_path)
                
        except Exception as e:
            return jsonify({'error': f'Transcription failed: {str(e)}'}), 500
    
    @monitoring_bp.route('/audio-files', methods=['GET'])
    def get_audio_files():
        """Get list of saved audio files (now returns empty since we use in-memory processing)"""
        try:
            if audio_handler:
                files = audio_handler.get_saved_files()
                return jsonify({
                    'files': files,
                    'total': len(files),
                    'message': 'Audio files are processed in memory and not saved permanently'
                }), 200
            else:
                return jsonify({'error': 'Audio handler not available'}), 500
        except Exception as e:
            return jsonify({'error': f'Failed to get audio files: {str(e)}'}), 500
    
    @monitoring_bp.route('/folder-structure', methods=['GET'])
    def get_folder_structure():
        """Get the current folder structure for file path mapping"""
        try:
            if stt_service:
                structure = stt_service.get_folder_structure()
                ignored_dirs = stt_service.file_mapper.get_ignored_directories()
                return jsonify({
                    'folder_structure': structure,
                    'ignored_directories': ignored_dirs,
                    'monitored_path': stt_service.file_mapper.monitored_path,
                    'total_files_tracked': len(stt_service.file_mapper.file_map)
                }), 200
            else:
                return jsonify({'error': 'STT service not available'}), 500
        except Exception as e:
            return jsonify({'error': f'Failed to get folder structure: {str(e)}'}), 500
    
    @monitoring_bp.route('/cleanup-temp', methods=['POST'])
    def cleanup_temp_files():
        """Clean up all temporary audio files"""
        try:
            if audio_handler:
                audio_handler.cleanup_temp_directory()
                return jsonify({
                    'message': 'Temporary files cleaned up successfully'
                }), 200
            else:
                return jsonify({'error': 'Audio handler not available'}), 500
        except Exception as e:
            return jsonify({'error': f'Failed to cleanup temp files: {str(e)}'}), 500
    
    return monitoring_bp
