# 🎨 Easy Color Theme System

## How to Change Colors

### Method 1: Quick Theme Switch (Easiest)
Open your browser's developer console and run:
```javascript
switchTheme('blue')    // Blue theme
switchTheme('green')   // Green theme  
switchTheme('purple')  // Purple theme
switchTheme('dark')    // Dark theme (default)
```

### Method 2: Manual Color Change
Edit the CSS variables in `frontend/index.html` (lines 25-50):

```css
:root {
  --bg-primary: #0f172a;      /* Main background */
  --bg-secondary: #1e293b;    /* Secondary background */
  --bg-input: #1e293b;        /* Input field background */
  --bg-card: rgba(30, 41, 59, 0.7); /* Card background */
  --bg-button: #334155;       /* Button background */
  
  --text-primary: #f8fafc;    /* Main text color */
  --text-secondary: #e2e8f0;  /* Secondary text */
  --text-muted: #94a3b8;      /* Muted text */
  
  --border-primary: #334155;  /* Border color */
  --accent-primary: #3b82f6;  /* Accent color (buttons, focus) */
  
  --gradient-from: #0f172a;   /* Gradient start */
  --gradient-to: rgba(30, 41, 59, 0.6); /* Gradient end */
}
```

### Method 3: Use Preset Themes
Uncomment one of the preset themes in `frontend/index.html` (lines 55-101):

```css
/* Blue Theme */
:root {
  --bg-primary: #1e3a8a;
  --bg-secondary: #1e40af;
  /* ... more colors ... */
}
```

## Available Color Variables

| Variable | Purpose | Example |
|----------|---------|---------|
| `--bg-primary` | Main background | `#0f172a` |
| `--bg-secondary` | Secondary background | `#1e293b` |
| `--bg-input` | Input field background | `#1e293b` |
| `--bg-card` | Card/component background | `rgba(30, 41, 59, 0.7)` |
| `--bg-button` | Button background | `#334155` |
| `--bg-button-hover` | Button hover state | `#475569` |
| `--text-primary` | Main text color | `#f8fafc` |
| `--text-secondary` | Secondary text | `#e2e8f0` |
| `--text-muted` | Muted text | `#94a3b8` |
| `--border-primary` | Border color | `#334155` |
| `--border-secondary` | Secondary border | `#475569` |
| `--accent-primary` | Accent color | `#3b82f6` |
| `--accent-hover` | Accent hover | `#2563eb` |
| `--error-bg` | Error background | `rgba(239, 68, 68, 0.1)` |
| `--error-text` | Error text | `#f87171` |
| `--error-border` | Error border | `rgba(239, 68, 68, 0.2)` |
| `--gradient-from` | Gradient start | `#0f172a` |
| `--gradient-to` | Gradient end | `rgba(30, 41, 59, 0.6)` |

## Creating Custom Themes

1. Copy the dark theme variables
2. Change the hex colors to your preferred colors
3. Make sure to maintain good contrast ratios
4. Test all components (buttons, inputs, cards, etc.)

## Theme Persistence

Themes are automatically saved to localStorage and will persist between browser sessions.

## Quick Color Ideas

- **Ocean**: `#0c4a6e`, `#075985`, `#0369a1`
- **Forest**: `#14532d`, `#166534`, `#16a34a`  
- **Sunset**: `#7c2d12`, `#ea580c`, `#f97316`
- **Midnight**: `#1e1b4b`, `#312e81`, `#4338ca`
- **Rose**: `#881337`, `#be185d`, `#e11d48`
