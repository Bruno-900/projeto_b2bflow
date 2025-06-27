import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import time

def coleta_html(endereco_url: str):
    """
    Faz requisição GET e retorna o objeto BeautifulSoup,
    ou None em caso de falha.
    """
    try:
        resposta = requests.get(endereco_url, timeout=10)
        resposta.raise_for_status()
        return BeautifulSoup(resposta.text, "lxml")
    except requests.exceptions.RequestException as erro:
        print(f"Erro ao baixar {endereco_url}: {erro}")
        return None

# Pausa de 1 segundo entre requisições
time.sleep(1)

def obter_com_retentativas(endereco_url: str, num_tentativas: int = 3):
    """
    Tenta baixar uma URL várias vezes antes de desistir.
    Retorna o objeto Response ou None.
    """
    for tentativa_atual in range(1, num_tentativas + 1):
        try:
            resposta = requests.get(endereco_url, timeout=10)
            resposta.raise_for_status()
            return resposta
        except requests.exceptions.RequestException as erro:
            print(f"Tentativa {tentativa_atual} para {endereco_url} falhou: {erro}. Tentando novamente…")
            time.sleep(1)
    print(f"Todas as {num_tentativas} tentativas falharam para {endereco_url}")
    return None


#Funçao que usa o link da noticia para acessar a data de publicação.
def extrai_data_por_link(url: str) -> str:
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "lxml")
        time_tag = soup.find("time")
        if time_tag:
            return time_tag.get("datetime", time_tag.get_text(strip=True))
    except Exception:
        pass
    return "sem data"


#Funçao que usa o link da noticia para acessar o primeiro paragrafo da noticia e criar um resumo.
def extrai_resumo(url: str) -> str:
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "lxml")
        artigo = soup.find("article")
        p = artigo.find("p") if artigo else soup.find("p")
        return p.get_text(strip=True) if p else "sem resumo"
    except Exception:
        return "sem resumo"

#Função para coletar as noticias no site da CNN (https://www.cnnbrasil.com.br)
def coleta_noticias():
    url = 'https://www.cnnbrasil.com.br/'
    resp = requests.get(url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "lxml")
    noticias = soup.select("h2.font-bold")

    resultados = []  # 1) lista onde vamos acumular dicts

    # 2) gravação do arquivo de texto
    with open("NOTICIAS/noticias_coletadas.txt", "w", encoding="utf-8") as f:
        f.write("5 primeiras notícias da CNN Brasil:\n\n")
        for i, titulo_tag in enumerate(noticias[:5], start=1):
            titulo_txt = titulo_tag.get_text(strip=True)
            parent_a = titulo_tag.find_parent("a")
            link = parent_a["href"] if parent_a and parent_a.has_attr("href") else "sem link"
            data = extrai_data_por_link(link) if link.startswith("http") else "sem data"
            resumo = extrai_resumo(link) if link.startswith("http") else "sem resumo"

            # 3) adiciona o dict à lista
            resultados.append({
                "titulo": titulo_txt,
                "link": link,
                "data": data,
                "resumo": resumo
            })

            # 4) escreve no texto
            f.write(f"{i}. {titulo_txt}\n\n")
            f.write(f"   Resumo: {resumo}\n\n")               #Resumo da noticia(primeiro paragrafo).
            f.write(f"   Data: {data}\n\n")                   #Data da noticia.
            f.write(f"   Link: {link}\n\n")                   #link para a pagina da noticia.
            
    print("Dados salvos em noticias_coletadas.txt")

    # 5) salvar em CSV
    df = pd.DataFrame(resultados)
    df.to_csv("NOTICIAS/csv_noticias.csv", index=False, encoding="utf-8")
    print("CSV salvo em data/output.csv")

    # 6) salvar em JSON
    with open("NOTICIAS/json_noticias.json", "w", encoding="utf-8") as jf:
        json.dump(resultados, jf, ensure_ascii=False, indent=2)
    print("JSON salvo em data/output.json")

if __name__ == "__main__":
    coleta_noticias()
