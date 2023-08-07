```python
import requests
from bs4 import BeautifulSoup

def search_product_alternatives(product_name):
    search_url = f"https://www.google.com/search?q={product_name}"
    response = requests.get(search_url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        search_results = soup.find_all('div', class_='g')
        
        alternatives = []
        for result in search_results:
            title = result.find('h3').get_text()
            link = result.find('a')['href']
            alternatives.append({'title': title, 'link': link})
        
        return alternatives
    else:
        return None
```