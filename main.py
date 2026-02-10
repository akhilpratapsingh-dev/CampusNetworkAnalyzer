# Campus Network Analyzer
# This program simulates basic network analysis for a campus
# Modules:
# 1. IP & Subnet Validator
# 2. Device Connectivity Checker
# 3. Security Rule Engine
# 4. Innovation: Duplicate IP Detection

# Module 1: IP & Subnet Validator


# Given IP address and subnet mask
ip_address = "192.168.10.25"
subnet_mask = "255.255.255.0"

print("IP Address:", ip_address)
print("Subnet Mask:", subnet_mask)

# Check Private or Public
# Private IP ranges:
# 10.x.x.x
# 172.16.x.x to 172.31.x.x
# 192.168.x.x

if ip_address.startswith("10.") or ip_address.startswith("192.168."):
    ip_type = "Private"
elif ip_address.startswith("172."):
    second_octet = int(ip_address.split(".")[1])
    if 16 <= second_octet <= 31:
        ip_type = "Private"
    else:
        ip_type = "Public"
else:
    ip_type = "Public"

print("IP Type:", ip_type)

# Network ID and Broadcast
# Assumption: subnet mask is 255.255.255.0

ip_parts = ip_address.split(".")

network_id = ip_parts[0] + "." + ip_parts[1] + "." + ip_parts[2] + ".0"
broadcast_address = ip_parts[0] + "." + ip_parts[1] + "." + ip_parts[2] + ".255"

print("Network ID:", network_id)
print("Broadcast Address:", broadcast_address)

# Total Usable Hosts 
# For 255.255.255.0 → 256 total addresses
# Network + Broadcast are not usable

total_usable_hosts = 256 - 2
print("Total Usable Hosts:", total_usable_hosts)

# Module 2: Device Connectivity Checker

print("Device Connectivity Check:")

# Device details (simple variables)
device1_name = "PC1"
device1_vlan = 10

device2_name = "PC2"
device2_vlan = 10

device3_name = "Server1"
device3_vlan = 30

# Assume inter-VLAN routing is disabled
inter_vlan_routing = False

# Check PC1 and PC2
if device1_vlan == device2_vlan:
    print(device1_name, "→", device2_name, ": ACCESS GRANTED (Same VLAN)")
else:
    print(device1_name, "→", device2_name, ": ACCESS DENIED (Different VLANs)")

# Check PC1 and Server1
if device1_vlan == device3_vlan:
    print(device1_name, "→", device3_name, ": ACCESS GRANTED (Same VLAN)")
else:
    if inter_vlan_routing == True:
        print(device1_name, "→", device3_name, ": ACCESS GRANTED (Routing Enabled)")
    else:
        print(device1_name, "→", device3_name, ": ACCESS DENIED (Different VLANs)")

print("\n-------------------------------\n")


# Module 3: Security Rule Engine

print("Security Rule Check:")

# Security rule settings
blocked_ip = "192.168.10.99"

# Using PC1 and Server1 from previous module
pc1_ip = "192.168.10.2"
pc1_vlan = 10

server_ip = "192.168.30.2"
server_vlan = 30

# Rule 1: Check blocked IP
if pc1_ip == blocked_ip:
    print("ACCESS DENIED: PC1 is using a blocked IP address")

# Rule 2: VLAN restriction
elif pc1_vlan == 10 and server_vlan == 30:
    print("ACCESS DENIED: VLAN 10 cannot access VLAN 30")

# If no rule is broken
else:
    print("ACCESS GRANTED: No security rule violated")

print("\n-------------------------------\n")

# Module 4: Innovation Feature
# Duplicate IP Detection

print("Innovation Feature: Duplicate IP Detection")

# IP addresses of devices
ip1 = "192.168.10.2"   # PC1
ip2 = "192.168.10.3"   # PC2
ip3 = "192.168.10.2"   # PC3 (duplicate)

# Check for duplicate IPs
if ip1 == ip2 or ip1 == ip3 or ip2 == ip3:
    print("WARNING: Duplicate IP detected")
    print("Conflicting IP Address:", ip1)
else:
    print("No duplicate IPs found")

print("\n-------------------------------\n")
