# I tried rename but this file is created when Splunk is started without issue

# Just going to delete the file to avoid further cleanup of the renamed file

 

Remove-Item -Path "C:\Program Files\SplunkUniversalForwarder\etc\auth\server.pem"

 

# We need to write these values to the conf files to generate key size we want

#

# C:\Program Files\SplunkUniversalForwarder\etc\system\local\server.conf

# [sslConfig]

# certCreateScript = $SPLUNK_HOME/bin/splunk, createssl, server-cert, 2048

#

# C:\Program Files\SplunkUniversalForwarder\etc\system\local\distsearch.conf

# [tokenExchKeys]

# genKeyScript = $SPLUNK_HOME/bin/splunk, createssl, audit-keys, 2048

#

# Add the content to each confile

 

Add-Content -Path "C:\Program Files\SplunkUniversalForwarder\etc\system\local\server.conf" -Value ""

Add-Content -Path "C:\Program Files\SplunkUniversalForwarder\etc\system\local\server.conf" -Value "[sslConfig]"

Add-Content -Path "C:\Program Files\SplunkUniversalForwarder\etc\system\local\server.conf" -Value "certCreateScript = C:\Program Files\SplunkUniversalForwarder\bin\splunk, createssl, server-cert, 3072"

 

# Check to see if file C:\Program Files\SplunkUniversalForwarder\etc\system\local\distsearch.conf exists

 

if (!(Test-Path "C:\Program Files\SplunkUniversalForwarder\etc\system\local\distsearch.conf"))

{

    New-Item -Path "C:\Program Files\SplunkUniversalForwarder\etc\system\local" -Name distsearch.conf -type "file" -value ""

    Add-Content -Path "C:\Program Files\SplunkUniversalForwarder\etc\system\local\distsearch.conf" -Value "[tokenExchKeys]"

    Add-Content -Path "C:\Program Files\SplunkUniversalForwarder\etc\system\local\distsearch.conf" -Value "genKeyScript = C:\Program Files\SplunkUniversalForwarder\bin\splunk, createssl, audit-keys, 3072"

    Write-Host "File doesn't exist, creating file, and adding content"

}

else

{

    Add-Content -Path "C:\Program Files\SplunkUniversalForwarder\etc\system\local\distsearch.conf" -Value ""

    Add-Content -Path "C:\Program Files\SplunkUniversalForwarder\etc\system\local\distsearch.conf" -Value "[tokenExchKeys]"

    Add-Content -Path "C:\Program Files\SplunkUniversalForwarder\etc\system\local\distsearch.conf" -Value "genKeyScript = C:\Program Files\SplunkUniversalForwarder\bin\splunk, createssl, audit-keys, 3072"

    Write-Host "File already exists and new text content added"

}

 

# Restart Splunk service

 

Restart-Service -Name SplunkForwarder
