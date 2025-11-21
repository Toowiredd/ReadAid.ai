# ReadAid.ai 📚✨

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Version](https://img.shields.io/badge/version-2.0-green.svg)](https://github.com/Toowiredd/ReadAid.ai)

> Making the web more accessible, one page at a time.

ReadAid.ai is an AI-powered accessibility tool that transforms web content into dyslexia and ADHD-friendly formats. Using advanced language models, intelligent web search, and evidence-based formatting guidelines, ReadAid.ai helps millions of readers access information more easily.

## ✨ Features

### Core Features
- 🔍 **Intelligent Web Search**: Powered by Tavily AI search for accurate, up-to-date information
- 🤖 **AI-Powered Content Generation**: Uses OpenAI GPT models to create clear, accessible content
- 🎨 **Accessibility-Optimized Formatting**: 
  - Large, readable fonts (Arial, Verdana, Calibri)
  - High-contrast color scheme
  - Short paragraphs and bullet points
  - Bold sentence starters for easier reading initiation
  - Blue highlighting for key terms
- ⚡ **Real-time Processing**: Fast content generation with streaming support
- 🎯 **Simple Interface**: Clean, distraction-free design built with Streamlit

### ✨ NEW in Version 2.0

- 📚 **Reading Level Customization**: Choose Beginner, Intermediate, or Advanced complexity
- 📏 **Content Length Options**: Select Brief summaries, Moderate, or Detailed explanations
- 🔤 **Font Size Adjustment**: Customize text size from 12px to 24px for comfortable reading
- 🎨 **Background Color Selection**: Choose from 4 eye-friendly color schemes
- 📖 **Content History**: Automatically saves your last 5 searches for easy reference
- ⭐ **Bookmark System**: Save and organize your favorite topics
- 💾 **Multiple Export Formats**: Download as HTML or plain text
- 📊 **Reading Statistics**: Track your queries, bookmarks, and session time
- 🚀 **Quick Access**: Pre-selected popular topics and recent history
- ℹ️ **Enhanced Help**: Comprehensive in-app guidance for all features

See [FEATURES.md](FEATURES.md) for detailed feature documentation.

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- Tavily API key ([Get one here](https://tavily.com/))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Toowiredd/ReadAid.ai.git
   cd ReadAid.ai
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```bash
   OPENAI_API_KEY=your_openai_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here
   ```
   
   Or set them in your environment:
   ```bash
   # On macOS/Linux
   export OPENAI_API_KEY='your_openai_api_key_here'
   export TAVILY_API_KEY='your_tavily_api_key_here'
   
   # On Windows
   set OPENAI_API_KEY=your_openai_api_key_here
   set TAVILY_API_KEY=your_tavily_api_key_here
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Access the app**
   
   Open your browser and navigate to `http://localhost:8501`

## 💡 How to Use

1. **Enter a Topic**: Type any topic or question you want to learn about in the text area
2. **Generate Content**: Click the "Generate Content with Readability" button
3. **Read Comfortably**: View the formatted, accessible content optimized for dyslexic and ADHD readers

### Example Queries

- "Explain quantum computing"
- "What is climate change?"
- "How do electric cars work?"
- "Tell me about ancient Egypt"

## 🏗️ Architecture

ReadAid.ai uses a sophisticated pipeline built with LangFlow:

```
User Input → Web Search (Tavily) → AI Processing (GPT) → Formatted Output
```

**Key Components:**
- **Chat Input**: Receives and manages user queries
- **Tavily Search Agent**: Intelligent web search with ReAct reasoning
- **Prompt Engineering**: Applies accessibility formatting guidelines
- **OpenAI Model**: Generates structured, accessible HTML content
- **Chat Output**: Displays the formatted result

For detailed architecture information, see [ARCHITECTURE.md](ARCHITECTURE.md).

## 🎯 Accessibility Guidelines

ReadAid.ai follows evidence-based accessibility guidelines:

### Typography
- **Fonts**: Sans-serif fonts (Arial, Verdana, Calibri)
- **Size**: 14-16pt minimum
- **Spacing**: Proper line height and character spacing

### Layout
- **Structure**: Clear headings and subheadings
- **Lists**: Bullet points and numbered lists
- **Paragraphs**: Short, focused blocks of text

### Visual Aids
- **Bold First Character**: Helps reading initiation
- **Color Highlighting**: Blue for important terms
- **High Contrast**: Yellow background for reduced eye strain

## 🛠️ Technology Stack

- **Frontend**: [Streamlit](https://streamlit.io/) - Python web framework
- **AI Orchestration**: [LangFlow](https://langflow.org/) - Visual AI workflow builder
- **Language Models**: [OpenAI GPT](https://openai.com/) via [LangChain](https://langchain.com/)
- **Search**: [Tavily AI](https://tavily.com/) - Advanced web search API
- **Python Libraries**: `streamlit`, `langflow`, `langchain`, `openai`

## 📖 Documentation

- [Architecture Overview](ARCHITECTURE.md) - Detailed system architecture
- [Contributing Guide](CONTRIBUTING.md) - How to contribute to the project
- [API Documentation](docs/API.md) - API reference (coming soon)

## 🤝 Contributing

We welcome contributions! ReadAid.ai is an open-source project aimed at improving web accessibility for everyone.

Please read our [Contributing Guidelines](CONTRIBUTING.md) to get started.

### Ways to Contribute

- 🐛 Report bugs
- 💡 Suggest new features
- 📝 Improve documentation
- 🎨 Enhance UI/UX
- ♿ Add accessibility features
- 🧪 Write tests

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Developed for the [LangFlow Hackathon](https://lablab.ai/) by [lablab.ai](https://lablab.ai/)
- Built with ❤️ for the dyslexia and ADHD community
- Inspired by accessibility research and best practices

## �� Contact & Support

- **Issues**: [GitHub Issues](https://github.com/Toowiredd/ReadAid.ai/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Toowiredd/ReadAid.ai/discussions)

## 🌟 Star History

If you find ReadAid.ai useful, please consider giving it a star! ⭐

---

**Made with ❤️ for a more accessible web**
