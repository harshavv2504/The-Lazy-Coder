# 🎙️ The Lazy Coder - Backend

A powerful Flask-based backend service for audio transcription with intelligent path replacement and session management.

## 🏗️ Architecture

The backend is built with a modular, scalable architecture:

```
backend/
├── 🐍 app.py                    # Main Flask application
├── ⚙️ config.py                 # Configuration management
├── 📦 requirements.txt          # Python dependencies
├── 📁 models/                   # Data models
│   └── 📊 monitoring_session.py # Monitoring session model
├── 📁 services/                 # Business logic services
│   ├── 🎵 audio_handler.py      # Audio processing utilities
│   ├── 🗂️ file_path_mapper.py   # Smart path replacement logic
│   ├── 🧠 nova3_stt.py          # Deepgram Nova-3 STT integration
│   └── 📊 session_manager.py    # Session management
└── 📁 routes/                   # API route handlers
    ├── 🏥 health.py             # Health check endpoints
    └── 📹 monitoring.py         # Audio transcription endpoints
```

## ✨ Features

- 🎤 **Audio Transcription**: High-quality speech-to-text using Deepgram Nova-3
- 🧠 **Smart Path Replacement**: Automatically maps file paths in transcriptions
- 📊 **Session Management**: Track and manage transcription sessions
- ⚙️ **Configuration Management**: Environment-based configuration
- 🔄 **RESTful API**: Clean API endpoints with proper error handling
- 🌐 **CORS Support**: Ready for frontend integration
- 🏥 **Health Monitoring**: Built-in health checks and status endpoints

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+**
- **Deepgram API Key** (get one at [deepgram.com](https://deepgram.com))

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Environment Configuration

Create a `.env` file in the backend directory:

```env
# Required: Deepgram API Key
DEEPGRAM_API_KEY=your_deepgram_api_key_here

# Optional: Flask Configuration
FLASK_ENV=development
DEBUG=True
HOST=0.0.0.0
PORT=5000
SECRET_KEY=your-secret-key-here

# Optional: CORS Configuration
CORS_ORIGINS=http://localhost:5173,http://localhost:3000

# Optional: Logging
LOG_LEVEL=INFO
LOG_FILE=app.log
```

### 3. Run the Server

```bash
python app.py
```

The server will start on `http://localhost:5000` with the following endpoints available:

```
🎯 Available Endpoints:
  POST /api/v1/monitoring/set-context - Set folder context for path replacement
  GET  /api/v1/monitoring/status - Get session status
  POST /api/v1/monitoring/stop - End current session
  GET  /api/v1/monitoring/sessions - Get all sessions
  POST /api/v1/monitoring/transcribe - Transcribe audio with smart path replacement
  GET  /api/v1/monitoring/audio-files - Get saved audio files
  GET  /api/v1/monitoring/folder-structure - Get current folder structure
  POST /api/v1/monitoring/cleanup-temp - Clean up temporary audio files
  GET  /api/v1/health - Health check
  GET  /api/v1/status - Service status
```

## 📡 API Documentation

### 🎯 Core Endpoints

#### POST `/api/v1/monitoring/set-context`
Set project context for intelligent path replacement.

**Request:**
```json
{
  "projectContext": "/path/to/your/project"
}
```

**Response:**
```json
{
  "message": "Project context set successfully",
  "projectContext": "/path/to/your/project",
  "session_id": "uuid-here"
}
```

#### POST `/api/v1/monitoring/transcribe`
Transcribe audio with smart path replacement.

**Request:**
```
Content-Type: multipart/form-data
audio: [WebM audio file]
```

**Response:**
```json
{
  "transcription": "Your transcribed text with smart path replacement",
  "session_id": "uuid-here",
  "processing_time": 1.23
}
```

#### GET `/api/v1/monitoring/status`
Get current session status and information.

**Response:**
```json
{
  "session_id": "uuid-here",
  "project_context": "/path/to/project",
  "is_active": true,
  "created_at": "2024-01-01T12:00:00Z",
  "transcription_count": 5
}
```

### 🏥 Health Endpoints

#### GET `/api/v1/health`
Basic health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T12:00:00Z"
}
```

#### GET `/api/v1/status`
Detailed service status and configuration.

**Response:**
```json
{
  "status": "running",
  "version": "1.0.0",
  "environment": "development",
  "services": {
    "deepgram": "connected",
    "session_manager": "active"
  }
}
```

### 🔧 Management Endpoints

#### GET `/api/v1/monitoring/sessions`
Get all transcription sessions.

#### POST `/api/v1/monitoring/stop`
End the current session.

#### GET `/api/v1/monitoring/audio-files`
Get list of saved audio files.

#### POST `/api/v1/monitoring/cleanup-temp`
Clean up temporary audio files.

## ⚙️ Configuration

The application supports multiple configuration environments:

| Environment | Description | Debug | Logging |
|-------------|-------------|-------|---------|
| `development` | Development mode | ✅ Enabled | Detailed |
| `production` | Production mode | ❌ Disabled | Warnings only |
| `testing` | Test mode | ✅ Enabled | Test-specific |

Set the `FLASK_ENV` environment variable to switch between configurations.

### Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `DEEPGRAM_API_KEY` | Deepgram API key for transcription | - | ✅ Yes |
| `FLASK_ENV` | Flask environment | `development` | ❌ No |
| `DEBUG` | Enable debug mode | `True` | ❌ No |
| `HOST` | Server host | `0.0.0.0` | ❌ No |
| `PORT` | Server port | `5000` | ❌ No |
| `SECRET_KEY` | Flask secret key | Auto-generated | ❌ No |
| `CORS_ORIGINS` | Allowed CORS origins | `*` | ❌ No |
| `LOG_LEVEL` | Logging level | `INFO` | ❌ No |

## 🛠️ Development

### Adding New Features

The modular architecture makes it easy to extend functionality:

1. **Models**: Add data models in `models/`
2. **Services**: Create business logic in `services/`
3. **Routes**: Add API endpoints in `routes/`
4. **Registration**: Register blueprints in `app.py`

### Project Structure

```
services/
├── 🎵 audio_handler.py      # Audio processing utilities
├── 🗂️ file_path_mapper.py   # Smart path replacement logic
├── 🧠 nova3_stt.py          # Deepgram Nova-3 STT integration
└── 📊 session_manager.py    # Session management

routes/
├── 🏥 health.py             # Health check endpoints
└── 📹 monitoring.py         # Audio transcription endpoints
```

### Error Handling

The API uses consistent error responses:

```json
{
  "error": "Clear, user-facing error message",
  "code": "ERROR_CODE",
  "timestamp": "2024-01-01T12:00:00Z"
}
```

## 🧪 Testing

```bash
# Run tests
python -m pytest

# Run with coverage
python -m pytest --cov=.

# Run specific test file
python -m pytest tests/test_services.py
```

## 🚀 Deployment

### Production Deployment

1. Set `FLASK_ENV=production`
2. Configure production database
3. Set secure `SECRET_KEY`
4. Configure proper CORS origins
5. Set up logging and monitoring

### Docker Deployment

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

## 📊 Monitoring

The backend includes built-in monitoring capabilities:

- **Health Checks**: `/api/v1/health` and `/api/v1/status`
- **Session Tracking**: Monitor active transcription sessions
- **Error Logging**: Comprehensive error tracking
- **Performance Metrics**: Processing time tracking