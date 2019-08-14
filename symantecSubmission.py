mport os
import argparse
import random
import requests
import hashlib
import cStringIO
import time
import sys
from datetime import datetime, timedelta
from ConfigParser import SafeConfigParser
import urllib
import urllib2
import re
import io
import csv



#Read the configuration file
config = SafeConfigParser()
config.read('config.ini')

#Read the command line arguments
parser = argparse.ArgumentParser()

#The user needs to specify specific filename , first name and last name
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-f', '--file', help="File Name" ,action='store')
group.add_argument('-u', '--url', help="URL submission" ,action='store')
group.add_argument('-ha', '--hash', help="Hash submission (CSV file)" ,action='store')
group.add_argument('-m', "--multiple", help="multiple_Hashes", action="store")

parser.add_argument("-fn", "--fname", help="First Name", action="store")
parser.add_argument("-ln", "--lname", help="Last Name", action="store")
parser.add_argument("-s", "--severity", help="Flag Submission as High Severity - on / off (default)", action="store", default='off')
parser.add_argument("-c", "--comments", help="Comments", action="store", default='')


parser.add_argument('args', nargs=argparse.REMAINDER)
args = parser.parse_args()

if args.url is not None:

    #If user has told us it's a URL download it

    print "Downloading " + args.url + "..."

    # User Agents (we can add more in the future)
    useragent_list = (
        'User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
    )

    req_headers = {
            'User-Agent': random.choice(useragent_list),
            'Referer': 'https://submit.symantec.com/websubmit/bcs.cgi'
        }

    #Make the request
    sample_request = requests.get(args.url, headers=req_headers)

    if sample_request.status_code == 200:
        print 'ok'
        #If we grabbed it, dump it into a StringIO object so we can use it

        holdingfile = cStringIO.StringIO()
        holdingfile.write(sample_request.content)

        #Put the file into the variable and generate a hash for the filename

        file = sample_request.content
        filename = hashlib.sha256(sample_request.content).hexdigest()

    else:

        #If it doesn't return a 200, abort....
        print args.url + " did not return HTTP 200..."
        sys.exit(1)

if args.file is not None:

    #If it's a file read it in and

    file = open(args.file, 'rb')
    filename = os.path.basename(args.file)

print "Submitting File..."

#Specific UA
useragent_list = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36']





req_headers = {
        'User-Agent': random.choice(useragent_list),
        'Referer': 'https://submit.symantec.com/websubmit/bcs.cgi'
    }
submission_url = "https://submit.symantec.com/websubmit/bcs.cgi"

args.hash_value=''
args.hash_value=args.hash

if  args.hash is  None:
    args.stype = 'upfile'
else: args.stype = 'hash'

payload = {'mode' : '2',
           'fname'  :   args.fname,
           'lname'  :   args.lname,
           'cname'  :  'paypal',
           'email'  :  'DL-PP-GSS-IR@paypal.com',
           'email2' :  'DL-PP-GSS-IR@paypal.com',
           'pin'    :  '468480653483',
           'stype'  :   args.stype,
           'url'    :  '',
           'hash'   :   args.hash_value,
           'critical' : args.severity,
           'comments' : args.comments,
}

#attaching the file

#print payload



if args.file or args.url is not None:
 files = {'upfile' : (filename, file)}
 #Submit the request (URL OR File)
 #print payload
 r = requests.post(submission_url, payload, files=files,headers=req_headers)

 #FIXME: Print out the Page
 #print r.text


if args.hash is not None:
 files = {'upfile' : ''}
 r = requests.post(submission_url, payload, files=files,headers=req_headers)
 #Submit the request (Hash)
 #print payload
 #print r.text

 regex = re.compile("\<p\>(.*?)\.\<\/p\>")
 sub_response=regex.search(r.text).group(1)
 print "Submission Response: " +  sub_response


if args.multiple is not None:
 print ("Multiple Hashes")

 f = open(args.multiple, 'rb')
 reader = csv.reader(f)
 lines = list(reader)
 count =len(lines)

 time=time.strftime("%a %b %d %H:%M:%S %Y")
 Hash_list=[]
 Hash_list.append("The list of Hashes that have not been uploaded: \n" +'Date: ' + time)

 for i in range(count):
    #New HashName
    HashName=" " .join(lines[i])
    print HashName

    #Convert the Hash as argument
    args.hash_value=HashName

    useragent_list = [
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36']

    req_headers = {
            'User-Agent': random.choice(useragent_list),
            'Referer': 'https://submit.symantec.com/websubmit/bcs.cgi'
        }
    submission_url = "https://submit.symantec.com/websubmit/bcs.cgi"


    payload = {'mode' : '2',
               'fname'  :   args.fname,
               'lname'  :   args.lname,
               'cname'  :  'paypal',
               'email'  :  'DL-PP-GSS-IR@paypal.com',
               'email2' :  'DL-PP-GSS-IR@paypal.com',
               'pin'    :  '468480653483',
               'stype'  :   'hash',
               'url'    :  '',
               'hash'   :   args.hash_value,
               'critical' : args.severity,
               'comments' : args.comments,
    }


    #Uploade the hash
    files = {'upfile' : ''}
    r = requests.post(submission_url, payload, files=files,headers=req_headers)

    # printing the error message
    regex = re.compile("\<p\>(.*?)\.\<\/p\>")
    sub_response=regex.search(r.text).group(1)
    print "Submission Response: " +  sub_response
    if sub_response == "This file is not publicly available by hash. Please submit the original file":
       Hash_list.append("\n" + args.hash_value)


    Len_List= len(Hash_list)
    if  Len_List > 1 and count-1 == i:
        print "\n" .join(Hash_list)
        print "Please see HashName_file.txt"

        HashName_file = open('HashName_file.txt', 'w+')
        for j in  range(Len_List):
            HashName_file.write("%s\n" % Hash_list[j])
        HashName_file.close()


    #print r.text


#FIXME: Print out the Page
