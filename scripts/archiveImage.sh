#!/bin/bash
#
# Backup latestImage
 
## Get current date ##
_now=$(date +"%m_%d_%Y_%H")
 
## Appending a current date from a $_now to a filename stored in $_file ##
_file="/home/piserver/dev/webgarden/proc/imgArchive/img_$_now.jpg"
 
## Do it ##
echo "Copying latest image to $_file..."
cp /home/piserver/dev/webgarden/proc/LatestImage.jpg "$_file"

echo "Done"