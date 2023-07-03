import urllib.request, urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup

url = input('Enter a URL: ')
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

contact_grid_sections = soup.find('div', class_= 'contact_grid').find_all('h3')
customer_suport_string_refs = ['EMEA', 'APAC', 'China', 'USA', 'Australia & New Zealand']
mail_re = '^mailto:(.+)'

def getNextAnchor(custom_re, tag=None, text=None, section=None):
    if section == None : 
       section = soup.find(tag, string=text)
    rawLink = section.find_next('a').get('href')
    return re.findall(custom_re, rawLink)[0]

for contact_section in contact_grid_sections:
  print(contact_section.contents[0])
  if contact_section.contents[0] == 'Customer Support':
     for string_ref in customer_suport_string_refs:
      print('·',string_ref, ':', getNextAnchor(mail_re, 'div', string_ref, ))
  else:
     print('·', getNextAnchor(mail_re, None, None, section=contact_section))

#  https://reviewpro.shijigroup.com/team#contact