import re
"""
pattern = 'this'
text = 'Does this text match the pattern?'

match = re.search(pattern, text)

s = match.start()
e = match.end()

print 'Found "%s"\nin "%s"\nfrom %d to %d("%s")' %\
    (match.re.pattern, match.string, s, e, text[s:e])


regexes = [re.compile(p)
            for p in ["this", "that"]
          ]

print 'Text: %r\n' % text

for regex in regexes:
    print "Searching for", regex.pattern

    if regex.search(text):
        print 'Match!'
    else:
        print 'No match!'
"""

newString = 'This is the best string ever!'
def seeker(patt):
    thePattern = patt
    Chill = re.search(thePattern, newString)
    if Chill:
        print '%r is in the string!' % thePattern
    elif not Chill:
        print '%r is not in the string :(' % thePattern


print "This is the string you are going to search through:\n"

print newString, '\n'

entry = raw_input('What would you like to search this string for?\n')
seeker(entry)
