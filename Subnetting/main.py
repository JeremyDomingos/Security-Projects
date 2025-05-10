"""
   This program takes an IP Address, Subnet Mask and CIDR Class
   and will provide information on the number of hosts, subnets and both 
   Network and Broadcast address
"""
import sys
import math

classful_ranges = {
    "A":"0.0.0.0", # uNTIL 127.255.255.255
    "B":"128.0.0.0", # uNTIL 191.255.255.255
    "C":"192.0.0.0", # 223.255.255.255
    "D":"224.0.0.0", # 239.255.255.255
    "E":"240.0.0.0", # 255.255.255.255
}

CIDR_NOTATION = "\0"

def main():

    print("Welcome\n------------------------\nUsage:[IP][Mask][CIDR CLASS]")
# Get user input from command line
# Requires sys module for sys.argv[]
    if len(sys.argv) < 1:
        print("Invalid arguments")
        print("Welcome\n------------------------\nUsage:[IP][Mask][CIDR CLASS]")
        return
    else:
        IP_Add = sys.argv[1]
        Sub_Mask = sys.argv[2]
        Class = sys.argv[3]

    # Input as strings only
    # Validate CIDR Class
    
    if Class > "E":
        print("Invalid Class")
    # Validate Subnet Mask

    
    print(number_hosts(Sub_Mask))

def binary(decimal):
    binary = ""
    reminder = 0
    # Verfiy as a intger
    # Convert from decimal to binary

    if decimal == 0:
        return "00000000"
    try:
        while decimal > 0:#   Until decimal is => 0
            reminder = decimal % 2
            #  Modulo the number and record answer
            binary = str(reminder) + binary
            #  Divide number by 2
            decimal = decimal // 2
        # Return binary format to user
        # Check for input == 0

        return binary

    except ValueError:
        print("Invalid Input")
        return 
    

def number_hosts(Mask):
    mask_str= Mask.split(".")
    mask_byte = []

    for byte in mask_str:
        mask_byte.append(binary(int(byte)))

    mask_byte = ".".join(mask_byte)
    # network portion

    print(mask_byte)
    zeros = 0
    ones = 0
    
    for i in range(0,len(mask_byte) - 1):
        if mask_byte[i] == 0:
            zeros = zeros + 1
        else:
            ones = ones + 1

    network_portion = ones

    CIDR_NOTATION = str(network_portion)
    # host portion 
    host_portion = zeros

    print(host_portion)
    number_hosts = 2 ** (host_portion)

    return "Number of Hosts:" + str((number_hosts - 2))

    
    
# Find Number of Hosts
    # convert IP address to binary inorder to find the number of zeros and ones
# Find the CIDR Class
    # Number of ones = subnet mask
    # (2 ^ (32 - number of ones)) - 2 = number of hosts


# Find Number of Subnets
    # 2^ (subnet mask - provide CIDR Mask) = number of subnets


main()