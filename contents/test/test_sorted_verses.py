import unittest
import random
import requests
from bs4 import BeautifulSoup

urls_bible_books = ['https://bkjfiel.com.br/genesis-', 'https://bkjfiel.com.br/exodo-', 'https://bkjfiel.com.br/levitico-', 'https://bkjfiel.com.br/numeros-', 'https://bkjfiel.com.br/deuteronomio-', 'https://bkjfiel.com.br/josue-', 'https://bkjfiel.com.br/juizes-', 'https://bkjfiel.com.br/rute-', 'https://bkjfiel.com.br/1-samuel-', 'https://bkjfiel.com.br/2-samuel-', 'https://bkjfiel.com.br/1-reis-', 'https://bkjfiel.com.br/2-reis-', 'https://bkjfiel.com.br/1-cronicas-', 'https://bkjfiel.com.br/2-cronicas-', 'https://bkjfiel.com.br/esdras-', 'https://bkjfiel.com.br/neemias-', 'https://bkjfiel.com.br/ester-', 'https://bkjfiel.com.br/jo-', 'https://bkjfiel.com.br/salmos-', 'https://bkjfiel.com.br/proverbios-', 'https://bkjfiel.com.br/eclesiastes-', 'https://bkjfiel.com.br/cantares-de-salomao-', 'https://bkjfiel.com.br/isaias-', 'https://bkjfiel.com.br/jeremias-', 'https://bkjfiel.com.br/lamentacoes-', 'https://bkjfiel.com.br/ezequiel-', 'https://bkjfiel.com.br/daniel-', 'https://bkjfiel.com.br/oseias-', 'https://bkjfiel.com.br/joel-', 'https://bkjfiel.com.br/amos-', 'https://bkjfiel.com.br/obadias-', 'https://bkjfiel.com.br/jonas-', 'https://bkjfiel.com.br/miqueias-', 'https://bkjfiel.com.br/naum-', 'https://bkjfiel.com.br/habacuque-', 'https://bkjfiel.com.br/sofonias-', 'https://bkjfiel.com.br/ageu-', 'https://bkjfiel.com.br/zacarias-', 'https://bkjfiel.com.br/malaquias-', 'https://bkjfiel.com.br/mateus-', 'https://bkjfiel.com.br/marcos-', 'https://bkjfiel.com.br/lucas-', 'https://bkjfiel.com.br/joao-', 'https://bkjfiel.com.br/atos-dos-apostolos-', 'https://bkjfiel.com.br/romanos-', 'https://bkjfiel.com.br/1-corintios-', 'https://bkjfiel.com.br/2-corintios-', 'https://bkjfiel.com.br/galatas-', 'https://bkjfiel.com.br/efesios-', 'https://bkjfiel.com.br/filipenses-', 'https://bkjfiel.com.br/colossenses-', 'https://bkjfiel.com.br/1-tessalonicenses-', 'https://bkjfiel.com.br/2-tessalonicenses-', 'https://bkjfiel.com.br/1-timoteo-', 'https://bkjfiel.com.br/2-timoteo-', 'https://bkjfiel.com.br/tito-', 'https://bkjfiel.com.br/filemom-', 'https://bkjfiel.com.br/hebreus-', 'https://bkjfiel.com.br/tiago-', 'https://bkjfiel.com.br/1-pedro-', 'https://bkjfiel.com.br/2-pedro-', 'https://bkjfiel.com.br/1-joao-', 'https://bkjfiel.com.br/2-joao-', 'https://bkjfiel.com.br/3-joao-', 'https://bkjfiel.com.br/judas-', 'https://bkjfiel.com.br/apocalipse-']

def sort_verse():
    random_url_book = random.choice(urls_bible_books)

    random_chapter = random.randint(1, 150)

    url_with_chapter= f'{random_url_book}{random_chapter}'
    verses = extract_verse_text(url_with_chapter)
    random_index = random.randint(2, len(verses) - 1)
    selected_three_verses = verses[random_index - 2 : random_index + 1]
    
    print(selected_three_verses)


def extract_verse_text(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        html_content = response.text

        soup = BeautifulSoup(html_content, "html.parser")

        elements = soup.find_all("a", class_="btn-link text-lg lg:text-xl xl:text-2xl")
        verses = []
        for element in elements:
            verse_text = element.text.strip()
            verses.append(verse_text)

        return verses
    except requests.RequestException as e:
        print("Error:", e)

def get_biblie_book_in_king_james_site():
    url = "https://bkjfiel.com.br/"
    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.content

        soup = BeautifulSoup(html_content, "html.parser")

        div = soup.find("div", class_="bg-bkjfiel-offwhite")

        links = []

        if div:
            links_elements = div.find_all("a")

            links = [link["href"] for link in links_elements]

        else:
            print("Div não encontrada.")
    else:
        print("Falha ao carregar a página:", response.status_code)


class TestSorteioVersiculo(unittest.TestCase):
    def test_sorteio_versiculo(self):
        sort_verse()


if __name__ == '__main__':
    unittest.main()
