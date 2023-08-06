from bs4 import BeautifulSoup
import requests

class Labrar:
    def despliega_agentes(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Un ejemplo simple, extrae todos los párrafos de la página
        paragraphs = soup.find_all('p')
        return [p.text for p in paragraphs]
