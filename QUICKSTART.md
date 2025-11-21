# Quick Start Guide - ReadAid.ai

**Get ReadAid.ai running in 5 minutes!** ⚡

## For Absolute Beginners

Never used Python or Git before? No problem! Follow these steps:

### Step 1: Install Python 🐍

1. Go to [python.org/downloads](https://www.python.org/downloads/)
2. Download Python 3.8 or higher
3. **Important**: During installation, check "Add Python to PATH"
4. Click "Install Now"

To verify installation, open Terminal (Mac/Linux) or Command Prompt (Windows) and type:
```bash
python --version
```

You should see something like `Python 3.11.5`

### Step 2: Get the Code 📥

**Option A: Download ZIP** (Easiest)
1. Go to [github.com/Toowiredd/ReadAid.ai](https://github.com/Toowiredd/ReadAid.ai)
2. Click the green "Code" button
3. Click "Download ZIP"
4. Extract the ZIP file to a folder

**Option B: Use Git** (Recommended)
1. Install Git from [git-scm.com](https://git-scm.com)
2. Open Terminal/Command Prompt
3. Navigate to where you want the folder:
   ```bash
   cd Desktop  # or any other location
   ```
4. Clone the repository:
   ```bash
   git clone https://github.com/Toowiredd/ReadAid.ai.git
   cd ReadAid.ai
   ```

### Step 3: Get API Keys 🔑

You need two free API keys:

#### OpenAI API Key
1. Go to [platform.openai.com/signup](https://platform.openai.com/signup)
2. Create a free account
3. Go to [API Keys](https://platform.openai.com/api-keys)
4. Click "Create new secret key"
5. Copy the key (starts with `sk-`)
6. **Save it somewhere safe!** You can't see it again

#### Tavily API Key
1. Go to [tavily.com](https://tavily.com/)
2. Sign up for a free account
3. Go to your dashboard
4. Copy your API key
5. Save it somewhere safe

### Step 4: Quick Setup 🚀

#### On Windows:
1. Open the ReadAid.ai folder
2. Double-click `setup.bat`
3. Wait for installation to complete

#### On Mac/Linux:
1. Open Terminal
2. Navigate to the ReadAid.ai folder:
   ```bash
   cd path/to/ReadAid.ai
   ```
3. Run the setup script:
   ```bash
   bash setup.sh
   ```

### Step 5: Add Your API Keys 🔐

1. In the ReadAid.ai folder, find the file named `.env`
2. Open it with a text editor (Notepad, TextEdit, etc.)
3. Replace the placeholder text:
   ```
   OPENAI_API_KEY=sk-your-actual-key-here
   TAVILY_API_KEY=tvly-your-actual-key-here
   ```
4. Save the file

**Important**: 
- Don't add quotes around the keys
- Don't share your `.env` file with anyone
- Keep your keys secret!

### Step 6: Run the App! 🎉

#### On Windows:
1. Open Command Prompt
2. Navigate to the ReadAid.ai folder:
   ```
   cd path\to\ReadAid.ai
   ```
3. Activate the virtual environment:
   ```
   venv\Scripts\activate
   ```
4. Run the app:
   ```
   streamlit run app.py
   ```

#### On Mac/Linux:
1. Open Terminal
2. Navigate to the ReadAid.ai folder:
   ```bash
   cd path/to/ReadAid.ai
   ```
3. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```
4. Run the app:
   ```bash
   streamlit run app.py
   ```

### Step 7: Use ReadAid.ai! 📚

1. Your web browser should open automatically to `http://localhost:8501`
2. If not, manually open your browser and go to that address
3. Type a topic in the text box (e.g., "Explain photosynthesis")
4. Click "Generate Accessible Content"
5. Wait 10-30 seconds
6. Read your formatted content!

## Troubleshooting

### "Python is not recognized"
- Reinstall Python and check "Add Python to PATH"
- Restart your computer

### "pip is not recognized"
- Python installation issue - reinstall Python

### "Missing required environment variables"
- Check your `.env` file has the correct API keys
- Make sure there are no extra spaces
- Make sure the file is named `.env` (not `.env.txt`)

### "Failed to initialize AI model"
- Check your OpenAI API key is correct
- Verify you have credits in your OpenAI account
- Try generating a new API key

### App won't start
- Make sure you activated the virtual environment
- Try reinstalling dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### Can't find .env file
- On Windows: Enable "Show hidden files" in File Explorer
- On Mac: Press Cmd+Shift+. in Finder to show hidden files
- The file starts with a dot: `.env`

## Next Steps

Once you have the app running:

1. Read the [User Guide](USER_GUIDE.md) for detailed usage tips
2. Try different types of questions
3. Experiment with various topics
4. Save content you like using the download button

## Need Help?

- Check the [Full User Guide](USER_GUIDE.md)
- Look at [Troubleshooting](USER_GUIDE.md#troubleshooting)
- Open an issue on [GitHub](https://github.com/Toowiredd/ReadAid.ai/issues)

## Tips for Success

✅ **Do:**
- Ask specific questions
- Use clear, simple language
- Try different topics
- Download content you want to keep

❌ **Don't:**
- Share your API keys
- Ask multiple questions at once
- Expect instant results (AI takes time)
- Worry if something doesn't work perfectly the first time

---

**Congratulations!** 🎉 You're now using ReadAid.ai to make the web more accessible!

**Happy Reading!** 📚✨
