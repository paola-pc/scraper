import urllib.request, urllib.parse, urllib.error
import re
from lib import getNextAnchor
from bs4 import BeautifulSoup

contact_url = 'https://reviewpro.shijigroup.com/team#contact'
html = urllib.request.urlopen(contact_url)
soup = BeautifulSoup(html, 'html.parser')

contact_grid_sections = soup.find('div', class_= 'contact_grid').find_all('h3')
customer_suport_string_refs = ['EMEA', 'APAC', 'China', 'USA', 'Australia & New Zealand']
mail_re = r'[\w\.-]+@[\w\.-]+'
contact_results = {}

for contact_section in contact_grid_sections:
  if contact_section.contents[0] == 'Customer Support':
    references = {}
    for string_ref in customer_suport_string_refs:
      references[string_ref] = getNextAnchor.get_next_anchor(mail_re, soup, 'div', string_ref, )
    contact_results['Customer Support'] = references
  else:
    if len(contact_section.fetchNextSiblings('a')) > 1:
        links = []
        for link in contact_section.fetchNextSiblings('a'):
           links.append(re.findall(mail_re, link.get('href'))[0])
        contact_results[contact_section.contents[0]] = links
    else:
       contact_results[contact_section.contents[0]] = getNextAnchor.get_next_anchor(mail_re, None, None, section=contact_section)



