# KnowYourProduct

KnowYourProduct is a browser extension and backend service designed to assist users in retrieving and presenting product information in a concise and fact-based manner. It integrates with Walmart's product data and uses LLMs (Large Language Models) to generate responses based on predefined templates.

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

### Extension (`KnowYourProduct-extension/`)
- `background.js`: Handles background tasks for the extension.
- `content.js`: Manages the chat window and user interactions.
- `manifest.json`: Defines the extension's metadata and permissions.
- `popup.html` & `popup.js`: Code for the extension's popup interface.
- `images/`: Contains icons for the extension.

### Backend (`KnowYourProduct-AI-srv/`)
- `.env`: Configuration for environment variables.
- `config.py`: Loads and manages application settings.
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
- Docker

### Backend Setup using Docker

These instructions assume you have Docker installed and running on your system.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/AnudeepGadi/KnowYourProduct-AI-srv.git](https://github.com/AnudeepGadi/KnowYourProduct-AI-srv.git)
    ```

2.  **Navigate to the source directory:**
    ```bash
    cd KnowYourProduct-AI-srv
    ```

3.  **Build the Docker image:**
    This command builds an image named `know-your-product-backend` using the `Dockerfile` in the current directory (`.`).
    ```bash
    docker build -t know-your-product-backend .
    ```

4.  **Run the Docker container:**
    This command runs the container in detached mode (`-d`), maps port 8080 on your host machine to port 8080 inside the container (`-p 8080:8080`), and uses the image built in the previous step.
    ```bash
    docker run -d \
      -p 8000:8000 \
      know-your-product-backend
    ```

The backend service should now be running and accessible on `http://localhost:8080`.