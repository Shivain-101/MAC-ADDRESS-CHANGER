import subprocess

x = input(" ENTER YOUR NETWORK INTERFACE=")
y = input("ENTER YOUR MAC ADDRESS=")

# Disable the network interface
subprocess.run(["ifconfig", x, "down"])

# Change the MAC address
subprocess.run(["ifconfig", x, "hw", "ether", y])

# Enable the network interface again
subprocess.run(["ifconfig", x , "up"])

if subprocess.run(["ifconfig", x], capture_output=True).stdout:
    print("MAC address successfully changed")
else:
    print("EXIT: Unable to change MAC address. Please check your input or permissions.")
