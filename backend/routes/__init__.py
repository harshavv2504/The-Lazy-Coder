"""
Routes package for The Lazy Coder backend
"""
from .monitoring import monitoring_bp
from .health import health_bp

__all__ = ['monitoring_bp', 'health_bp']
