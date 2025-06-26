2.Coletar a data de publicação

Localizar a tag <time> ou outro elemento que contenha a data.

Ler o atributo datetime ou o texto interno e incluir no output.

3.Implementar paginação

Identificar o seletor ou URL da “próxima página” no site.

Loop que percorre N páginas (ou até não haver mais “next”), acumulando resultados.

4.Gerar saída estruturada (CSV/JSON)

Montar um list[dict] com campos titulo, link, data.

Usar pandas ou json para salvar em data/output.csv ou data/output.json.

5.Resumir conteúdos (opcional)

Para cada link, fazer nova requisição e extrair o primeiro parágrafo da matéria.

Incluir esse resumo no seu arquivo de saída.

6.Adicionar barras de progresso

Integrar tqdm no loop de iteração (páginas ou itens), para feedback visual.

7.Tratamento de exceções e delays

Capturar possíveis erros de requisição (timeouts, status != 200).

Inserir time.sleep() entre requisições para respeitar o servidor.