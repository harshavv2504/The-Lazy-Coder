<div align="center">

# 🎙️ The Lazy Coder

</div>

<div align="center">
  <img src="https://img.shields.io/badge/React-19.1.1-blue?style=for-the-badge&logo=react" alt="React Version" />
  <img src="https://img.shields.io/badge/Flask-Latest-green?style=for-the-badge&logo=flask" alt="Flask Version" />
  <img src="https://img.shields.io/badge/TypeScript-5.8.2-blue?style=for-the-badge&logo=typescript" alt="TypeScript Version" />
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License" />
</div>

<div align="center">
  <h3>🎯 Smart Audio Transcription for Developers</h3>
  <p>Record your thoughts, get instant transcriptions with intelligent path replacement for coding contexts</p>
</div>

---

## 💭 Why I Built This

As a developer, I found myself constantly putting off documentation because typing out file paths and detailed explanations felt tedious. I realized that **speaking is more natural than typing** - you can put more thought into what you're saying when you're not focused on the mechanics of typing.

I wanted a free alternative to paid transcription services like WhisperFlow, so I built this using Deepgram's generous $200 signup bonus (which gives you ~3300 hours of transcription!). The smart path replacement feature means you can just say "the main component in the src folder" and it automatically maps to your actual file paths.

**The philosophy**: Let's be lazy by speaking instead of typing boring stuff. Sometimes the best solution is the one that removes friction from your workflow.

---

## ✨ Features

- 🎤 **Real-time Audio Recording** - High-quality WebM audio capture
- 🧠 **Smart Transcription** - Powered by Deepgram's Nova-3 STT
- 🔄 **Intelligent Path Replacement** - Automatically maps file paths in transcriptions
- 🎨 **Beautiful UI** - Modern, responsive design with customizable themes
- ⚡ **Fast Processing** - Optimized for quick transcription turnaround
- 🔧 **Developer-Friendly** - Built for coding workflows and documentation

## 🚀 Quick Start

### Prerequisites

- **Node.js** (v18 or higher)
- **Python** (v3.8 or higher)
- **Deepgram API Key** (for transcription service)

### 1. Clone the Repository

```bash
git clone https://github.com/harshavv2504/The-Lazy-Coder.git
cd the-lazy-coder
```

### 2. Backend Setup

```bash
cd backend
pip install -r requirements.txt
```

Create a `.env` file in the backend directory:
```env
DEEPGRAM_API_KEY=your_deepgram_api_key_here
FLASK_ENV=development
DEBUG=True
HOST=0.0.0.0
PORT=5000
```

Start the backend server:
```bash
python app.py
```

### 3. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

The application will be available at `http://localhost:5173`

## 🏗️ Architecture

```
the-lazy-coder/
├── 📁 backend/                 # Flask API server
│   ├── 🐍 app.py              # Main Flask application
│   ├── ⚙️ config.py           # Configuration management
│   ├── 📦 requirements.txt    # Python dependencies
│   ├── 📁 models/             # Data models
│   ├── 📁 services/           # Business logic
│   │   ├── 🎵 audio_handler.py
│   │   ├── 🗂️ file_path_mapper.py
│   │   ├── 🧠 nova3_stt.py
│   │   └── 📊 session_manager.py
│   └── 📁 routes/             # API endpoints
│       ├── 🏥 health.py
│       └── 📹 monitoring.py
├── 📁 frontend/               # React TypeScript app
│   ├── ⚛️ App.tsx             # Main application component
│   ├── 📁 components/         # React components
│   ├── 📁 hooks/              # Custom React hooks
│   ├── 📄 package.json        # Node.js dependencies
│   └── 🎨 THEME_GUIDE.md      # UI customization guide
└── 📄 README.md               # This file
```

## 🎯 How It Works

1. **Set Context** - Enter your project path or name to establish context
2. **Record Audio** - Click and hold to record your thoughts or code explanations
3. **Smart Processing** - The system transcribes audio and intelligently replaces file paths
4. **Get Results** - View your transcription with proper file path mappings

## 📝 Example: Input vs Output

### What You Say:
*"I need to update the app dot p y file. The user authentication is handled in the auth service dot t s file, and I should also check the config dot j son file."*

