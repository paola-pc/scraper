import urllib.request, urllib.parse, urllib.error
import re
import json
from bs4 import BeautifulSoup

contact_url = 'https://reviewpro.shijigroup.com/team#contact'
html = urllib.request.urlopen(contact_url)
soup = BeautifulSoup(html, 'html.parser')

contact_grid_sections = soup.find('div', class_= 'contact_grid').find_all('h3')
customer_suport_string_refs = ['EMEA', 'APAC', 'China', 'USA', 'Australia & New Zealand']
mail_re = r'[\w\.-]+@[\w\.-]+'
contact_results = {}

def getNextAnchor(custom_re, tag=None, text=None, section=None):
    if section == None : 
       section = soup.find(tag, string=text)
    rawLink = section.find_next('a').get('href')
    return re.findall(custom_re, rawLink)[0]

for contact_section in contact_grid_sections:
  if contact_section.contents[0] == 'Customer Support':
    references = {}
    for string_ref in customer_suport_string_refs:
      references[string_ref] = getNextAnchor(mail_re, 'div', string_ref, )
    contact_results['Customer Support'] = references
  else:
    if len(contact_section.fetchNextSiblings('a')) > 1:
        links = []
        for link in contact_section.fetchNextSiblings('a'):
           links.append(re.findall(mail_re, link.get('href'))[0])
        contact_results[contact_section.contents[0]] = links
    else:
       contact_results[contact_section.contents[0]] = getNextAnchor(mail_re, None, None, section=contact_section)
       

dropdown = soup.find('div', class_= 'nav_dropdown-list').findAll(class_='nav_dropdown-block')
product_results = {'products': {}, 'essential': {}}
block = 0
while block < len(dropdown):
  category = 'products' if block == 0 else 'essential'
  for a_tags in dropdown[block].findAll('a'):
    baseUrl = 'https://www.shijigroup.com'
    link_destructured = re.findall('https://www.shijigroup.com?|(.+)', a_tags.get('href'))
    endpoint = link_destructured[len(link_destructured)-1]
    product_results[category][a_tags.contents[0]] = baseUrl + endpoint
  block += 1

final_data = { 'contact': contact_results, 'products': product_results}
with open('data.json', 'w') as json_file:
    json.dump(final_data, json_file, indent=4)
