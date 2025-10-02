#!/usr/bin/env python3
import os, time, random, sys, signal



#iface = "br0"
iface = "eth1"
target_ip = "192.168.232.100"
run_time = 50  # seconds

conditions = [
    "netem loss 20% 90%",
    "netem delay 700ms 50ms",
    "tbf rate 2mbit burst 32kbit latency 400ms",
    "netem loss 10% delay 200ms",
    "netem loss 40% 50%",
    "netem delay 1000ms 100ms",
    "netem duplicate 30%",
    "netem corrupt 10%",
    "netem delay 300ms 100ms loss 10%",
    "netem delay 500ms 200ms loss 20% duplicate 10%",
]
conditions_set_2 = [
    
    "netem duplicate 10%",
    "netem corrupt 10%",
    "netem delay 500ms 200ms loss 20% duplicate 10%",
    "netem delay 1000ms 100ms",
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
        for cond in conditions_set_2:
            print(f"Applying: {cond}")
            os.system(f"sudo tc qdisc replace dev {iface} root {cond}")
            os.system(f"sudo tc qdisc show dev {iface} root ")
            time.sleep(run_time)


        # Optional: clear before next run
        os.system(f"sudo tc qdisc del dev {iface} root")
except KeyboardInterrupt:
    cleanup(iface)
