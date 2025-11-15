# Milutin Milanković Chatbot

This project is a chatbot that allows users to interact with a virtual representation of Milutin Milanković, the renowned Serbian mathematician, astronomer, climatologist, geophysicist, and civil engineer. The chatbot is designed to answer questions and engage in conversation in a manner that reflects Milanković's personality and expertise.

## Features

- **Conversational AI:** Engage in natural language conversations with the chatbot.
- **Historical Persona:** The chatbot adopts the persona of Milutin Milanković, providing a unique and educational experience.
- **Web Interface:** A user-friendly web interface for easy interaction.
- **Customizable Avatars:** User and bot avatars can be customized.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/milutin-milankovic-chatbot.git
   cd milutin-milankovic-chatbot
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your environment variables:**
   Create a `.env` file in the root of the project and add your Gemini API key:
   ```
   GEMINI_API_KEY="your-api-key"
   ```
   You can also customize the user and bot avatars by adding the following lines to your `.env` file:
   ```
   AVATAR_USER="path/to/your/avatar.png"
   AVATAR_BOT="path/to/your/bot/avatar.png"
   ```

## Usage

To start the chatbot, run the following command:
```bash
python main.py
```
This will launch a local web server, and you can interact with the chatbot through your web browser.

## Dependencies

The project uses the following libraries:

- `python-dotenv`
- `langchain-core`
- `langchain-google-genai`
- `langchain`
- `gradio`

## About Milutin Milanković

Milutin Milanković (1879-1958) was a Serbian scientist who is best known for his theory of ice ages, which connects the Earth's long-term climate changes with variations in its orbit around the Sun. His work has had a profound impact on our understanding of climate science and the history of our planet.

## Acknowledgements

This project was completed as a part of the **"Python Mega Course: Build 20 Real-World Apps and AI Agents"** course taught by **Ardit Sulce** at **udemy.com**. The core concepts and structure are derived from the course material.