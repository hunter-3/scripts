#!/bin/env python3
# import os > commands to terminal
import os

# Merge pcap files

os.system("mergecap *.pcap -w merged.pcap")

# Output > IP.csv using tshark > Distinct count on src ip's
os.system("tshark -r ddos.pcap -T fields -e ip.src | sort | uniq -c | sort -nr > ddos.csv")

#  Text file for whois and shodan
#       Command tshark -r ddos.pcap -T fields -e ip.src | uniq > ip.txt
os.system("tshark -r ddos.pcap -T fields -e ip.src | sort | uniq | sort -nr > ip.txt")

# Creating whois file
os.system("for i in `cat ip.txt`; do whois $i >> whois.txt; done")

# Shodan API for running IPs through

# Display Folder contents
os.system("ls -al")
