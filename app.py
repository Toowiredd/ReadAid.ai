"""
ReadAid.ai - Dyslexia & ADHD Friendly Content Generator

This application transforms web content into accessible formats optimized for
readers with Dyslexia and ADHD. It uses AI-powered search and language models
to generate well-structured, easy-to-read content.

Author: ReadAid.ai Team
License: MIT
"""

from __future__ import annotations

import streamlit as st
import os
import datetime
import logging
import re
from typing import Optional, Tuple, List, Dict
from html import unescape as html_unescape
from langchain.chat_models import ChatOpenAI
from langflow.load import run_flow_from_json

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# ==================== Session State Initialization ====================

def initialize_session_state():
    """Initialize session state variables for persistent data."""
    if 'history' not in st.session_state:
        st.session_state.history = []
    if 'bookmarks' not in st.session_state:
        st.session_state.bookmarks = []
    if 'total_queries' not in st.session_state:
        st.session_state.total_queries = 0
    if 'start_time' not in st.session_state:
        st.session_state.start_time = datetime.datetime.now()
    if 'user_preferences' not in st.session_state:
        st.session_state.user_preferences = {
            'font_size': 16,
            'reading_level': 'Intermediate',
            'content_length': 'Detailed',
            'background_color': '#fdfd96'
        }


# ==================== Configuration ====================

