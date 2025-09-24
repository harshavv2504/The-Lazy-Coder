"""
Main Flask application for The Lazy Coder backend
"""
from flask import Flask
from flask_cors import CORS

from .config import config
from .services.session_manager import SessionManager
from .services.audio_handler import AudioHandler
from .services.nova3_stt import Nova3STTService
from .routes.monitoring import create_monitoring_routes
from .routes.health import health_bp

def create_app(config_name='default'):
    """Application factory pattern"""
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config[config_name])
    
    # Enable CORS
    CORS(app, origins=app.config['CORS_ORIGINS'])
    
    # Initialize services
    session_manager = SessionManager(app.config)
    audio_handler = AudioHandler()
    stt_service = Nova3STTService()
    
    # Register blueprints
    app.register_blueprint(health_bp)
    
    # Create and register monitoring routes with dependencies
    monitoring_routes = create_monitoring_routes(session_manager, audio_handler, stt_service)
    app.register_blueprint(monitoring_routes)
    
    # Make services available to routes (if needed)
    app.session_manager = session_manager
    app.audio_handler = audio_handler
    app.stt_service = stt_service
    
    return app

def main():
    """Main entry point"""
    import os
    
    # Get config from environment
    config_name = os.environ.get('FLASK_ENV', 'default')
    
    # Create app
    app = create_app(config_name)
    
    print("Starting The Lazy Coder Backend...")
    print("Available endpoints:")
    print("  POST /api/v1/monitoring/set-context - Set folder context for path replacement")
    print("  GET  /api/v1/monitoring/status - Get session status")
    print("  POST /api/v1/monitoring/stop - End current session")
    print("  GET  /api/v1/monitoring/sessions - Get all sessions")
    print("  POST /api/v1/monitoring/transcribe - Transcribe audio with smart path replacement")
    print("  GET  /api/v1/monitoring/audio-files - Get saved audio files")
    print("  GET  /api/v1/monitoring/folder-structure - Get current folder structure")
    print("  POST /api/v1/monitoring/cleanup-temp - Clean up temporary audio files")
    print("  GET  /api/v1/health - Health check")
    print("  GET  /api/v1/status - Service status")
    
    try:
        app.run(
            host=app.config['HOST'],
            port=app.config['PORT'],
            debug=app.config['DEBUG']
        )
    except KeyboardInterrupt:
        print("\nShutting down...")
        # Cleanup services
        pass

if __name__ == '__main__':
    main()