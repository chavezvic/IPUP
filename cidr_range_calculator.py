#Subner masks and their ranges
#/8  -> 16,777,216 IPs (Example: 10.0.0.0 - 10.255.255.255)
#/16 -> 65,536 IPs    (Example: 192.168.0.0 - 192.168.255.255)
#/24 -> 256 IPs       (Example: 192.168.1.0 - 192.168.1.255)


def main():
    print("CIDR Range Calculator")
    print("Supported masks: /8, /16, /24\n")

    # Get user input
    ip_address = input("Enter an IP address (e.g., 192.168.1.1): ")
    mask = input("Select a mask from /8, /16, /24: ")

    # Validate mask
    if mask not in ["/8", "/16", "/24"]:
        print("Invalid mask. Please restart and select a valid option.")
        return

    # Call function to calculate range
    network_range = calculate_range(ip_address, mask)
    if network_range:
        print(f"\nNetwork range for {ip_address}{mask}:")
        print(network_range)


def calculate_range(ip, mask):
    """Calculates the network range for a given IP and mask."""

    # Split the IP into octets
    octets = ip.split(".")
    if len(octets) != 4:
        print("Invalid IP address format. Please restart.")
        return None

    # Convert octets to integers
    try:
        converted_octets = []
        for o in octets:
            try:
                converted_octets.append(int(o))
            except ValueError:
                print("IP address must contain only numbers. Please restart.")
                return None
        octets = converted_octets
    except ValueError:
        print("IP address must contain only numbers. Please restart.")
        return None

    # Validate octet range
    for o in octets:
        if o < 0 or o > 255:
            print("IP address octets must be between 0 and 255. Please restart.")
            return None

    # Calculate range based on mask
    if mask == "/8":
        network_start = f"{octets[0]}.0.0.0"
        network_end = f"{octets[0]}.255.255.255"
    elif mask == "/16":
        network_start = f"{octets[0]}.{octets[1]}.0.0"
        network_end = f"{octets[0]}.{octets[1]}.255.255"
    elif mask == "/24":
        network_start = f"{octets[0]}.{octets[1]}.{octets[2]}.0"
        network_end = f"{octets[0]}.{octets[1]}.{octets[2]}.255"
    else:
        print("Unsupported mask. Please restart.")
        return None

    return f"{network_start} - {network_end}"

if __name__ == "__main__":
    main()
