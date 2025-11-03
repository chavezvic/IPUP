#Network Device Inventory

# Step 1: Create an empty dictionary to store the inventory
inventory = {}

# Step 2: Function to add a new device
def add_device():
    hostname = input("Enter hostname: ")
    ip_address = input("Enter IP address: ")
    device_type = input("Enter device type (Router/Switch/Firewall): ")

    inventory[hostname] = {
        "ip_address": ip_address,
        "device_type": device_type
    }
    print(f"Device '{hostname}' added successfully!\n")

# Step 3: Function to retrieve device details
def retrieve_device():
    hostname = input("Enter hostname to retrieve: ")
    if hostname in inventory:
        device = inventory[hostname]
        print(f"\nHostname: {hostname}")
        print(f"IP Address: {device['ip_address']}")
        print(f"Device Type: {device['device_type']}\n")
    else:
        print("Device not found in inventory.\n")

# Step 4: Function to display all devices
def display_devices():
    if not inventory:
        print("No devices in inventory.\n")
    else:
        print("\nNetwork Device Inventory:")
        for hostname, details in inventory.items():
            print(f"Hostname: {hostname}")
            print(f"  IP Address: {details['ip_address']}")
            print(f"  Device Type: {details['device_type']}\n")

# Step 5: Main program loop
def main():
    while True:
        print("Network Device Inventory System")
        print("1. Add Device")
        print("2. Retrieve Device Details")
        print("3. Display All Devices")
        print("4. Exit")
        choice = input("Select an option (1-4): ")

        if choice == "1":
            add_device()
        elif choice == "2":
            retrieve_device()
        elif choice == "3":
            display_devices()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
