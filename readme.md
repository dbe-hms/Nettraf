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

This is designed to run on a raspberrypi with an additional USB Ethernet adapter.  

./setup_bridge.sh Will setup a bridge betwen eth0 and eth1
./remove_bridge.sh Will remove the bridge
./cycle_issues.py Will cycle through random issues causing data an assortment of delays, loss and disconnections between the two ports. 
./Uinput_issues.py Is intended to be run via terminal with the user picking the operating mode

What things you need to install the software and how to install them.