### What You Get:
```
I need to update the @backend/app.py file. The user authentication is handled in the @frontend/services/authService.ts file, and I should also check the @frontend/config.json file.
```

### Smart Path Replacement in Action:
- **"app dot p y"** → **"@backend/app.py"** (handles STT pronunciation of file extensions)
- **"auth service dot t s"** → **"@frontend/services/authService.ts"** (maps spoken filenames to actual paths)
- **"config dot j son"** → **"@frontend/config.json"** (handles "j son" pronunciation)

### Another Example:
**Input:** *"The error is coming from the utils dot j s file, check the routes dot p y in the backend"*

**Output:** 
```
The error is coming from the @frontend/utils/helpers.js file, check the @backend/routes/monitoring.py in the backend
```

### How It Works:
1. **Scans your project** and builds a map of all filenames to their full paths
2. **Handles STT quirks** like "dot p y" instead of ".py" or "j son" instead of "json"
3. **Replaces filenames** with `@full/path/to/file` format for easy identification
4. **Ignores junk folders** like `node_modules`, `__pycache__`, `.git`, etc.

This intelligent path mapping saves you from typing out full file paths and makes your documentation much more accurate and useful! 🎯

## 🔧 API Endpoints

### Core Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/v1/monitoring/set-context` | Set project context for path replacement |
| `POST` | `/api/v1/monitoring/transcribe` | Transcribe audio with smart path replacement |
| `GET` | `/api/v1/monitoring/status` | Get current session status |
| `GET` | `/api/v1/health` | Health check endpoint |

### Example Usage

```bash
# Set project context
curl -X POST http://localhost:5000/api/v1/monitoring/set-context \
  -H "Content-Type: application/json" \
  -d '{"projectContext": "/path/to/your/project"}'

# Transcribe audio
curl -X POST http://localhost:5000/api/v1/monitoring/transcribe \
  -F "audio=@recording.webm"
```

## 🎨 Customization

The frontend supports multiple themes and easy customization:

- **Quick Theme Switch**: Use browser console commands
- **Manual Color Changes**: Edit CSS variables in `index.html`
- **Preset Themes**: Blue, Green, Purple, and Dark themes included

See [THEME_GUIDE.md](frontend/THEME_GUIDE.md) for detailed customization instructions.

## 🛠️ Development

### Backend Development

```bash
cd backend
# Install development dependencies
pip install -r requirements.txt

# Run with auto-reload
export FLASK_ENV=development
python app.py
```

### Frontend Development

```bash
cd frontend
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build
```

### Adding New Features

1. **Backend**: Add new services in `services/`, routes in `routes/`
2. **Frontend**: Create components in `components/`, hooks in `hooks/`
3. **Integration**: Update API calls in `App.tsx`

## 📋 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DEEPGRAM_API_KEY` | Deepgram API key for transcription | Required |
| `FLASK_ENV` | Flask environment (development/production) | `development` |
| `DEBUG` | Enable debug mode | `True` |
| `HOST` | Server host | `0.0.0.0` |
| `PORT` | Server port | `5000` |
| `CORS_ORIGINS` | Allowed CORS origins | `*` |

## 🧪 Testing

```bash
# Backend tests
cd backend
python -m pytest

# Frontend tests
cd frontend
npm test
```

## 📦 Deployment

### Docker Deployment

```bash
# Build and run with Docker Compose
docker-compose up --build
```

### Manual Deployment

1. **Backend**: Deploy Flask app to your preferred hosting service
2. **Frontend**: Build and deploy static files
3. **Environment**: Set production environment variables

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Workflow

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Deepgram** for providing excellent speech-to-text services
- **React** and **Flask** communities for amazing frameworks
- **Vite** for fast development experience

## 📞 Support

- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/harshavv2504/The-Lazy-Coder/issues)
- 💡 **Feature Requests**: [GitHub Discussions](https://github.com/harshavv2504/The-Lazy-Coder/discussions)
- 📧 **Contact**: [harshavardhan2504@gmail.com](mailto:harshavardhan2504@gmail.com)

---

<div align="center">
  <p>Made with ❤️ for developers who prefer talking over typing</p>
  <p>
    <a href="#-the-lazy-coder">⬆️ Back to Top</a>
  </p>
</div>
