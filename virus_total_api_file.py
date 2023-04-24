import requests

# Set API key and endpoint URL
api_key = 'YOUR_API_KEY_HERE'
endpoint_url = 'https://www.virustotal.com/vtapi/v2/file/report'

# Prompt user for file path
file_path = input("Enter file path: ")

# Set parameters for API request
params = {'apikey': api_key, 'resource': file_path}

# Send API request and retrieve response
response = requests.get(endpoint_url, params=params)

# Parse response and print results
json_response = response.json()
if json_response['response_code'] == 0:
    print('File not found on VirusTotal.')
else:
    print('Detection ratio: {}/{}'.format(json_response['positives'], json_response['total']))
    print('Scan date: {}'.format(json_response['scan_date']))
    print('MD5 hash: {}'.format(json_response['md5']))
