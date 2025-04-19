# KnowUrProduct

KnowUrProduct is a browser extension and backend service designed to assist users in retrieving and presenting product information in a concise and fact-based manner. It integrates with Walmart's product data and uses LLMs (Large Language Models) to generate responses based on predefined templates.

## Features

- **Browser Extension**:
  - Chat window for user interaction.
  - Buttons for maximizing, refreshing, and closing the chat window.
  - Input field and send button for user queries.

- **Backend Service**:
  - Parses Walmart product data using custom parsers.
  - Generates product prompts using predefined templates.
  - Integrates with LLMs for generating responses.

## Project Structure

### Extension (`knowurproduct-extension/`)
- `background.js`: Handles background tasks for the extension.
- `content.js`: Manages the chat window and user interactions.
- `manifest.json`: Defines the extension's metadata and permissions.
- `popup.html` & `popup.js`: Code for the extension's popup interface.
- `images/`: Contains icons for the extension.

### Backend (`knowurproduct-src/`)
- `.env`: Configuration for environment variables.
- `config.py`: Loads and manages application settings.
- `helper.py`: Utility functions for the backend.
- `main.py`: Entry point for the backend service.
- `ecommerce_processor/`: Core logic for processing product data.
  - `builders/`: Builds product data and prompts.
  - `factories/`: Creates instances of LLMs and processors.
  - `llm/`: Manages LLM integration.
  - `models/`: Defines data models.
  - `prompt_templates/`: Contains templates for generating product prompts.
  - `strategies/`: Parsing strategies for different data sources.

## Installation

### Prerequisites
- Python 3.10 or higher
- Node.js (for building the browser extension)

### Backend Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/knowurproduct.git
   cd knowurproduct/knowurproduct-src