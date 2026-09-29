import ipaddress

# ============================================================

# NETWORK CALCULATOR

# ============================================================

def calculate(ip_str, hosts_needed):

    """Calculate subnet information based on required hosts."""

    # Find the number of host bits required

    host_bits = 2

    while (2 ** host_bits) - 2 < hosts_needed:

        host_bits += 1

    prefix = 32 - host_bits

    if prefix < 1:

        raise ValueError("Too many hosts requested for an IPv4 subnet.")

    network = ipaddress.ip_network(

        f"{ip_str}/{prefix}",

        strict=False

    )

    first_host = network.network_address + 1

    last_host = network.broadcast_address - 1
    
    return {

        "Network Address": network.network_address,

        "Subnet Mask": network.netmask,

        "CIDR": f"/{prefix}",

        "Wildcard Mask": network.hostmask,

        "First Host": first_host,

        "Last Host": last_host,

        "Broadcast Address": network.broadcast_address,

        "Total Addresses": network.num_addresses,

        "Usable Hosts": network.num_addresses - 2,

        "Next Network Starts At": network.broadcast_address + 1,

    }

# ============================================================

# OPTION 1 - SUBNET INFORMATION

# ============================================================

def subnet_information():

    """Calculate complete subnet information."""

    try:

        ip_str = input(

            "\nEnter IP address (e.g. 192.168.1.0): "

        ).strip()

        ipaddress.IPv4Address(ip_str)

        hosts = int(

            input("Enter number of hosts needed: ").strip()

        )

        if hosts < 1:

            raise ValueError(

                "Number of hosts must be at least 1."

            )

        result = calculate(ip_str, hosts)

        print("\n--- Subnet Information ---")

        for key, value in result.items():
            print(f"{key:<28}: {value}")
            
    except ValueError as e:
        print(f"Invalid input: {e}")

# ============================================================

# OPTION 2 - CALCULATE HOSTS

# ============================================================

def calculate_host():

    """Calculate total and usable hosts from CIDR prefix."""

    text = input(

        "\nEnter prefix length (e.g. 24 or /24): "

    ).strip().lstrip("/")

    if not text.isdigit():

        print("Invalid input: please enter a whole number.")

        return

    prefix = int(text)

    if prefix < 0 or prefix > 32:

        print(

            "Invalid input: prefix length must be between 0 and 32."

        )

        return

    host_bits = 32 - prefix

    total = 2 ** host_bits

    # Special cases

    if prefix == 32:

        usable = 1

    elif prefix == 31:

        usable = 2

    else:

        usable = total - 2

    mask = ipaddress.ip_network(

        f"0.0.0.0/{prefix}"
        ).netmask

    print("\n--- Host Calculation ---")

    print(f"{'Prefix Length':<28}: /{prefix}")

    print(f"{'Subnet Mask':<28}: {mask}")

    print(f"{'Host Bits':<28}: {host_bits}")

    print(f"{'Total Addresses':<28}: {total}")

    print(f"{'Usable Hosts':<28}: {usable}")

# ============================================================

# OPTION 3 - LIST USABLE HOSTS

# ============================================================

def list_hosts():

    """List all usable host addresses in a network."""

    try:

        network_input = input(

            "\nEnter network (e.g. 192.168.1.0/29): "

        ).strip()

        network = ipaddress.ip_network(

            network_input,

            strict=False

        )

        print("\n--- Network Information ---")

        print(f"Network Address : {network.network_address}")

        print(f"Broadcast       : {network.broadcast_address}")

        print(f"Subnet Mask     : {network.netmask}")

        print(f"Total Addresses : {network.num_addresses}")

        # /31 and /32 need special handling

        if network.prefixlen == 32:

            hosts = [network.network_address]

        elif network.prefixlen == 31:

            hosts = list(network.hosts())

        else:

            hosts = list(network.hosts())

        print("\n--- Usable Hosts ---")

        for number, host in enumerate(hosts, start=1):

            print(f"Host {number}: {host}")

        print(f"\nTotal usable hosts: {len(hosts)}")

    except ValueError as e:

        print(f"Invalid network: {e}")
        # ============================================================

# OPTION 4 - CHECK IP MEMBERSHIP

# ============================================================

def check_ip():

    """Check whether an IP address belongs to a network."""

    try:

        ip_str = input(

            "\nEnter IP address: "

        ).strip()

        network_str = input(

            "Enter network (e.g. 192.168.1.0/24): "

        ).strip()

        ip = ipaddress.ip_address(ip_str)

        network = ipaddress.ip_network(

            network_str,

            strict=False

        )

        print("\n--- IP Membership Check ---")

        print(f"IP Address : {ip}")

        print(f"Network    : {network}")

        if ip in network:

            print(f"Result     : {ip} belongs to {network}")

        else:

            print(

                f"Result     : {ip} does NOT belong to {network}"

            )

    except ValueError as e:

        print(f"Invalid input: {e}")
        
        # ============================================================

# MAIN MENU

# ============================================================

def main():

    while True:

        print("\n")

        print("=" * 45)

        print("          NETWORK TOOL v2.0")

        print("=" * 45)

        print("1. Subnet Information")

        print("2. Calculate Hosts")

        print("3. List Usable Hosts")

        print("4. Check IP Belongs to Network")

        print("5. Exit")

        print("=" * 45)

        choice = input(

            "Choose an option (1-5): "

        ).strip()

        if choice == "1":

            subnet_information()

        elif choice == "2":

            calculate_host()

        elif choice == "3":

            list_hosts()

        elif choice == "4":

            check_ip()

        elif choice == "5":

            print("\nThank you for using Network Tool v2.0!")

            print("Goodbye!")

            break

        else:

            print(

                "\nInvalid choice. Please enter 1, 2, 3, 4 or 5."

            )
            
            # ============================================================

# START PROGRAM

# ============================================================

if __name__ == "__main__":

    main()