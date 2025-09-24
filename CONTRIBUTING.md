# 🤝 Contributing to The Lazy Coder

Thank you for your interest in contributing to The Lazy Coder! This document provides guidelines and information for contributors.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Contributing Guidelines](#contributing-guidelines)
- [Pull Request Process](#pull-request-process)
- [Issue Guidelines](#issue-guidelines)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Documentation](#documentation)

## 📜 Code of Conduct

This project adheres to a code of conduct that we expect all contributors to follow:

- **Be respectful** and inclusive in all interactions
- **Be constructive** in feedback and discussions
- **Be patient** with newcomers and questions
- **Be collaborative** and help others succeed

## 🚀 Getting Started

### Prerequisites

- **Node.js** (v18 or higher)
- **Python** (v3.8 or higher)
- **Git** for version control
- **Deepgram API Key** (for testing transcription features)

### Fork and Clone

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/harshavv2504/The-Lazy-Coder.git
   cd the-lazy-coder
   ```
3. Add the upstream repository:
   ```bash
   git remote add upstream https://github.com/harshavv2504/The-Lazy-Coder.git
   ```

## 🛠️ Development Setup

### Backend Setup

```bash
cd backend
pip install -r requirements.txt

# Create environment file
cp .env.example .env
# Edit .env with your Deepgram API key
```

### Frontend Setup

```bash
cd frontend
npm install
```

### Running the Application

1. **Start the backend:**
   ```bash
   cd backend
   python app.py
   ```

2. **Start the frontend:**
   ```bash
   cd frontend
   npm run dev
   ```

3. **Access the application:**
   - Frontend: `http://localhost:5173`
   - Backend API: `http://localhost:5000`

## 📝 Contributing Guidelines

### Types of Contributions

We welcome various types of contributions:

- 🐛 **Bug fixes** - Fix issues and improve stability
- ✨ **New features** - Add functionality and enhancements
- 📚 **Documentation** - Improve docs and add examples
- 🎨 **UI/UX improvements** - Enhance the user interface
- 🧪 **Tests** - Add or improve test coverage
- 🔧 **Refactoring** - Improve code quality and structure

### Before You Start

1. **Check existing issues** - Look for similar issues or feature requests
2. **Create an issue** - For significant changes, discuss first
3. **Choose an issue** - Pick an issue labeled `good first issue` or `help wanted`

## 🔄 Pull Request Process

### 1. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/issue-description
```

### 2. Make Your Changes

- Write clean, readable code
- Follow the coding standards
- Add tests for new functionality
- Update documentation as needed

### 3. Test Your Changes

```bash
# Backend tests
cd backend
python -m pytest

# Frontend tests
cd frontend
npm test

# Manual testing
# Test the full application flow
```

### 4. Commit Your Changes

Use clear, descriptive commit messages:

```bash
git add .
git commit -m "feat: add audio quality indicator to recording interface"
```

**Commit Message Format:**
- `feat:` - New features
- `fix:` - Bug fixes
- `docs:` - Documentation changes
- `style:` - Code style changes
- `refactor:` - Code refactoring
- `test:` - Adding or updating tests
- `chore:` - Maintenance tasks

### 5. Push and Create PR

```bash
git push origin feature/your-feature-name
```

Then create a pull request on GitHub with:
- Clear title and description
- Reference related issues
- Screenshots for UI changes
- Testing instructions

## 🐛 Issue Guidelines

### Bug Reports

When reporting bugs, please include:

```markdown
**Bug Description**
A clear description of the bug.

**Steps to Reproduce**
1. Go to '...'
2. Click on '....'
3. See error

**Expected Behavior**
What you expected to happen.

**Actual Behavior**
What actually happened.

**Environment**
- OS: [e.g., Windows 10, macOS 12.0]
- Browser: [e.g., Chrome 91, Firefox 89]
- Node.js version: [e.g., 18.0.0]
- Python version: [e.g., 3.9.0]

**Screenshots**
If applicable, add screenshots.

**Additional Context**
Any other context about the problem.
```

### Feature Requests

For feature requests, please include:

```markdown
**Feature Description**
A clear description of the feature.

**Use Case**
Why would this feature be useful?

**Proposed Solution**
How would you like this to work?

**Alternatives Considered**
Any alternative solutions you've considered.

**Additional Context**
Any other context about the feature request.
```

## 📏 Coding Standards

### Python (Backend)

- Follow **PEP 8** style guidelines
- Use **type hints** for function parameters and return values
- Write **docstrings** for all functions and classes
- Use **meaningful variable names**
- Keep functions **small and focused**

```python
def transcribe_audio(audio_data: bytes, session_id: str) -> dict:
    """
    Transcribe audio data using Deepgram STT service.
    
    Args:
        audio_data: Raw audio data in bytes
        session_id: Unique session identifier
        
    Returns:
        Dictionary containing transcription result
        
    Raises:
        TranscriptionError: If transcription fails
    """
    # Implementation here
    pass
```

### TypeScript/React (Frontend)

- Use **TypeScript** for type safety
- Follow **React best practices**
- Use **functional components** with hooks
- Implement **proper error handling**
- Use **meaningful component names**

```typescript
interface AudioRecorderProps {
  onRecordingComplete: (audioBlob: Blob) => void;
  isProcessing: boolean;
}

const AudioRecorder: React.FC<AudioRecorderProps> = ({
  onRecordingComplete,
  isProcessing
}) => {
  // Component implementation
};
```

### General Guidelines

- **Write self-documenting code** with clear variable names
- **Keep functions small** (ideally under 20 lines)
- **Use consistent formatting** (use Prettier/Black)
- **Add comments** for complex logic
- **Handle errors gracefully**

## 🧪 Testing

### Backend Testing

```bash
cd backend
python -m pytest                    # Run all tests
python -m pytest --cov=.           # Run with coverage
python -m pytest tests/test_stt.py # Run specific test file
```

### Frontend Testing

```bash
cd frontend
npm test                    # Run all tests
npm test -- --coverage     # Run with coverage
npm test -- --watch        # Run in watch mode
```

### Test Requirements

- **New features** must include tests
- **Bug fixes** should include regression tests
- **Aim for >80% code coverage**
- **Test both success and error cases**

## 📚 Documentation

### Code Documentation

- **Python**: Use docstrings following Google style
- **TypeScript**: Use JSDoc comments
- **README files**: Keep updated with changes

### API Documentation

- Update API endpoint documentation
- Include request/response examples
- Document error codes and messages

### User Documentation

- Update user guides for new features
- Add screenshots for UI changes
- Keep installation instructions current

## 🏷️ Labels and Milestones

### Issue Labels

- `bug` - Something isn't working
- `enhancement` - New feature or request
- `documentation` - Improvements to documentation
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention is needed
- `question` - Further information is requested

### Pull Request Labels

- `ready for review` - Ready for code review
- `needs testing` - Requires additional testing
- `breaking change` - Breaking change to API
- `documentation` - Documentation changes only

## 🎯 Development Workflow

### Daily Workflow

1. **Sync with upstream:**
   ```bash
   git fetch upstream
   git checkout main
   git merge upstream/main
   ```

2. **Create feature branch:**
   ```bash
   git checkout -b feature/your-feature
   ```

3. **Make changes and test:**
   - Write code
   - Add tests
   - Test manually
   - Update documentation

4. **Commit and push:**
   ```bash
   git add .
   git commit -m "feat: your feature description"
   git push origin feature/your-feature
   ```

5. **Create pull request:**
   - Fill out PR template
   - Request review
   - Address feedback

### Code Review Process

1. **Automated checks** must pass
2. **At least one review** required
3. **All conversations resolved**
4. **Tests passing** in CI/CD

## 🚀 Release Process

### Version Numbering

We use [Semantic Versioning](https://semver.org/):
- `MAJOR.MINOR.PATCH`
- `1.0.0` - Initial release
- `1.1.0` - New features
- `1.1.1` - Bug fixes

### Release Checklist

- [ ] All tests passing
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
- [ ] Version numbers updated
- [ ] Release notes prepared

## 💡 Tips for Contributors

### Getting Help

- **GitHub Discussions** - For questions and ideas
- **GitHub Issues** - For bug reports and feature requests
- **Code Review** - Learn from feedback on your PRs

### Best Practices

- **Start small** - Begin with documentation or small bug fixes
- **Ask questions** - Don't hesitate to ask for clarification
- **Be patient** - Code reviews take time
- **Learn continuously** - Each contribution is a learning opportunity

### Recognition

Contributors will be recognized in:
- **README.md** contributors section
- **Release notes** for significant contributions
- **GitHub contributors** page

## 📞 Contact

- **Maintainer**: [Harshavardhan](mailto:harshavardhan2504@gmail.com)
- **GitHub Issues**: [Create an issue](https://github.com/harshavv2504/The-Lazy-Coder/issues)
- **Discussions**: [GitHub Discussions](https://github.com/harshavv2504/The-Lazy-Coder/discussions)

---

Thank you for contributing to The Lazy Coder! 🎉

Your contributions help make this project better for everyone. We appreciate your time and effort in improving the codebase, documentation, and user experience.