def validate_environment() -> Tuple[bool, List[str]]:
    """
    Validate that required environment variables are set.
    
    Returns:
        Tuple[bool, List[str]]: (is_valid, list of missing variables)
    """
    required_vars = ["OPENAI_API_KEY", "TAVILY_API_KEY"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    return len(missing_vars) == 0, missing_vars


def get_llm_model() -> str:
    """
    Determine which OpenAI model to use based on current date.
    
    Returns:
        str: Model name to use
    """
    current_date = datetime.datetime.now().date()
    target_date = datetime.date(2024, 6, 12)
    
    if current_date > target_date:
        return "gpt-3.5-turbo"
    else:
        return "gpt-3.5-turbo-0301"


def get_reading_level_prompt(level: str) -> str:
    """
    Get prompt modifier based on reading level.
    
    Args:
        level: Reading level (Beginner, Intermediate, Advanced)
        
    Returns:
        str: Prompt modifier for reading level
    """
    level_prompts = {
        'Beginner': 'Use very simple language suitable for ages 8-12. Explain concepts like teaching a child. Avoid jargon.',
        'Intermediate': 'Use clear language suitable for general audience. Define technical terms when used.',
        'Advanced': 'Use standard language with technical terms. Assume reader has background knowledge.'
    }
    return level_prompts.get(level, level_prompts['Intermediate'])


def get_content_length_modifier(length: str) -> str:
    """
    Get modifier for content length preference.
    
    Args:
        length: Content length preference (Brief, Moderate, Detailed)
        
    Returns:
        str: Modifier for content length
    """
    length_modifiers = {
        'Brief': 'Provide a concise summary in 3-5 key points. Keep it short and focused.',
        'Moderate': 'Provide a balanced explanation with main points and supporting details.',
        'Detailed': 'Provide comprehensive information with examples, explanations, and context.'
    }
    return length_modifiers.get(length, length_modifiers['Moderate'])


# ==================== UI Configuration ====================

# Initialize session state
initialize_session_state()

# Page configuration
st.set_page_config(
    page_title="ReadAid.ai - Accessible Content Generator",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Get user preferences
font_size = st.session_state.user_preferences['font_size']
bg_color = st.session_state.user_preferences['background_color']

# Custom CSS for accessibility
css = f"""
<style>
.stApp {{
    background-color: {bg_color}; /* High contrast background */
}}

/* Improve button styling */
.stButton > button {{
    background-color: #4CAF50;
    color: white;
    font-size: 16px;
    font-weight: bold;
    padding: 12px 24px;
    border-radius: 8px;
    border: none;
    cursor: pointer;
    transition: background-color 0.3s;
}}

.stButton > button:hover {{
    background-color: #45a049;
}}

/* Text area styling */
.stTextArea > div > div > textarea {{
    font-size: {font_size}px;
    font-family: Arial, Verdana, sans-serif;
}}

/* Title styling */
h1 {{
    font-family: Arial, Verdana, sans-serif;
    color: #333;
}}

/* Content area styling */
.content-display {{
    font-size: {font_size}px;
    line-height: 1.6;
    font-family: Arial, Verdana, sans-serif;
}}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

# ==================== Main Application ====================

# Sidebar for settings and features
with st.sidebar:
    st.header("⚙️ Settings & Features")
    
    # Reading Preferences
    st.subheader("📖 Reading Preferences")
    
    reading_level = st.selectbox(
        "Reading Level",
        options=["Beginner", "Intermediate", "Advanced"],
        index=1,
        help="Adjust the complexity of explanations"
    )
    st.session_state.user_preferences['reading_level'] = reading_level
    
    content_length = st.selectbox(
        "Content Length",
        options=["Brief", "Moderate", "Detailed"],
        index=1,
        help="Choose how much detail you want"
    )
    st.session_state.user_preferences['content_length'] = content_length
    
    font_size = st.slider(
        "Font Size",
        min_value=12,
        max_value=24,
        value=st.session_state.user_preferences['font_size'],
        step=2,
        help="Adjust text size for comfortable reading"
    )
    st.session_state.user_preferences['font_size'] = font_size
    
    bg_color = st.selectbox(
        "Background Color",
        options=["#fdfd96 (Yellow)", "#E8F4F8 (Light Blue)", "#F0F0F0 (Light Gray)", "#FFF9E6 (Cream)"],
        index=0,
        help="Choose a background color that's comfortable for your eyes"
    )
    st.session_state.user_preferences['background_color'] = bg_color.split()[0]
    
    st.markdown("---")
    
    # History Section
    st.subheader("📚 Content History")
    if st.session_state.history:
        for idx, item in enumerate(reversed(st.session_state.history[-5:])):
            with st.expander(f"{item['query'][:30]}..."):
                st.caption(f"Generated: {item['timestamp']}")
                if st.button(f"📌 Bookmark", key=f"bookmark_{idx}"):
                    if item not in st.session_state.bookmarks:
                        st.session_state.bookmarks.append(item)
                        st.success("Bookmarked!")
    else:
        st.info("No history yet. Generate some content to see it here!")
    
    st.markdown("---")
    
    # Bookmarks Section
    st.subheader("⭐ Bookmarks")
    if st.session_state.bookmarks:
        bookmark_titles = [f"{b['query'][:30]}..." for b in st.session_state.bookmarks]
        selected_bookmark = st.selectbox(
            "Load Bookmark",
            options=range(len(st.session_state.bookmarks)),
            format_func=lambda x: bookmark_titles[x]
        )
        if st.button("📄 Load Bookmarked Content"):
            st.session_state.loaded_bookmark = st.session_state.bookmarks[selected_bookmark]
    else:
        st.info("No bookmarks yet. Click the bookmark button on generated content!")
    
    st.markdown("---")
    
    # Statistics
    st.subheader("📊 Reading Statistics")
    st.metric("Total Queries", st.session_state.total_queries)
    st.metric("Bookmarks Saved", len(st.session_state.bookmarks))
    session_duration = datetime.datetime.now() - st.session_state.start_time
    st.metric("Session Duration", f"{session_duration.seconds // 60} min")

st.title("ReadAid.ai 📚")
st.subheader("Dyslexia & ADHD Reader Friendly Content Search and Display")

# Add helpful description
with st.expander("ℹ️ How to use ReadAid.ai"):
    st.markdown("""
    **ReadAid.ai** makes web content more accessible for people with Dyslexia and ADHD.
    
    **How it works:**
    1. Enter any topic or question you want to learn about
    2. Click the "Generate Content" button
    3. Receive formatted, easy-to-read content with:
       - Large, clear fonts
       - Short paragraphs
       - Bullet points
       - Color-coded important terms
       - High contrast design
    
    **Example topics:**
    - "Explain quantum computing"
    - "What is climate change?"
    - "How do electric cars work?"
    """)

# Validate environment
is_valid, missing_vars = validate_environment()
if not is_valid:
    st.error(f"⚠️ Missing required environment variables: {', '.join(missing_vars)}")
    st.info("Please set up your API keys in the .env file or environment variables. See README.md for instructions.")
    st.stop()

# Initialize OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Get appropriate model
llm_model = get_llm_model()
logger.info(f"Using model: {llm_model}")

# Initialize LLM
try:
    llm = ChatOpenAI(temperature=0.7, model=llm_model, api_key=OPENAI_API_KEY)
except Exception as e:
    logger.error(f"Failed to initialize LLM: {e}")
    st.error("Failed to initialize AI model. Please check your API key.")
    st.stop()


# ==================== Content Generation ====================

def generate_content(users_input: str, reading_level: str = "Intermediate", 
                     content_length: str = "Moderate") -> Optional[str]:
    """
    Generate accessible content based on user input with customization options.
    
    Args:
        users_input: The topic or question from the user
        reading_level: Complexity level for the content
        content_length: Desired length of content
        
    Returns:
        Optional[str]: Generated HTML content or None if error occurs
    """
    if not users_input or not users_input.strip():
        st.warning("⚠️ Please enter a topic or question.")
        return None
    
    # Build enhanced query with preferences
    level_instruction = get_reading_level_prompt(reading_level)
    length_instruction = get_content_length_modifier(content_length)
    
    enhanced_query = f"{users_input}. {level_instruction} {length_instruction}"
    
    # LangFlow tweaks configuration
    TWEAKS = {
        "ChatInput-eRZ4s": {},
        "Prompt-WxrOa": {},
        "ChatOutput-G3OiS": {},
        "OpenAIModel-RZuxG": {}
    }
    
    try:
        logger.info(f"Processing query: {users_input} (Level: {reading_level}, Length: {content_length})")
        
        # Show progress
        with st.spinner("🔍 Searching and generating accessible content..."):
            # Run LangFlow pipeline with enhanced query
            result = run_flow_from_json(
                flow="LangFlow_Hackathon.json",
                input_value=enhanced_query,
                fallback_to_env_vars=True,
                tweaks=TWEAKS
            )
            
            # Extract HTML content
            result_text = result[0].outputs[0].results['message'].data['text']
            
            # Clean up markdown code blocks if present
            result_text = result_text.replace("```html", "").replace("```", "")
            
            logger.info("Content generated successfully")
            
            # Update statistics
            st.session_state.total_queries += 1
            
            # Add to history
            history_item = {
                'query': users_input,
                'content': result_text,
                'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                'reading_level': reading_level,
                'content_length': content_length
            }
            st.session_state.history.append(history_item)
            
            return result_text
            
    except KeyError as e:
        logger.error(f"Error extracting result: {e}")
        st.error("❌ Error processing the response. The content structure was unexpected.")
        return None
    except Exception as e:
        logger.error(f"Error generating content: {e}")
        st.error(f"❌ An error occurred: {str(e)}")
        st.info("Please try again or check your API keys and internet connection.")
        return None


def export_to_formats(content: str, query: str) -> Dict[str, bytes]:
    """
    Export content to multiple formats.
    
    Args:
        content: HTML content to export
        query: Original query for filename
        
    Returns:
        Dict with format names and content bytes
    """
    exports = {}
    
    # Plain text version (strip HTML tags and decode HTML entities)
    plain_text = re.sub('<[^<]+?>', '', content)
    plain_text = html_unescape(plain_text)
    exports['txt'] = plain_text.encode('utf-8')
    
    # HTML version (already have it)
    exports['html'] = content.encode('utf-8')
    
    return exports


# ==================== User Interface ====================

# Check if there's a loaded bookmark
if 'loaded_bookmark' in st.session_state:
    bookmark = st.session_state.loaded_bookmark
    st.info(f"📖 Loaded from bookmarks: {bookmark['query']}")
    users_input = bookmark['query']
    del st.session_state.loaded_bookmark
else:
    users_input = ""

# Add helpful description with features
with st.expander("ℹ️ How to use ReadAid.ai - Now with Enhanced Features!"):
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🎯 Core Features:**
        - AI-powered web search for current information
        - Dyslexia & ADHD optimized formatting
        - Large, clear fonts and color coding
        - Structured, easy-to-digest content
        
        **📝 How to use:**
        1. Enter any topic or question
        2. Adjust settings in the sidebar
        3. Click "Generate Content"
        4. Read, bookmark, or download
        """)
    
    with col2:
        st.markdown("""
        **✨ New Features:**
        - **Reading Levels**: Adjust complexity (Beginner/Intermediate/Advanced)
        - **Content Length**: Choose brief summaries or detailed explanations
        - **Customization**: Adjust font size and background color
        - **History**: View your recent searches
        - **Bookmarks**: Save favorite topics for later
        - **Export**: Download as HTML or plain text
        - **Statistics**: Track your reading progress
        """)
    
    st.markdown("""
    **💡 Example topics:**
    - "Explain quantum computing"
    - "What is climate change?"
    - "How do electric cars work?"
    """)

# Input section with tabs for different modes
tab1, tab2 = st.tabs(["🔍 New Search", "📚 Quick Access"])

with tab1:
    # Input section
    users_input = st.text_area(
        "Enter the Topic on which you want Information:",
        value=users_input,
        height=100,
        placeholder="E.g., 'Explain how photosynthesis works' or 'What is machine learning?'",
        help="Type any topic or question you'd like to learn about"
    )
    
    # Generate button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        button_pressed = st.button(
            "🚀 Generate Accessible Content",
            use_container_width=True,
            type="primary"
        )

