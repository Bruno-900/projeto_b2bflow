import requests
from bs4 import BeautifulSoup

def coleta_noticias():
    url = 'https://www.cnnbrasil.com.br/'
    resposta = requests.get(url)
    resposta.raise_for_status()
    
    parser_html = BeautifulSoup(resposta.text, "lxml")
    noticias = parser_html.select("h2.font-bold")

    with open("noticias_coletadas.txt", "w", encoding="utf-8") as f:
        f.write("5 primeiros títulos da CNN Brasil:\n\n")
        for indice, titulo in enumerate(noticias[:5], start=1):
            linha = f"{indice}. {noticias.get_text(strip=True)}\n"
        f.write(linha)
    print("Dados salvos em data/output.txt")

    print("5 primeiros títulos da CNN Brasil:\n")
    for indice, titulo in enumerate(noticias[:5], start=1):
        print(f"{indice}. {titulo.get_text(strip=True)}")

if __name__ == "__main__":
    coleta_noticias()

