import openai
import os
from dotenv import load_dotenv
from openai import OpenAI

#ładowanie klucza API
load_dotenv(dotenv_path=".env")
openai.api_key = os.getenv("OPENAI_API_KEY")
openai = OpenAI()

#czytanie pliku z artykulem
def read_article(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


#generowanie htmla z pomoca AI
def generate_html(article_text):
    prompt = (
        "Przekształć poniższy artykuł na format HTML z następującymi wytycznymi:\n"
        "- Użyj odpowiednich tagów HTML do strukturyzacji treści: <h1> dla tytułów, <h2> dla sekcji, <p> dla akapitów.\n"
        "- Dodaj znaczniki <img> jako miejsce na obrazki, ustawiając 'src' na 'image_placeholder.jpg', a dokładny opis obrazu umieść w atrybucie 'alt'.\n"
        "- Umieść podpisy do obrazków w tagach <figcaption> w obrębie <figure>.\n"
        "- Wygeneruj kod HTML jedynie w zakresie do umieszczenia w <body> (bez <html>, <head>, czy <body>).\n\n"
        "Artykuł:\n"
        f"{article_text}"
    )

    response = openai.chat.completions.create(
        model="gpt-4-turbo",
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