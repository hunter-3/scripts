#!/bin/env python3
# import os > commands to terminal
import os

# Merge pcap files > Must run out of directory where pcaps are stored

os.system("mergecap *.pcap -w merged.pcap")

# Output > IP.csv using tshark > Distinct count on src ip's
os.system("tshark -r merged.pcap -T fields -e ip.src | sort | uniq -c | sort -nr > ip.csv")

#  Text file for whois and shodan
os.system("tshark -r merged.pcap -T fields -e ip.src | sort | uniq | sort -nr > ip.txt")

# Creating whois file
os.system("for i in `cat ip.txt`; do whois $i >> whois.txt; done")

# Shodan API for running IPs through

# Display Folder contents > Not needed > check all files are created when completed
os.system("ls -al")
