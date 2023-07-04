import re

# Use the content of the tag as the key and the href as the value.
def key_value_from_anchor_tags (tag, baseURL=''):
  if tag.get('href').startswith('http') == True: 
    return {'key': tag.contents[0], 'value': tag.get('href')}
  # if some anchor tags don't include the domain we assume is the baseURL:
  path_pattern = r'(?:https?://[^/]+)?(/[^"]*)'
  path = re.findall(path_pattern, tag.get('href'))[0] or ''
  return {'key': tag.contents[0], 'value': baseURL+path}