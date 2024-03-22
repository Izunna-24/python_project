# r'\d+[A-Z][a-z]*[A-Z][a-z]*'
#
import re

check = 'yes' if re.fullmatch(r'\d+ [A-Z][a-z]*[A-Z][a-z]*', '1 IzvccdAkk') else 'No'
print(check)
