# Network sim 

>Scripts and tools for Simulating network traffic and issues
>These project is intended to run on a Raspberry pi with two networks adapters.  Bridging them then causing faults,  slowing traffic,  dropping packets, causing jitter.  


## ✨ Features

-   
-   

# 🚀 Getting Started

# Install necessary tools
sudo apt update

sudo apt install -y bridge-utils


### Prerequisites
Python

##Hardware
This setup requires a second Ethernet port connected via USB 


### SETUP
Clone git repo
This is designed to run on a raspberrypi with an additional USB Ethernet adapter.  

./setup_bridge.sh Will setup a bridge betwen eth0 and eth1

./remove_bridge.sh Will remove the bridge

./cycle_issues.py Will cycle through random issues causing data an assortment of delays, loss and disconnections between the two ports. 

./Uinput_issues.py Is intended to be run via terminal with the user picking the operating mode

### AUTO run setup
In the terminal run **sudo crontab -e**  this will open a text editor to setup cron jobs.   Update the following line to directory to location repo was created and enter and add the text to the bottom of the File that opens.  

    @reboot / home/pi/Nettraf/setup_bridge.sh >>/home/pi/Nettraf/log.log 2>&1            
    @reboot /usr/bin/python3 / home/pi/Nettraf/cycle_issues.py

