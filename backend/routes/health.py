"""
Health check routes
"""
from flask import Blueprint, jsonify
from datetime import datetime

health_bp = Blueprint('health', __name__, url_prefix='/api/v1')

@health_bp.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'The Lazy Coder Backend'
    })

@health_bp.route('/status', methods=['GET'])
def service_status():
    """Detailed service status"""
    return jsonify({
        'service': 'The Lazy Coder Backend',
        'version': '1.0.0',
        'status': 'running',
        'timestamp': datetime.now().isoformat(),
        'endpoints': {
            'monitoring': '/api/v1/monitoring',
            'health': '/api/v1/health'
        }
    })
