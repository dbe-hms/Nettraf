#!/bin/bash

sudo ip link set dev eth0 nomaster
sudo ip link set dev eth1 nomaster

echo "Interfaces eth0 and eth1 removed from any bridge."

sudo ip link set dev br0 down
sudo ip link delete br0 type bridge

echo "Bridge br0 deleted."