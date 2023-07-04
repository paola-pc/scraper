import re

def get_next_anchor(custom_re, soup, tag=None, text=None, section=None):
    if section == None : 
       section = soup.find(tag, string=text)
    rawLink = section.find_next('a').get('href')
    return re.findall(custom_re, rawLink)[0]