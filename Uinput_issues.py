#!/usr/bin/env python3
import os, sys, signal, random, time, select

iface = "eth1"

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

# Global cleanup for quitting script entirely
def cleanup(sig=None, frame=None):
    print("\nCleaning up...")
    os.system(f"sudo tc qdisc del dev {iface} root")
    sys.exit(0)

signal.signal(signal.SIGINT, cleanup)

def show_menu():
    print("\nSelect a condition to apply:")
    for i, cond in enumerate(conditions, start=1):
        print(f"{i}. {cond}")
    print("r. Random condition (auto-cycle)")
    print("0. Clear / No impairment")
    print("q. Quit")

def random_mode(duration):
    print(f"\nRandom cycling every {duration} seconds. Type 'q' + Enter to stop.")

    while True:
        cond = random.choice(conditions)
        print(f"\nApplying random condition: {cond}")
        os.system(f"sudo tc qdisc replace dev {iface} root {cond}")
        os.system(f"sudo tc qdisc show dev {iface} root")

        # Wait up to 'duration' seconds, but allow user input
        for _ in range(duration):
            time.sleep(1)
            if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                user_input = sys.stdin.readline().strip().lower()
                if user_input == "q":
                    print("\nStopped random mode. Clearing and returning to menu...")
                    os.system(f"sudo tc qdisc del dev {iface} root")
                    return


while True:
    show_menu()
    choice = input("Enter choice: ").strip()

    if choice.lower() == "q":
        cleanup()

    if choice == "0":
        print("Clearing conditions...")
        os.system(f"sudo tc qdisc del dev {iface} root")
        continue
    
    if choice.lower() == "r":
        try:
            duration = int(input("How many seconds per random condition? ").strip())
        except ValueError:
            print("Invalid number. Returning to menu.")
            continue
        random_mode(duration)
        continue  # return to main menu after random mode

    if not choice.isdigit() or not (1 <= int(choice) <= len(conditions)):
        print("Invalid choice. Try again.")
        continue

    cond = conditions[int(choice) - 1]
    print(f"Applying: {cond}")
    os.system(f"sudo tc qdisc replace dev {iface} root {cond}")
    os.system(f"sudo tc qdisc show dev {iface} root ")

    print(f"Condition '{cond}' active. It will stay until you choose another option.")
