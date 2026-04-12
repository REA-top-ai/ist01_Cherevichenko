from datetime import date, timedelta
from .mistral import ask_mistral
import requests as req

mistal_api_key = 'CUF6JCSM5ILfgKknw0HSOUfayPabtG4P'
base_url = 'https://newsapi.org/v2'

def _make_request(endpoint: str, api_key: str, params: dict = None) -> dict[str: str]:
    url = f'{base_url}/{endpoint}'
    default_params = {'apiKey': api_key}

    if params:
        default_params.update(params)
    
    try:
        response = req.get(url=url, params=default_params, timeout=10)
        return response.json()  

    except req.exceptions.RequestException as error:
        raise Exception(f'Ошибка в запросе к NewsAPI ({endpoint}): {error}')
    
    except ValueError as error:
        raise Exception(f'Ошибка парсинга JSON: {error}')


def get_top_headlines(api_key: str, q: str, country: str = None, category: str = None, sources: str = None, page_size: int = None, page: int = None) -> dict:
    allowed_params = {'q': q, 'country': country, 'category': category, 'sources': sources, 'pageSize': page_size, 'page': page}
    
    params = {key: value for key, value in allowed_params.items() if value is not None}

    return _make_request('top-headlines', api_key, params)


def get_everything(api_key: str, q: str, search_in: str = None, sources: str = None, domains: str = None, exclude_domains: str = None, w_from: str = None, to: str = None, language: str = None, sort_by: str = None, page_size: int = None, page: int = None) -> dict:
    allowed_params = {'q': q, 'searchIn': search_in, 'sources': sources, 'domains': domains, 'excludeDomains': exclude_domains, 'from': w_from, 'to': to, 'language': language, 'sortBy': sort_by, 'pageSize': page_size, 'page': page}
    
    params = {key: value for key, value in allowed_params.items() if value is not None}

    return _make_request('everything', api_key, params)


def get_sources(api_key: str, category: str = None, language: str = None, country: str = None) -> dict:
    allowed_params = {'category': category, 'language': language, 'country': country}

    params = {key: value for key, value in allowed_params.items() if value is not None}

    return _make_request('top-headlines/sources', api_key, params)



def articles_from_yesterday(api_key):
    date_from = date.today() - timedelta(days=1)
    date_to = date.today() - timedelta(days=1)

    prompt = 'По представленным статьям напиши краткую выжимку на 250-300 слов'

    result = get_everything(
        q='apple',
        api_key=api_key,
        sort_by="publishedAt",
        w_from=date_from,
        to=date_to,
        language='en'
   )
    
    if result and result.get("status") == "ok":
        mistral_answer = ask_mistral(result, prompt, mistal_api_key)
        with open("mistral_results/mistral_results.txt", "w", encoding="utf-8") as f:
            f.write(mistral_answer)


    