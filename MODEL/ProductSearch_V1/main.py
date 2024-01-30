# https://serpapi.com/blog/scrape-google-lens/
# pip install google-search-results

from serpapi import GoogleSearch
import json

params = {
    'api_key': 'fd62426a36c60b0a86f6b225426b2ecf37dc8a6373c6b14542b0cc55981d06f5',
    'engine': 'google_lens',
    'url': 'CLIENTVIEW/images/productImg.png',
    'hl': 'es'
}

# Performs the image product search
search = GoogleSearch(params)
lensResult = search.get_dict()

# Delete information about request that we don't need
del lensResult['search_metadata']
del lensResult['search_parameters']

print(json.dumps(lensResult, indent=2, ensure_ascii=False))