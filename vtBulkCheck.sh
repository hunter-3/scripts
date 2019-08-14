#!/bin/bash
# virustotal checker

# your vt api key
vtApiKey="<api_key>"

# hash array
datHash=(01979e180e36684efdb278bcd700ff7f0802ffff0000000030b6b90600700000
13430bf55ea250553d685a91bc1d37256da233dd34c53c9b29e3ccda79df6a82
13e9929debd4125d361ed8be5f38891859e2f93a87d0640ade27ec2b8daa6bb4
18d7d991968247260c3e40630cde57e93b3f692999ae27eee5d3b7e80573273f
24ca9bffd4cf01f9b7f3ba530c6a6f4ea463e348acfded8ae464e00cb52b506f
2672596e9215f2abad8077a976222abe7e6c205859bbded4de46d79f3b0748ea)
# iteration assignment
datHashLen="${!datHash[*]}"
# set unique timestamp
dateSt=$(date +%s)
# main loop
for i in $datHashLen; do
	{
	# reset vars
	curlResult=""
	curlResultTotal=""
	curlResultPositives=""
	curlResultScanDate=""
	# main curl
	curlResult=$(curl -v --request POST --url https://www.virustotal.com/vtapi/v2/file/report -d apikey=${vtApiKey} -d "resource=${datHash[${i}]}")
	# clean result
	curlResultTotal=$(echo "${curlResult}" | grep -o '"total\"\: [0-9]\{1,3\}')
	curlResultPositives=$(echo "${curlResult}" | grep -o '\"positives\"\: [0-9]\{1,3\}')
	curlResultScanDate=$(echo "${curlResult}" | grep -o '\"scan_date\"\: \"[0-9]\{4\}\-[0-9]\{2\}\-[0-9]\{2\} [0-9]\{2\}\:[0-9]\{2\}\:[0-9]\{2\}\"')
	# output clean
	echo "${datHash[${i}]}, ${curlResultTotal}, ${curlResultPositives}, ${curlResultScanDate}" >>~/Desktop/vt_bulk_hash_${dateSt}.txt
	} &> /dev/null
done
cat ~/Desktop/vt_bulk_hash_${dateSt}.txt

