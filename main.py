import openai
import os
from dotenv import load_dotenv
from openai import OpenAI

#ładowanie klucza API
load_dotenv(dotenv_path="key.env")
openai.api_key = os.getenv("OPENAI_API_KEY")
openai = OpenAI()

#czytanie pliku z artykulem
def read_article(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


#generowanie htmla z pomoca AI
def generate_html(article_text):
    prompt = (
        "Przekształć poniższy artykuł do formatu HTML zgodnie z następującymi wytycznymi:\n"
        "- Użyj odpowiednich tagów HTML, takich jak <h1>, <h2>, <p> do strukturyzacji treści.\n"
        "- Wstaw znaczniki <img> w miejscach, gdzie mogłyby się pojawić grafiki. Ustaw src na "
        "'image_placeholder.jpg' i dodaj dokładny opis obrazu w atrybucie alt, aby można było go "
        "wykorzystać do generowania grafiki.\n"
        "- Dodaj podpisy pod obrazami używając tagu <figcaption> w obrębie <figure>.\n"
        "- Kod powinien zawierać tylko zawartość do wstawienia między tagami <body> i </body>, "
        "bez sekcji <html>, <head> ani <body>.\n"
        "-Brak kodu CSS ani JavaScript. Zwrócony kod powinien zawierać wyłącznie zawartość do,"
        "wstawienia pomiędzy tagami <body> i </body>. Nie dołączaj znaczników <html>,"
        "<head> ani <body>.\n\n"
        "Artykuł:\n"
        f"{article_text}"
    )

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user",
             "content": prompt}
        ],
        max_tokens=1500,
        temperature=0.7

    )
    return response.choices[0].message.content

#zapis do pliku
def save_to_html(content, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(content)

#classic main
def main():
    article_path = "text.txt"


    article_text = read_article(article_path)

    html_content = generate_html(article_text)

    save_to_html(html_content, "artykul.html")
    print("Job done.")

main()