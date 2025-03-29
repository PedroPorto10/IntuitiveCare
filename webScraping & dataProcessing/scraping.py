import requests
from bs4 import BeautifulSoup
import zipfile

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
resposta = requests.get(url)

if resposta.status_code == 200:
    conteudo = resposta.content
    sopa = BeautifulSoup(conteudo, "html.parser")

    lista_links = []
    for elemento in sopa.find_all("a", href=True):
        if elemento["href"].endswith(".pdf"):
            lista_links.append(elemento["href"])

    for link_pdf in lista_links:
        resposta_pdf = requests.get(link_pdf)
        if resposta_pdf.status_code == 200:
            with open(link_pdf.split("/")[-1], "wb") as arquivo_pdf:
                arquivo_pdf.write(resposta_pdf.content)
        else:
            print(f"Erro ao baixar {link_pdf}")

    with zipfile.ZipFile("arquivos.zip", "w") as arquivo_zip:
        for link_pdf in lista_links:
            arquivo_zip.write(link_pdf.split("/")[-1])

    print("Download e compactação concluídos com sucesso!")
else:
    print("Erro ao acessar o site")
