"""
Session manager for handling monitoring sessions
"""
import uuid
from datetime import datetime
from typing import Dict, Optional, List

from ..models.monitoring_session import MonitoringSession
from ..config import Config

class SessionManager:
    """Manages monitoring sessions and file events"""
    
    def __init__(self, config: Config):
        self.config = config
        self.sessions: Dict[str, MonitoringSession] = {}
        self.current_session: Optional[MonitoringSession] = None
    
    def create_session(self, path: str) -> MonitoringSession:
        """Create a new monitoring session"""
        session_id = str(uuid.uuid4())
        session = MonitoringSession(
            session_id=session_id,
            path=path,
            start_time=datetime.now()
        )
        
        self.sessions[session_id] = session
        self.current_session = session
        
        return session
    
    def end_current_session(self) -> Optional[MonitoringSession]:
        """End the current monitoring session"""
        if self.current_session:
            self.current_session.is_active = False
            ended_session = self.current_session
            self.current_session = None
            return ended_session
        return None
    
    
    def get_current_session(self) -> Optional[MonitoringSession]:
        """Get the current active session"""
        return self.current_session
    
    def get_session(self, session_id: str) -> Optional[MonitoringSession]:
        """Get a specific session by ID"""
        return self.sessions.get(session_id)
    
    def get_all_sessions(self) -> List[MonitoringSession]:
        """Get all sessions"""
        return list(self.sessions.values())
    
    def get_session_status(self) -> dict:
        """Get current session status"""
        if self.current_session:
            return self.current_session.to_dict()
        return {
            'session_id': None,
            'path': None,
            'start_time': None,
            'is_active': False,
            'total_events': 0,
            'recent_events': []
        }
