# 🎙️ The Lazy Coder - Frontend

A modern React TypeScript frontend for The Lazy Coder audio transcription application. Features a beautiful, responsive UI with real-time audio recording and customizable themes.

## ✨ Features

- 🎤 **Real-time Audio Recording** - High-quality WebM audio capture with visual feedback
- 🎨 **Beautiful UI** - Modern, responsive design with smooth animations
- 🌈 **Customizable Themes** - Multiple color themes with easy switching
- ⚡ **Fast Performance** - Built with Vite for lightning-fast development
- 📱 **Responsive Design** - Works perfectly on desktop and mobile
- 🔄 **Real-time Updates** - Live transcription results with error handling
- 🎯 **Developer-Focused** - Optimized for coding workflows

## 🏗️ Architecture

```
frontend/
├── ⚛️ App.tsx                 # Main application component
├── 📁 components/             # React components
│   ├── 🎤 RecorderButton.tsx  # Audio recording button
│   ├── 📄 TextCard.tsx        # Transcription display card
│   └── 📁 FolderSelector.tsx  # Project path selector
├── 📁 hooks/                  # Custom React hooks
│   └── 🎵 useAudioRecorder.ts # Audio recording logic
├── 📄 types.ts                # TypeScript type definitions
├── ⚙️ vite.config.ts          # Vite configuration
├── 📦 package.json            # Dependencies and scripts
└── 🎨 THEME_GUIDE.md          # UI customization guide
```

## 🚀 Quick Start

### Prerequisites

- **Node.js** (v18 or higher)
- **npm** or **yarn**

### 1. Install Dependencies

```bash
npm install
```

### 2. Start Development Server

```bash
npm run dev
```

The application will be available at `http://localhost:5173`

### 3. Build for Production

```bash
npm run build
```

### 4. Preview Production Build

```bash
npm run preview
```

## 🎨 Customization

### Theme System

The frontend includes a powerful theme system with multiple options:

#### Quick Theme Switch (Browser Console)

```javascript
switchTheme('blue')    // Blue theme
switchTheme('green')   // Green theme  
switchTheme('purple')  // Purple theme
switchTheme('dark')    // Dark theme (default)
```

#### Manual Color Customization

Edit CSS variables in `index.html`:

```css
:root {
  --bg-primary: #0f172a;      /* Main background */
  --bg-secondary: #1e293b;    /* Secondary background */
  --text-primary: #f8fafc;    /* Main text color */
  --accent-primary: #3b82f6;  /* Accent color */
  /* ... more variables */
}
```

See [THEME_GUIDE.md](THEME_GUIDE.md) for complete customization instructions.

## 🎯 Usage

### 1. Set Project Context

Enter your project path or name to establish context for intelligent path replacement in transcriptions.

### 2. Record Audio

- Click and hold the record button to start recording
- Release to stop and automatically transcribe
- Visual feedback shows recording status

### 3. View Results

Transcriptions appear in real-time with smart path replacement for coding contexts.

## 🛠️ Development

### Project Structure

```
components/
├── RecorderButton.tsx    # Audio recording interface
├── TextCard.tsx          # Transcription display
└── FolderSelector.tsx    # Project path input

hooks/
└── useAudioRecorder.ts   # Audio recording logic
```

### Key Components

#### `App.tsx`
Main application component handling:
- Project context management
- Audio recording coordination
- Error handling and display
- API integration

#### `useAudioRecorder.ts`
Custom hook providing:
- Audio recording functionality
- MediaRecorder API integration
- Error handling
- Recording state management

#### `RecorderButton.tsx`
Recording interface with:
- Visual recording states
- Accessibility features
- Smooth animations
- Processing indicators

### API Integration

The frontend integrates with the backend through these endpoints:

```typescript
// Set project context
POST /api/v1/monitoring/set-context
{
  "projectContext": "your/project/path"
}

// Transcribe audio
POST /api/v1/monitoring/transcribe
FormData with audio file
```

## 🎨 Styling

### CSS Variables

The application uses CSS custom properties for theming:

| Variable | Purpose | Example |
|----------|---------|---------|
| `--bg-primary` | Main background | `#0f172a` |
| `--bg-secondary` | Secondary background | `#1e293b` |
| `--text-primary` | Main text color | `#f8fafc` |
| `--accent-primary` | Accent color | `#3b82f6` |
| `--error-bg` | Error background | `rgba(239, 68, 68, 0.1)` |

### Responsive Design

- **Mobile-first** approach
- **Flexible layouts** with CSS Grid and Flexbox
- **Touch-friendly** interface elements
- **Adaptive typography** scaling

## 🧪 Testing

```bash
# Run tests (when implemented)
npm test

# Run tests in watch mode
npm test -- --watch

# Run tests with coverage
npm test -- --coverage
```

## 📦 Build Configuration

### Vite Configuration

The project uses Vite for fast development and optimized builds:

```typescript
// vite.config.ts
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    host: true
  },
  build: {
    outDir: 'dist',
    sourcemap: true
  }
})
```

### TypeScript Configuration

Strict TypeScript configuration for type safety:

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true
  }
}
```

## 🚀 Deployment

### Static Hosting

Build the application and deploy to any static hosting service:

```bash
npm run build
# Deploy the 'dist' folder
```

### Environment Variables

For production deployment, configure:

```env
VITE_API_BASE_URL=https://your-backend-url.com
VITE_APP_TITLE=The Lazy Coder
```

## 🔧 Troubleshooting

### Common Issues

1. **Audio Recording Not Working**
   - Ensure HTTPS in production
   - Check microphone permissions
   - Verify browser compatibility

2. **API Connection Issues**
   - Check backend server status
   - Verify CORS configuration
   - Check network connectivity

3. **Theme Not Applying**
   - Clear browser cache
   - Check CSS variable syntax
   - Verify theme switching function

### Browser Compatibility

- **Chrome** 90+
- **Firefox** 88+
- **Safari** 14+
- **Edge** 90+

## 📚 Additional Resources

- [THEME_GUIDE.md](THEME_GUIDE.md) - Complete theming guide
- [DOCUMENTATION.md](DOCUMENTATION.md) - Backend integration guide
- [React Documentation](https://react.dev/)
- [Vite Documentation](https://vitejs.dev/)
- [TypeScript Documentation](https://www.typescriptlang.org/)
