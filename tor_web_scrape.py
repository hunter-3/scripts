import requests

response = requests.get('https://www.dan.me.uk/torlist/?exit')
response.status_code
tor_list = open('tor_exit_updated.txt', 'w')
print(response.text, file=tor_list)
tor_list.close()
