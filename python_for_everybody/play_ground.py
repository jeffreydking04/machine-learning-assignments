import re

line = 'QB Russell Wilson is the greatest:here\s why:2013SB.that\'s what we\'re sayin\' \nQB Aaron Rodgers is right:2010SB.ya ya ya'
desired = re.findall('QB.+:(.+)\.', line)
print(desired)
