import re

text = 'https://github.com/metersphere/metersphere/blob/master/README.md'

regex = 'README.md'

r = re.search(regex, text)

print(r)