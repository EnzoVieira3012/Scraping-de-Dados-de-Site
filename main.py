import requests
from bs4 import BeautifulSoup


def fetch_page(url):
    """Obtém o conteúdo HTML da página."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lança um erro para códigos de status HTTP 4xx/5xx
        return response.text
    except requests.RequestException as e:
        print(f"Erro ao acessar {url}: {e}")
        return None


def parse_html(html_content):
    """Analisa o HTML e extrai informações."""
    soup = BeautifulSoup(html_content, 'html.parser')
    articles = []

    # Exemplo fictício de seleção de elementos de um site de notícias
    for item in soup.find_all('div', class_='news-item'):
        title = item.find('h2').get_text(strip=True)
        summary = item.find('p', class_='summary').get_text(strip=True)
        articles.append({'title': title, 'summary': summary})

    return articles


def print_articles(articles):
    """Exibe as informações extraídas de forma organizada."""
    if not articles:
        print("Nenhuma notícia encontrada.")
        return

    for i, article in enumerate(articles, start=1):
        print(f"Notícia {i}:")
        print(f"Título: {article['title']}")
        print(f"Resumo: {article['summary']}")
        print("-" * 40)


def main():
    print("Bem-vindo ao scraper de notícias!")

    while True:
        url = input("Digite a URL para scraping (ou 'sair' para encerrar): ")
        if url.lower() == 'sair':
            print("Saindo...")
            break

        html_content = fetch_page(url)

        if html_content:
            articles = parse_html(html_content)
            print_articles(articles)


if __name__ == "__main__":
    main()
