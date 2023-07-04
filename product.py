import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
from lib import keyValueFromAnchorTags

contact_url = 'https://reviewpro.shijigroup.com'
html = urllib.request.urlopen(contact_url)
soup = BeautifulSoup(html, 'html.parser')

dropdown = soup.find('div', class_= 'nav_dropdown-list').findAll(class_='nav_dropdown-block')
product_results = {'products': {}, 'essential': {}}

block = 0
while block < len(dropdown):
  category = 'products' if block == 0 else 'essential'
  for a_tags in dropdown[block].findAll('a'):
    key_value = keyValueFromAnchorTags.key_value_from_anchor_tags(a_tags, 'https://www.shijigroup.com')
    product_results[category][key_value['key']] = key_value['value']
  block += 1



