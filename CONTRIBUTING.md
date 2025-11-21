# Contributing to ReadAid.ai

Thank you for your interest in contributing to ReadAid.ai! This project aims to make online content more accessible for individuals with Dyslexia and ADHD. Your contributions can help improve the reading experience for thousands of users.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Contributions](#making-contributions)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Pull Request Process](#pull-request-process)

## Code of Conduct

This project is committed to providing a welcoming and inclusive environment. We expect all contributors to:

- Be respectful and considerate
- Welcome newcomers and help them get started
- Focus on what's best for the community and users
- Show empathy towards other community members

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- OpenAI API key
- Tavily API key

### Development Setup

1. **Fork and Clone the Repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/ReadAid.ai.git
   cd ReadAid.ai
   ```

2. **Set Up Python Environment**
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   ```bash
   # Create .env file
   cp .env.example .env
   
   # Edit .env and add your API keys:
   # OPENAI_API_KEY=your_openai_key_here
   # TAVILY_API_KEY=your_tavily_key_here
   ```

5. **Run the Application**
   ```bash
   streamlit run app.py
   ```

## Making Contributions

### Types of Contributions

We welcome various types of contributions:

1. **Bug Fixes**: Fix issues in existing code
2. **Feature Development**: Add new capabilities
3. **Documentation**: Improve docs, add examples, create tutorials
4. **Accessibility Improvements**: Enhance readability features
5. **Performance Optimization**: Make the app faster and more efficient
6. **UI/UX Enhancements**: Improve user interface and experience
7. **Testing**: Add or improve tests

### Finding Issues to Work On

- Check the [Issues](https://github.com/Toowiredd/ReadAid.ai/issues) page
- Look for issues labeled `good first issue` for newcomers
- Issues labeled `help wanted` are great for contributions
- Feel free to propose new features by opening an issue first

## Coding Standards

### Python Style Guide

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines
- Use meaningful variable and function names
- Keep functions small and focused (Single Responsibility Principle)
- Add docstrings to functions and classes

### Code Examples

**Good:**
```python
def generate_accessible_content(user_query: str) -> str:
    """
    Generate accessible content for dyslexic and ADHD readers.
    
    Args:
        user_query: The topic or question from the user
        
    Returns:
        Formatted HTML string optimized for accessibility
    """
    # Implementation
    pass
```

**Less Ideal:**
```python
def gen_content(q):
    # does stuff
    pass
```

### Documentation

- Add docstrings to all public functions and classes
- Include type hints for function parameters and return values
- Update README.md if adding new features
- Add inline comments for complex logic

### Accessibility Guidelines

When contributing features that affect content display:

1. **Font Choices**: Stick to Arial, Verdana, Calibri, or similar sans-serif fonts
2. **Font Size**: Minimum 14pt, prefer 16pt or larger
3. **Color Contrast**: Ensure high contrast (WCAG AA minimum)
4. **Text Spacing**: Adequate line height (1.5x) and character spacing
5. **Structure**: Use clear headings, bullet points, and short paragraphs
6. **Special Formatting**: 
   - Bold first character of sentences
   - Highlight important words in blue
   - Avoid long blocks of text

## Testing Guidelines

### Manual Testing

Before submitting a PR:

1. **Basic Functionality**
   - Test with various topic queries
   - Verify HTML output is properly formatted
   - Check for errors in console

2. **Edge Cases**
   - Empty input
   - Very long queries
   - Special characters
   - Non-English text (if supported)

3. **Accessibility**
   - Test with different screen sizes
   - Verify color contrast
   - Check font rendering

### Automated Testing (Future)

We plan to add automated tests. Contributions in this area are especially welcome!

## Pull Request Process

### Before Submitting

1. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/issue-description
   ```

2. **Make Your Changes**
   - Write clear, concise code
   - Follow coding standards
   - Add comments where needed

3. **Test Your Changes**
   - Run the application and verify functionality
   - Test edge cases
   - Check for console errors

4. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Clear description of your changes"
   ```
   
   **Commit Message Guidelines:**
   - Use present tense ("Add feature" not "Added feature")
   - Be descriptive but concise
   - Reference issue numbers when applicable

### Submitting the PR

1. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your branch
   - Fill out the PR template

3. **PR Description Should Include:**
   - What changes were made and why
   - How to test the changes
   - Screenshots (for UI changes)
   - Reference to related issues

4. **Respond to Feedback**
   - Be open to suggestions
   - Make requested changes promptly
   - Ask questions if something is unclear

### PR Review Process

- Maintainers will review your PR
- You may be asked to make changes
- Once approved, your PR will be merged
- Your contribution will be credited

## Development Tips

### Working with LangFlow

- LangFlow components are defined in JSON
- Test changes in LangFlow UI before committing
- Keep component configurations in sync

### Debugging

- Use `print()` statements during development
- Check Streamlit console for errors
- Enable verbose mode in LangFlow for detailed logs

### Performance

- Consider caching for expensive operations
- Be mindful of API rate limits
- Test with realistic data volumes

## Questions or Need Help?

- Open an issue for questions
- Check existing documentation
- Reach out to maintainers

## Recognition

All contributors will be acknowledged in the project README and release notes.

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.

---

Thank you for contributing to ReadAid.ai and helping make the web more accessible! 🎉
