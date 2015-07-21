import re


text = 'abaaaaaabaaabbb'
pattern = 'ab'


for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print 'Found', text[s:e], 'at', s, e
