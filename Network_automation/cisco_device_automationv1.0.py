# ============================================================
# NETWORK AUTOMATION TOOL v1.0
# ============================================================

def display_device(device):
    """Display information about a network device."""

    print("\n" + "=" * 50)
    print("DEVICE INFORMATION")
    print("=" * 50)

    print(f"Device Name : {device['name']}")
    print(f"Device Type : {device['device_type']}")
    print(f"IP Address  : {device['ip']}")
    print(f"Username    : {device['username']}")

    print("=" * 50)


def simulate_command(device, command):
    """Simulate sending a command to a network device."""

    print("\n" + "-" * 50)
    print(f"Device  : {device['name']}")
    print(f"Command : {command}")
    print("-" * 50)

    if command == "show ip interface brief":
        output = """
Interface              IP-Address      Status       Protocol
GigabitEthernet0/0     192.168.10.1    up           up
GigabitEthernet0/1     unassigned      down         down
GigabitEthernet0/2     unassigned      down         down
Vlan1                  unassigned      down         down
"""

    elif command == "show ip ssh":
        output = """
SSH Enabled - version 2.0
Authentication timeout: 120 secs
Authentication retries: 3
"""

    elif command == "show version":
        output = """
Cisco IOS Software
Router Model: Cisco 2911
Hostname: R1
"""

    else:
        output = "Command output not available in simulation."

    print(output)


def main():

    device = {
        "name": "R1",
        "device_type": "cisco_ios",
        "ip": "192.168.10.1",
        "username": "admin"
    }

    display_device(device)

    commands = [
        "show ip interface brief",
        "show ip ssh",
        "show version"
    ]

    for command in commands:
        simulate_command(device, command)


if __name__ == "__main__":
    main()