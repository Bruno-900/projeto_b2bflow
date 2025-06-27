# CNN Brasil Scraper

Este projeto realiza **web scraping** no site [CNN Brasil](https://www.cnnbrasil.com.br/) e coleta as 5 primeiras manchetes de destaque da página principal, extraindo:

- Título da notícia  
- Link direto para a matéria  
- Data de publicação (quando disponível)  
- Primeiro parágrafo da matéria (resumo)

  ## Código principal (main.py)

![Captura de tela 2025-06-27 154745](https://github.com/user-attachments/assets/4c1c0ec7-379b-4327-9f88-0bf75e49eade)


Os dados são salvos em **três formatos**:
- `noticias_coletadas.txt` (leitura simples)
- `csv_noticias.csv` (planilha estruturada)
- `json_noticias.json` (formato estruturado)

---

🚀 Como usar o projeto
1. Clone o repositório

git clone https://github.com/seuusuario/coletor-noticias-cnn.git
cd coletor-noticias-cnn

2. (Opcional, mas recomendado) Crie um ambiente virtual

# Linux/macOS
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate

3. Instale as dependências

pip install -r requirements.txt

4. Crie a pasta data/ para salvar os arquivos (opcional)
mkdir data

5. Execute o script principal

python main.py
🧾 Requisitos
Python 3.8+

requests

beautifulsoup4

lxml

pandas

Todas as dependências serão instaladas automaticamente com o requirements.txt.

📦 Saídas Geradas
noticias_coletadas.txt → resumo legível das 5 notícias.

![Captura de tela 2025-06-27 155002](https://github.com/user-attachments/assets/bf2fbbfa-1c83-411f-b55b-1f6cd00d173c)


csv_noticias.csv → estrutura tabular com colunas: título, link, data, resumo.

![Captura de tela 2025-06-27 155015](https://github.com/user-attachments/assets/146050c2-4946-4f37-9bb4-83dba02cca7f)


json_noticias.json → lista de dicionários no formato JSON com os mesmos campos.

![Captura de tela 2025-06-27 155008](https://github.com/user-attachments/assets/72a1d9f6-0ef9-4323-ab50-4f308ad7cb36)


Todos os arquivos são gerados dentro da pasta noticias/.

💡 Funcionalidades Extras
Tratamento de exceções: falhas de conexão ou páginas com estrutura inesperada são tratadas com segurança.

Delay entre requisições: inclui time.sleep() para evitar sobrecarga no servidor.

Retentativas automáticas: o script tenta até 3 vezes em caso de erro de rede.

📌 Exemplo de Resultado (resumido)

1. Título da Notícia
   Resumo: Primeiro parágrafo do artigo...
   Link: https://cnn.com.br/noticia-exemplo
   Data: 2025-06-26T08:00:00

📁 Estrutura do Projeto

├── data/
│   ├── noticias_coletadas.txt
│   ├── csv_noticias.csv
│   └── json_noticias.json
├── main.py
├── requirements.txt
└── README.md
