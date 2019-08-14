#!/bin/env python3
# Process pcap files into usable formats
# import os > commands to terminal
# Merge pcap files > Must run out of directory where pcaps are stored
# Output > IP.csv using tshark > Distinct count on src ip's

import os


# Merge pcap files

os.system("mergecap *.pcap -w ddos.pcap")

# Process merged pcap file to pull out unique src IP's

os.system("tshark -r ddos.pcap -T fields -e ip.src | sort | uniq -c | sort -nr > ddos.csv")

# Protocol Hierarchy Statistics

os.system("tshark -q -r ddos.pcap -z io,phs > protocol_stats.txt")

# Packet Length breakdown

os.system("tshark -nr ddos.pcap -q -z plen,tree > packet_length.txt")

#   whois and shodan
#       Command tshark -r ddos.pcap -T fields -e ip.src | uniq > ip.txt
# os.system("tshark -r ddos.pcap -T fields -e ip.src | sort | uniq | sort -nr > ip.txt")
# Creating whois file
# os.system("for i in `cat ip.txt`; do whois $i >> whois.txt; done")

# Splunk Rest API for CSV upload > Don't like creds hard code in the curl command
#curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/data/lookup-table-files -d eai:data=/opt/splunk/var/run/splunk/lookup_tmp/lookup-in-staging-dir.csv -d name=lookup.csv

# Shodan API > install python library for shodan > Bulk lookup Corp API key (100 per request)

# View files created
os.system("ls -al")
