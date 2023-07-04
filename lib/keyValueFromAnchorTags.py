import re

def key_value_from_anchor_tags (tag, baseURL=''):
  # use this function for using the content of the tag as the key and the href as the value.
  if len(baseURL) == 0 : return [tag.contents[0], tag.get('href')]
  #if some anchor tags include the domain but others don't:
  path_pattern = r'(?:https?://[^/]+)?(/[^"]*)'
  path = re.findall(path_pattern, tag.get('href'))[0] or ''
  return {'key': tag.contents[0], 'value': baseURL+path}