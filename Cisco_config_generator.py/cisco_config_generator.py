import ipaddress


# ============================================================
# CISCO CONFIGURATION GENERATOR v1.0
# ============================================================


def get_valid_ip(prompt):
    """Ask for a valid IPv4 address."""

    while True:
        ip = input(prompt).strip()

        try:
            ipaddress.IPv4Address(ip)
            return ip

        except ValueError:
            print("Invalid IPv4 address. Please try again.")


def get_valid_mask(prompt):
    """Ask for a valid IPv4 subnet mask."""

    while True:
        mask = input(prompt).strip()

        try:
            # Convert subnet mask to IPv4 network
            ipaddress.IPv4Network(
                f"0.0.0.0/{mask}"
            )

            return mask

        except ValueError:
            print("Invalid subnet mask. Please try again.")


def generate_hostname(hostname):
    """Generate Cisco hostname configuration."""

    return f"hostname {hostname}"


def generate_interface_config(interface, ip, mask):
    """Generate Cisco interface configuration."""

    config = f"""
interface {interface}
 ip address {ip} {mask}
 no shutdown
 exit
"""

    return config.strip()


def generate_static_route(network, mask, next_hop):
    """Generate Cisco static route."""

    return (
        f"ip route {network} {mask} {next_hop}"
    )


def generate_config():
    """Generate complete Cisco configuration."""

    print("\n" + "=" * 55)
    print("        CISCO CONFIGURATION GENERATOR v1.0")
    print("=" * 55)

    # --------------------------------------------------------
    # Router hostname
    # --------------------------------------------------------

    hostname = input(
        "\nEnter router hostname: "
    ).strip()

    if not hostname:
        print("Hostname cannot be empty.")
        return

    config = []

    config.append("!")
    config.append(generate_hostname(hostname))
    config.append("!")

    # --------------------------------------------------------
    # Interfaces
    # --------------------------------------------------------

    try:
        number_of_interfaces = int(
            input(
                "\nHow many interfaces do you want to configure? "
            ).strip()
        )

        if number_of_interfaces < 1:
            print("You must configure at least one interface.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    for number in range(1, number_of_interfaces + 1):

        print(f"\n--- Interface {number} ---")

        interface = input(
            "Enter interface name "
            "(e.g. GigabitEthernet0/0): "
        ).strip()

        if not interface:
            print("Interface name cannot be empty.")
            return

        ip = get_valid_ip(
            "Enter IP address: "
        )

        mask = get_valid_mask(
            "Enter subnet mask: "
        )

        interface_config = generate_interface_config(
            interface,
            ip,
            mask
        )

        config.append(interface_config)
        config.append("!")

    # --------------------------------------------------------
    # Static Routes
    # --------------------------------------------------------

    add_routes = input(
        "\nDo you want to add static routes? (y/n): "
    ).strip().lower()

    if add_routes == "y":

        try:
            number_of_routes = int(
                input(
                    "How many static routes? "
                ).strip()
            )

            if number_of_routes < 1:
                print("No routes added.")

            else:

                for number in range(
                    1,
                    number_of_routes + 1
                ):

                    print(f"\n--- Static Route {number} ---")

                    network = get_valid_ip(
                        "Destination network: "
                    )

                    mask = get_valid_mask(
                        "Destination subnet mask: "
                    )

                    next_hop = get_valid_ip(
                        "Next-hop IP address: "
                    )

                    route = generate_static_route(
                        network,
                        mask,
                        next_hop
                    )

                    config.append(route)
                    config.append("!")

        except ValueError:
            print("Invalid number of routes.")

    # --------------------------------------------------------
    # Final configuration
    # --------------------------------------------------------

    final_config = "\n".join(config)

    print("\n")
    print("=" * 55)
    print("          GENERATED CISCO CONFIGURATION")
    print("=" * 55)

    print(final_config)

    print("=" * 55)

    # --------------------------------------------------------
    # Save configuration
    # --------------------------------------------------------

    save = input(
        "\nSave configuration to a file? (y/n): "
    ).strip().lower()

    if save == "y":

        filename = f"{hostname}_config.txt"

        try:

            with open(
                filename,
                "w",
                encoding="utf-8"
            ) as file:

                file.write(final_config)

            print(
                f"\nConfiguration saved successfully as: "
                f"{filename}"
            )

        except OSError as e:

            print(
                f"Could not save configuration: {e}"
            )


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    while True:

        print("\n")
        print("=" * 55)
        print("        CISCO CONFIGURATION GENERATOR")
        print("=" * 55)

        print("1. Generate Cisco Configuration")
        print("2. Exit")

        print("=" * 55)

        choice = input(
            "Choose an option (1-2): "
        ).strip()

        if choice == "1":

            generate_config()

        elif choice == "2":

            print(
                "\nThank you for using "
                "Cisco Configuration Generator!"
            )

            break

        else:

            print(
                "\nInvalid choice. Please select 1 or 2."
            )


# ============================================================
# START PROGRAM
# ============================================================

if __name__ == "__main__":
    main()
