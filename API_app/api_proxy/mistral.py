import requests  

def ask_mistral(articles_data, user_prompt, mistral_api_key):

    articles_text = ""
    for i, article in enumerate(articles_data.get("articles", [])):
        title = article.get("title", "")
        description = article.get("description", "")
        content = article.get("content", "")
        articles_text += f"\n Статья {i+1} \nНазвание: {title}\nОписание: {description}\nСодержание: {content[:500]}\n"
    
    full_prompt = f"{user_prompt}\nВот статьи:\n{articles_text}"
    
    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {mistral_api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "mistral-small-latest",  
        "messages": [
            {"role": "user", "content": full_prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 500
    }
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Ошибка: {response.status_code} - {response.text}"