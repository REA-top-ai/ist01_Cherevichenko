def anal(params: dict) -> list:
    default_params = []
    for article in params['articles']:
        if len(default_params) == 50:
            break
        if article.get('title') and article.get('url') and len(''.join(article.get('description'))) >= 50:
            default_params.append({
                    'title': article['title'],
                    'source': article['source']['name'] if article.get('source') and article['source'].get('name') else '',
                    'published': article.get('publishedAt', ''),
                    'author': article.get('author', '')
                })
    return default_params 