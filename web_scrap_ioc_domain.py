import requests
import re

# Define the URL of the article you want to extract IOCs from
url = "https://www.example.com/article"

# Make a request to the URL and get the article content
response = requests.get(url)
content = response.text

# Define a regular expression pattern to match IOCs in the article
ioc_pattern = https?:\/\/(?:www\.)?[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,}(?:\/[\w\-\.]*)*\/?

# Find all the matches for the IOC pattern in the article content
iocs = re.findall(ioc_pattern, content)

# Print the list of IOCs found in the article
print("IOCs found in the article:")
for ioc in iocs:
    print(ioc)
