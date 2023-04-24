import csv
import requests
from bs4 import BeautifulSoup

# Set the URL of the online article
url = "https://example.com/article"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Define a list to store the IOCs
iocs = []

# Find all the text in the article
article_text = soup.get_text()

# Parse the text for IOCs using regular expressions or other methods
# Here's an example regex pattern for IP addresses:
import re
ip_pattern = re.compile(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b")
for match in ip_pattern.finditer(article_text):
    iocs.append(match.group())

# Define the name of the CSV file to write the IOCs to
csv_file = "iocs.csv"

# Open the CSV file in write mode and create a CSV writer object
with open(csv_file, "w", newline="") as f:
    writer = csv.writer(f)

    # Write the IOCs to the CSV file
    writer.writerow(["IOC"])
    for ioc in iocs:
        writer.writerow([ioc])

# Print a message to indicate the script has completed
print(f"IOCs written to {csv_file}.")
