import re
from bs4 import BeautifulSoup
import requests

# Solicitando o site do usuário
site_do_usuario = input("Digite o URL do site que você deseja extrair: ")

# Fazendo a requisição para o site
site = requests.get(site_do_usuario).content

# Criando o objeto BeautifulSoup
soup = BeautifulSoup(site, 'html.parser')

# Solicitando as palavras-chave do usuário
palavras_chave = input("Digite as palavras-chave que você está procurando, separadas por vírgula: ").split(',')

# Procurando as palavras-chave no site
resultados = {}
for palavra in palavras_chave:
    resultados[palavra] = soup.body(text=re.compile(palavra))

# Imprimindo os resultados
for palavra, ocorrencias in resultados.items():
    print(f"\nPalavra-chave: {palavra}")
    for ocorrencia in ocorrencias:
        print(f"Ocorrência: {ocorrencia}")
