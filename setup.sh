#!/bin/bash

# ReadAid.ai Setup Script
# This script helps you set up ReadAid.ai quickly and easily

set -e  # Exit on error

echo "================================================"
echo "   Welcome to ReadAid.ai Setup!"
echo "================================================"
echo ""

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Function to print colored output
print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

# Check Python installation
echo "Checking Python installation..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
    print_success "Python $PYTHON_VERSION found"
else
    print_error "Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Check Python version
PYTHON_MAJOR=$(python3 -c 'import sys; print(sys.version_info.major)')
PYTHON_MINOR=$(python3 -c 'import sys; print(sys.version_info.minor)')

if [ "$PYTHON_MAJOR" -lt 3 ] || ([ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 8 ]); then
    print_error "Python 3.8 or higher is required. You have Python $PYTHON_MAJOR.$PYTHON_MINOR"
    exit 1
fi

# Check if pip is installed
echo ""
echo "Checking pip installation..."
if command -v pip3 &> /dev/null; then
    print_success "pip3 found"
else
    print_error "pip3 is not installed. Please install pip."
    exit 1
fi

# Create virtual environment
echo ""
echo "Setting up virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    print_success "Virtual environment created"
else
    print_warning "Virtual environment already exists"
fi

# Activate virtual environment
echo ""
echo "Activating virtual environment..."
source venv/bin/activate
print_success "Virtual environment activated"

# Upgrade pip
echo ""
echo "Upgrading pip..."
pip install --upgrade pip --quiet
print_success "pip upgraded"

# Install dependencies
echo ""
echo "Installing dependencies..."
echo "(This may take a few minutes...)"
pip install -r requirements.txt --quiet
print_success "Dependencies installed"

# Set up environment file
echo ""
echo "Setting up environment file..."
if [ ! -f ".env" ]; then
    cp .env.example .env
    print_success ".env file created from .env.example"
    print_warning "Please edit .env and add your API keys:"
    echo "  - OPENAI_API_KEY"
    echo "  - TAVILY_API_KEY"
else
    print_warning ".env file already exists"
fi

# Check for API keys
echo ""
echo "Checking API keys..."
if grep -q "your_openai_api_key_here" .env 2>/dev/null; then
    print_warning "OpenAI API key not set in .env file"
    echo "  Get your key at: https://platform.openai.com/api-keys"
fi

if grep -q "your_tavily_api_key_here" .env 2>/dev/null; then
    print_warning "Tavily API key not set in .env file"
    echo "  Get your key at: https://tavily.com/"
fi

# Summary
echo ""
echo "================================================"
echo "   Setup Complete!"
echo "================================================"
echo ""
echo "Next steps:"
echo "1. Edit .env file and add your API keys"
echo "2. Run: source venv/bin/activate"
echo "3. Run: streamlit run app.py"
echo ""
print_success "Happy accessible reading! 📚✨"
echo ""
