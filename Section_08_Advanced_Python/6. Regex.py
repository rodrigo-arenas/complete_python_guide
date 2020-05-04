import re

email = 'some.email@email.com'
expression = '[a-z\.]+'  # Encuentra letras o un punto

matches = re.findall(expression, email)
print(matches)

price = 'Price: $125.236'
expression = 'Price: \$([0-9,]*\.[0-9]*)'
matches = re.search(expression, price)
print(matches.group(0))  # Todo lo que cruce
print(matches.group(1))  # Lo que esté dentro del paréntesis de la expresión
