import sys
import requests

PORT = 45818
ROUTE = '/qWrite'

# read questions
with open(sys.argv[1], 'r') as f:
    text = f.read()

questions = text.split('\n\n')

url = 'http://188.166.160.44:{}{}'.format(PORT, ROUTE)
data = {'questions': questions}
response = requests.post(url, json=data)
print(response.text)
