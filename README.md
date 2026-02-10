Campus Network Analyzer
About the Project

This project is a simple simulation of a campus network.
It shows how IP addressing, VLANs, and basic security rules work in a network.

The goal of this project is to understand networking concepts, not to build a real router or firewall.

What This Project Does

Checks whether an IP address is private or public

Finds network address and broadcast address

Checks if two devices can communicate using VLAN rules

Applies simple security restrictions

Detects duplicate IP addresses in the network

How the Project Works

The project is divided into four parts:

IP and Subnet Check
The program analyzes a given IP address and subnet mask and prints network details.

Device Connectivity Check
Devices are assigned VLAN numbers.
Devices in the same VLAN can communicate, while devices in different VLANs cannot.

Security Rules
Some communication is blocked based on VLAN rules and blocked IP addresses.

Innovation Feature
The program checks if any two devices are using the same IP address.

Assumptions Made

Subnet mask is fixed as 255.255.255.0

Inter-VLAN routing is disabled

Device details are hardcoded to keep the logic simple

Innovation Feature

Duplicate IP detection is added to identify IP conflicts, which can cause network issues.
