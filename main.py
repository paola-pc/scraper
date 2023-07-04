import json
from bs4 import BeautifulSoup
import product, contact

final_data = { 
    'contact': contact.contact_results, 
    'products': product.product_results
}

with open('data.json', 'w') as json_file:
    json.dump(final_data, json_file, indent=4)


