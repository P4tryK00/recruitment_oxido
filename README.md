# HTML Generator with OpenAI

This Python script reads an article from a text file, uses OpenAI's GPT-4 model to convert it into structured HTML, and saves the generated HTML to a file. It is designed to help automate the process of creating simple HTML articles with image placeholders.

## Features

- Reads an article from a plain text file.
- Converts the article to HTML, including structural tags like `<h1>`, `<h2>`, `<p>`, and image placeholders (`<img>` with `alt` text).
- Saves the HTML content to a file, ready for further use.

## Installation and Setup

### Prerequisites
- Python 3.7+
- An OpenAI API key (stored in a `.env` file)

### Steps to Run

1. **Clone the Repository**
   ```bash
   git clone https://github.com/P4tryK00/recruitment_oxido
   cd recruitment_oxido

2. **Install Required Libraries Ensure openai and dotenv libraries are installed:**
    ```bash
    pip install openai python-dotenv

3. **Set up the OpenAI API Key**
    - Create a .env file in the project directory.
    - Add your OpenAI API key to .env as follows: OPENAI_API_KEY=your_api_key_here

4. **Prepare the Article**
    - Place the text of the article in text.txt in the project directory.

5. **Run the Script**
    ```bash
    python main.py

The generated HTML will be saved in artykul.html.

Notes
Ensure that text.txt contains the text content you wish to convert.
Modify the .env and .py file names to match your setup if necessary.
