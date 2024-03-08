import subprocess

x = input(" ENTER YOUR NETWORK INTERFACE=")
y = input("ENTER YOUR MAC ADDRESS=")
 
# Disable the network interface
subprocess.run(["ifconfig", x, "down"])

# Change the MAC address
subprocess.run(["ifconfig", x, "hw", "ether", y])

# Enable the network interface again
subprocess.run(["ifconfig", x , "up"])

print("MAC address successfully changed")