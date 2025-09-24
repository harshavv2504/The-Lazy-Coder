"""
Monitoring session model for tracking active monitoring
"""
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

@dataclass
class MonitoringSession:
    """Represents an active monitoring session"""
    
    session_id: str
    path: str
    start_time: datetime
    is_active: bool = True
    total_events: int = 0
    
    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization"""
        return {
            'session_id': self.session_id,
            'path': self.path,
            'start_time': self.start_time.isoformat(),
            'is_active': self.is_active,
            'total_events': self.total_events,
            'recent_events': []
        }
