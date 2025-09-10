#!/usr/bin/env python3
import os, time, random, sys, signal



iface = "br0"
target_ip = "192.168.232.100"
run_time = 50  # seconds

conditions = [
    "netem loss 40%",
    "netem delay 700ms 50ms",
    "tbf rate 2mbit burst 32kbit latency 400ms",
    "netem loss 10% delay 200ms",
    "netem loss 50% 90%",
]


# Handle Ctrl-C to cleanup to avoid leaving tc configs

def cleanup(iface):
    print("\nCaught Ctrl-C! Running cleanup...")
    # Example: clear any tc rules
    os.system(f"sudo tc qdisc del dev {iface} root")
    #os.system(f"sudo tc qdisc del dev {iface} root 2>/dev/null")
    sys.exit(0)



try:
    while True:
        
        #cond = random.choice(conditions)
        for cond in conditions:
            print(f"Applying: {cond}")
            os.system(f"sudo tc qdisc replace dev {iface} root {cond}")
            os.system(f"sudo tc qdisc show dev {iface} root ")
            time.sleep(run_time)


        # Optional: clear before next run
        #os.system(f"sudo tc qdisc del dev {iface} root")
except KeyboardInterrupt:
    cleanup(iface)
