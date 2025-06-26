import requests
from bs4 import BeautifulSoup
import pandas

def coleta_noticias():
    url = 'https://www.cnnbrasil.com.br/'
    resposta = requests.get(url)
    resposta.raise_for_status()
    
    parser_html = BeautifulSoup(resposta.text, "lxml")
    noticias = parser_html.select("h2.font-bold")

    with open("noticias_coletadas.txt", "w", encoding="utf-8") as f:
        f.write("5 primeiros títulos da CNN Brasil:\n\n")
        for indice, titulo in enumerate(noticias[:5], start=1):
            
            
            texto = titulo.get_text(strip=True)    
            
            #Coleta o link da noticia.
            tag_a = titulo.find_parent("a")
            link = tag_a["href"] if tag_a and tag_a.has_attr("href") else "sem link"

            #coleta adata da noticia
            data_tag = titulo.find_next("time")
            if data_tag and data_tag.has_attr("datetime"):
               data = data_tag["datetime"]
            elif data_tag:
               data = data_tag.get_text(strip=True)
            else:
               data = "sem data"             
            
            f.write(f"{indice}. {texto}\n")
            f.write(f"   Link: {link}\n\n")                #Cria um link para cada noticia.
            f.write(f"   Data: {data}\n\n")                #A data de cada noticia.

    print("Dados salvos em data/output.txt")

    print("5 primeiros títulos da CNN Brasil:\n")
    for indice, titulo in enumerate(noticias[:5], start=1):
        print(f"{indice}. {titulo.get_text(strip=True)}")

if __name__ == "__main__":
    coleta_noticias()
