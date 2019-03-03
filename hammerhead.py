#!/bin/env python3
# import os > commands to terminal
# Merge pcap files > Must run out of directory where pcaps are stored
# Output > IP.csv using tshark > Distinct count on src ip's
#  Text file for whois and shodan
# Creating whois file
# Display Folder contents > Not needed > check all files are created when completed

import os

os.system("mergecap *.pcap -w merged.pcap")

os.system("tshark -r merged.pcap -T fields -e ip.src | sort | uniq -c | sort -nr > ip.csv")

os.system("tshark -r merged.pcap -T fields -e ip.src | sort | uniq | sort -nr > ip.txt")

os.system("for i in `cat ip.txt`; do whois $i >> whois.txt; done")

os.system("ls -al")