with tab2:
    st.subheader("Popular Topics")
    
    popular_topics = [
        "What is artificial intelligence?",
        "Explain photosynthesis",
        "How does the internet work?",
        "What causes earthquakes?",
        "Explain the water cycle"
    ]
    
    # Build recent history list
    recent_history_list = [f"📜 {h['query']}" for h in reversed(st.session_state.history[-5:])] if st.session_state.history else []
    
    selected_topic = st.selectbox(
        "Choose a popular topic or use your recent history:",
        options=["-- Select --"] + popular_topics + recent_history_list
    )
    
    if st.button("Load Selected Topic", type="secondary"):
        if selected_topic != "-- Select --":
            # Store in session state for the main generation logic
            st.session_state.quick_topic = selected_topic.replace("📜 ", "")
            st.rerun()
        else:
            st.warning("Please select a topic first")

# Check if there's a quick topic to load
if 'quick_topic' in st.session_state:
    users_input = st.session_state.quick_topic
    del st.session_state.quick_topic
    button_pressed = True
else:
    button_pressed = False

# Process generation
if button_pressed and users_input:
    result_html = generate_content(
        users_input,
        reading_level=st.session_state.user_preferences['reading_level'],
        content_length=st.session_state.user_preferences['content_length']
    )
    
    if result_html:
        # Display success message
        st.success("✅ Content generated successfully!")
        
        # Show preferences used
        st.caption(f"📊 Generated with: {st.session_state.user_preferences['reading_level']} level, {st.session_state.user_preferences['content_length']} length")
        
        # Display the formatted content
        st.markdown("### 📖 Your Accessible Content:")
        st.markdown(f'<div class="content-display">{result_html}</div>', unsafe_allow_html=True)
        
        # Action buttons
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.download_button(
                label="💾 Download HTML",
                data=result_html,
                file_name=f"readaid_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.html",
                mime="text/html"
            )
        
        with col2:
            # Export to plain text
            exports = export_to_formats(result_html, users_input)
            st.download_button(
                label="📄 Download TXT",
                data=exports['txt'],
                file_name=f"readaid_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain"
            )
        
        with col3:
            if st.button("⭐ Add to Bookmarks"):
                history_item = {
                    'query': users_input,
                    'content': result_html,
                    'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                    'reading_level': st.session_state.user_preferences['reading_level'],
                    'content_length': st.session_state.user_preferences['content_length']
                }
                if history_item not in st.session_state.bookmarks:
                    st.session_state.bookmarks.append(history_item)
                    st.success("Bookmarked!")
                else:
                    st.info("Already bookmarked!")
        
        with col4:
            if st.button("🔄 Generate Again"):
                st.rerun()

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666; font-size: 14px;'>
        Made with ❤️ for accessible web content | 
        <a href='https://github.com/Toowiredd/ReadAid.ai' target='_blank'>GitHub</a> |
        Version 2.0 - Now with Enhanced Features!
    </div>
    """,
    unsafe_allow_html=True
)
