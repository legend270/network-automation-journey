import ipaddress


def calculate(ip_str, hosts_needed):
    # Find the smallest number of host bits that fits the required hosts
    # usable hosts = 2^h - 2 (network and broadcast addresses are reserved)
    host_bits = 2
    while (2 ** host_bits) - 2 < hosts_needed:
        host_bits += 1

    prefix = 32 - host_bits
    if prefix < 1:
        raise ValueError("Too many hosts requested for an IPv4 subnet.")

    # strict=False lets you enter any IP inside the subnet (e.g. 10.0.0.5)
    network = ipaddress.ip_network(f"{ip_str}/{prefix}", strict=False)

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


def main():
    print("======================================")
    print("=== IPv4 Subnet Calculator ===")
    print("======================================")
    while True:
        try:
            ip_str = input("\nEnter IP address (e.g. 10.0.0.0): ").strip()
            ipaddress.IPv4Address(ip_str)
            hosts = int(input("Enter number of hosts needed: ").strip())
            if hosts < 1:
                raise ValueError("Number of hosts must be at least 1.")

            result = calculate(ip_str, hosts)

            print("\n--- Result ---")
            for key, value in result.items():
                print(f"{key:<24}: {value}")

        except ValueError as e:
            print(f"Invalid input: {e}")
            continue


        again = input("\nCalculate another? (y/n): ").strip().lower()
        if again != "y":
            break


if __name__ == "__main__":
    main()
    