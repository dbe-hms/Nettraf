# Replace eth0 and eth1 with your two interfaces
ip link add name br0 type bridge
ip link set dev br0 up
echo "Bridge br0 created."
ip link set dev eth0 master br0
ip link set dev eth1 master br0
ip link set dev eth0 up
ip link set dev eth1 up

echo "Interfaces eth0 and eth1 added to bridge br0 and brought up."
echo "Bridge setup complete."