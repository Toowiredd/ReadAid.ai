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
from typing import Optional, Tuple, List
from langchain.chat_models import ChatOpenAI
from langflow.load import run_flow_from_json

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


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


# ==================== UI Configuration ====================

# Page configuration
st.set_page_config(
    page_title="ReadAid.ai - Accessible Content Generator",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for accessibility
css = """
<style>
.stApp {
    background-color: #fdfd96; /* High contrast yellow background */
}

/* Improve button styling */
.stButton > button {
    background-color: #4CAF50;
    color: white;
    font-size: 16px;
    font-weight: bold;
    padding: 12px 24px;
    border-radius: 8px;
    border: none;
    cursor: pointer;
    transition: background-color 0.3s;
}

.stButton > button:hover {
    background-color: #45a049;
}

/* Text area styling */
.stTextArea > div > div > textarea {
    font-size: 16px;
    font-family: Arial, Verdana, sans-serif;
}

/* Title styling */
h1 {
    font-family: Arial, Verdana, sans-serif;
    color: #333;
}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

# ==================== Main Application ====================

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

def generate_content(users_input: str) -> Optional[str]:
    """
    Generate accessible content based on user input.
    
    Args:
        users_input: The topic or question from the user
        
    Returns:
        Optional[str]: Generated HTML content or None if error occurs
    """
    if not users_input or not users_input.strip():
        st.warning("⚠️ Please enter a topic or question.")
        return None
    
    # LangFlow tweaks configuration
    TWEAKS = {
        "ChatInput-eRZ4s": {},
        "Prompt-WxrOa": {},
        "ChatOutput-G3OiS": {},
        "OpenAIModel-RZuxG": {}
    }
    
    try:
        logger.info(f"Processing query: {users_input}")
        
        # Show progress
        with st.spinner("🔍 Searching and generating accessible content..."):
            # Run LangFlow pipeline
            result = run_flow_from_json(
                flow="LangFlow_Hackathon.json",
                input_value=users_input,
                fallback_to_env_vars=True,
                tweaks=TWEAKS
            )
            
            # Extract HTML content
            result_text = result[0].outputs[0].results['message'].data['text']
            
            # Clean up markdown code blocks if present
            result_text = result_text.replace("```html", "").replace("```", "")
            
            logger.info("Content generated successfully")
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


# ==================== User Interface ====================

# Input section
users_input = st.text_area(
    "Enter the Topic on which you want Information:",
    height=100,
    placeholder="E.g., 'Explain how photosynthesis works' or 'What is machine learning?'",
    help="Type any topic or question you'd like to learn about"
)

# Generate button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    button_pressed = st.button(
        "🚀 Generate Accessible Content",
        use_container_width=True
    )

# Process generation
if button_pressed:
    result_html = generate_content(users_input)
    
    if result_html:
        # Display success message
        st.success("✅ Content generated successfully!")
        
        # Display the formatted content
        st.markdown("### 📖 Your Accessible Content:")
        st.html(result_html)
        
        # Option to download
        st.download_button(
            label="💾 Download as HTML",
            data=result_html,
            file_name="readaid_content.html",
            mime="text/html"
        )

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666; font-size: 14px;'>
        Made with ❤️ for accessible web content | 
        <a href='https://github.com/Toowiredd/ReadAid.ai' target='_blank'>GitHub</a>
    </div>
    """,
    unsafe_allow_html=True
)
