#!/bin/sh

#this script will pass an argument to the kismet server to select the channel used on our card

echo "shell script selected channel: $1"
sudo sh -c "echo 'source=wlan0,channel=$1' > ../kismet_site_2.conf"

return 0