import requests
import socket
from bs4 import BeautifulSoup


def get_website_text(url):
    # Criando objeto de requisição com cabeçalho de usuário aleatório
    headers = {'User-Agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=headers)

    # Obtendo o endereço IP do domínio da página
    ip_address = socket.gethostbyname(res.url.split('/')[2])

    # Extraindo o texto da página
    soup = BeautifulSoup(res.text, 'html.parser')
    texto_extraido = soup.get_text()

    return texto_extraido
