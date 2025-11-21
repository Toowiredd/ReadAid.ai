# ReadAid.ai User Guide

Welcome to ReadAid.ai! This guide will help you get the most out of our accessibility tool.

## Table of Contents

1. [What is ReadAid.ai?](#what-is-readaidai)
2. [Getting Started](#getting-started)
3. [Using the Application](#using-the-application)
4. [Understanding the Output](#understanding-the-output)
5. [Tips for Best Results](#tips-for-best-results)
6. [Troubleshooting](#troubleshooting)
7. [Frequently Asked Questions](#frequently-asked-questions)

## What is ReadAid.ai?

ReadAid.ai is an AI-powered tool designed to make web content more accessible for individuals with Dyslexia and ADHD. It takes any topic or question you provide and generates well-formatted, easy-to-read content using:

- **AI-powered web search** to find accurate, current information
- **Advanced language models** to explain concepts clearly
- **Evidence-based formatting** optimized for readers with Dyslexia and ADHD

### Who is it for?

- Individuals with Dyslexia
- Individuals with ADHD
- Anyone who prefers clear, well-structured content
- Students, researchers, and lifelong learners
- Educators looking for accessible content

## Getting Started

### Prerequisites

Before using ReadAid.ai, you'll need:

1. **Python 3.8 or higher** installed on your computer
2. **OpenAI API Key** - Get one at [platform.openai.com](https://platform.openai.com/api-keys)
3. **Tavily API Key** - Get one at [tavily.com](https://tavily.com/)

### Installation

Follow these steps to set up ReadAid.ai:

1. **Download the application**
   ```bash
   git clone https://github.com/Toowiredd/ReadAid.ai.git
   cd ReadAid.ai
   ```

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your API keys**
   
   Create a `.env` file in the main folder and add:
   ```
   OPENAI_API_KEY=your_actual_openai_key
   TAVILY_API_KEY=your_actual_tavily_key
   ```
   
   Replace `your_actual_openai_key` and `your_actual_tavily_key` with your real API keys.

4. **Start the application**
   ```bash
   streamlit run app.py
   ```

5. **Open in your browser**
   
   The app will automatically open at `http://localhost:8501`

## Using the Application

### Step-by-Step Guide

1. **Launch the Application**
   - Run `streamlit run app.py` in your terminal
   - Your web browser will open automatically

2. **Enter Your Topic**
   - In the text box, type any topic or question you want to learn about
   - Be as specific or general as you like

3. **Generate Content**
   - Click the "Generate Accessible Content" button
   - Wait while the AI searches and formats your content (usually 10-30 seconds)

4. **Read Your Content**
   - The formatted content will appear on the page
   - It's optimized for easy reading with special formatting

5. **Download (Optional)**
   - Click "Download as HTML" to save the content for offline reading

### Example Queries

Here are some examples to get you started:

**Science Topics:**
- "Explain how photosynthesis works"
- "What is quantum computing?"
- "How does the immune system fight viruses?"

**History Topics:**
- "Tell me about the Renaissance"
- "What caused World War I?"
- "Who were the ancient Egyptians?"

**Technology Topics:**
- "How do electric cars work?"
- "What is artificial intelligence?"
- "Explain blockchain technology"

**General Knowledge:**
- "What is climate change and how does it affect us?"
- "How do airplanes fly?"
- "What is the water cycle?"

## Understanding the Output

ReadAid.ai generates content with special formatting designed for accessibility:

### Font and Text Features

- **Large Font Size**: 14-16pt or larger for easy reading
- **Clean Fonts**: Arial, Verdana, or Calibri - simple, sans-serif fonts
- **Bold First Characters**: The first letter of each sentence is bold to help your eyes find the start of new thoughts
- **Short Paragraphs**: Small chunks of text prevent overwhelming the reader

### Visual Elements

- **Blue Highlighting**: Important words are highlighted in blue
- **Yellow Background**: High-contrast background reduces eye strain
- **Clear Headings**: Hierarchical structure helps you navigate
- **Bullet Points**: Information is broken into digestible lists

### Content Structure

The generated content typically includes:

1. **Introduction**: Brief overview of the topic
2. **Main Points**: Detailed explanation broken into sections
3. **Key Terms**: Important vocabulary highlighted
4. **Summary**: Quick recap of main ideas

## Tips for Best Results

### Writing Good Queries

**Do:**
- ✅ Be specific: "How do solar panels convert sunlight to electricity?"
- ✅ Ask direct questions: "What is photosynthesis?"
- ✅ Use clear language: "Explain machine learning in simple terms"

**Avoid:**
- ❌ Vague requests: "Tell me stuff about science"
- ❌ Multiple questions: "What is AI and also how do computers work and..."
- ❌ Overly complex requests: "Provide a comprehensive analysis of..."

### Getting the Most Value

1. **Start Broad, Then Narrow**
   - First query: "What is climate change?"
   - Follow-up: "How does carbon dioxide affect the atmosphere?"

2. **One Topic at a Time**
   - Focus on a single subject per query
   - Generate multiple results for related topics

3. **Use Examples**
   - "Explain democracy with examples"
   - "What is coding? Show me examples"

4. **Ask for Explanations**
   - "Explain how..." is better than "Tell me about..."
   - "Why does..." helps get deeper understanding

## Troubleshooting

### Common Issues and Solutions

#### "Missing required environment variables"

**Problem**: API keys are not set up correctly

**Solution**: 
1. Check that your `.env` file exists
2. Verify your API keys are correct
3. Make sure there are no extra spaces in the `.env` file
4. Restart the application

#### "Failed to initialize AI model"

**Problem**: OpenAI API key is invalid or expired

**Solution**:
1. Verify your OpenAI API key at [platform.openai.com](https://platform.openai.com/api-keys)
2. Check if you have credits remaining in your OpenAI account
3. Generate a new API key if needed

#### "Error processing the response"

**Problem**: Something went wrong during content generation

**Solution**:
1. Try rephrasing your query
2. Make your query simpler or more specific
3. Check your internet connection
4. Wait a moment and try again

#### Content Takes Too Long to Generate

**Problem**: Slow processing time

**Possible Causes**:
- Complex topic requiring extensive search
- Slow internet connection
- High API load

**Solution**:
- Wait patiently (can take 30-60 seconds for complex topics)
- Try a simpler query
- Check your internet connection

#### Application Won't Start

**Problem**: `streamlit run app.py` doesn't work

**Solution**:
1. Verify Python is installed: `python --version`
2. Check you're in the right folder: `ls` (should see app.py)
3. Reinstall dependencies: `pip install -r requirements.txt`
4. Try: `python -m streamlit run app.py`

## Frequently Asked Questions

### General Questions

**Q: Is ReadAid.ai free to use?**

A: The code is open-source and free, but you need API keys from OpenAI and Tavily which have their own pricing. OpenAI offers free credits for new users.

**Q: Can I use ReadAid.ai offline?**

A: No, ReadAid.ai requires an internet connection to search the web and use AI models. However, you can download generated content for offline reading.

**Q: How accurate is the information?**

A: ReadAid.ai uses current web search and advanced AI models, but always verify important information from authoritative sources.

**Q: Can I use this for homework or research?**

A: Yes! ReadAid.ai is a great learning tool. However, always cite your sources and verify important facts.

### Privacy & Security

**Q: Is my data saved?**

A: Your queries are processed through OpenAI and Tavily APIs according to their privacy policies. The app itself doesn't store your queries.

**Q: Are my API keys safe?**

A: Yes, when stored in the `.env` file. Never share your `.env` file or commit it to version control.

### Customization

**Q: Can I change the background color?**

A: Yes! Edit the CSS in `app.py` to change colors. The yellow background is chosen for accessibility, but you can customize it.

**Q: Can I adjust the font size?**

A: The font size is set in the prompt template in `LangFlow_Hackathon.json`. You can modify it there.

**Q: Can I use different AI models?**

A: Yes, you can change the model in the app configuration. See the code comments in `app.py`.

### Technical Questions

**Q: What programming language is this built with?**

A: Python, using Streamlit for the web interface and LangChain for AI integration.

**Q: Can I contribute to the project?**

A: Absolutely! See our [Contributing Guide](CONTRIBUTING.md) for details.

**Q: How do I update to the latest version?**

A: Run `git pull` in the project folder, then `pip install -r requirements.txt` to update dependencies.

## Need More Help?

If you're still having issues:

1. **Check the Documentation**
   - [README.md](README.md) - Quick start guide
   - [ARCHITECTURE.md](ARCHITECTURE.md) - Technical details
   - [CONTRIBUTING.md](CONTRIBUTING.md) - Development guide

2. **Get Support**
   - Open an issue on [GitHub](https://github.com/Toowiredd/ReadAid.ai/issues)
   - Check existing issues for solutions
   - Join discussions in the GitHub repository

3. **Report a Bug**
   - Describe what you were trying to do
   - Include any error messages
   - Mention your Python version and operating system

---

**Happy Reading! 📚✨**

We hope ReadAid.ai makes learning and reading more accessible and enjoyable for you!
