from datetime import datetime
from ipaddress import ip_address


# ============================================================
# NETWORK AUTOMATION TOOL v3.0
# SIMULATION MODE
# ============================================================


def get_devices():
    """Return the network device inventory."""

    return [
        {
            "name": "R1",
            "device_type": "Cisco Router",
            "ip": "192.168.10.1",
            "status": "ONLINE",
        },
        {
            "name": "S1",
            "device_type": "Cisco Switch",
            "ip": "192.168.10.2",
            "status": "ONLINE",
        },
        {
            "name": "R2",
            "device_type": "Cisco Router",
            "ip": "192.168.20.1",
            "status": "ONLINE",
        },
        {
            "name": "R3",
            "device_type": "Cisco Router",
            "ip": "192.168.30.1",
            "status": "ONLINE",
        },
    ]


def validate_devices(devices):
    """Validate required fields, names, IP addresses, and statuses."""

    required_fields = {"name", "device_type", "ip", "status"}
    seen_names = set()

    for index, device in enumerate(devices, start=1):
        if not isinstance(device, dict):
            raise ValueError(f"Device #{index} must be a dictionary.")

        missing_fields = required_fields - device.keys()
        if missing_fields:
            raise ValueError(
                f"Device #{index} is missing fields: "
                f"{', '.join(sorted(missing_fields))}"
            )

        name = device["name"]
        if not isinstance(name, str) or not name.strip():
            raise ValueError(f"Device #{index} has an invalid name.")

        if name in seen_names:
            raise ValueError(f"Duplicate device name: {name}")
        seen_names.add(name)

        device_type = device["device_type"]
        if not isinstance(device_type, str) or not device_type.strip():
            raise ValueError(f"{name} has an invalid device type.")

        try:
            address = ip_address(device["ip"])
        except (ValueError, TypeError):
            raise ValueError(
                f"{name} has an invalid IP address: {device['ip']}"
            ) from None

        if address.version != 4:
            raise ValueError(f"{name} must use an IPv4 address.")

        if device["status"] not in {"ONLINE", "OFFLINE"}:
            raise ValueError(
                f"{name} has an unsupported status: {device['status']}"
            )


def display_devices(devices):
    """Display all devices in the inventory."""

    print("\n" + "=" * 75)
    print("                 NETWORK DEVICE INVENTORY")
    print("=" * 75)
    print(f"{'Name':<12}{'Device Type':<22}{'IP Address':<20}{'Status':<12}")
    print("-" * 75)

    for device in devices:
        print(
            f"{device['name']:<12}"
            f"{device['device_type']:<22}"
            f"{device['ip']:<20}"
            f"{device['status']:<12}"
        )

    print("=" * 75)


def simulate_command(device, command):
    """Return simulated output for supported commands."""

    if device["status"] != "ONLINE":
        return "ERROR: Device is marked OFFLINE in simulation."

    if command == "show ip interface brief":
        interface_outputs = {
            "R1": (
                "GigabitEthernet0/0  192.168.10.1  up  up\n"
                "GigabitEthernet0/1  unassigned    down  down"
            ),
            "S1": (
                "FastEthernet0/1  unassigned   up  up\n"
                "FastEthernet0/2  unassigned   up  up\n"
                "Vlan1            192.168.10.2  up  up"
            ),
            "R2": (
                "GigabitEthernet0/0  192.168.20.1  up  up\n"
                "GigabitEthernet0/1  unassigned    down  down"
            ),
            "R3": (
                "GigabitEthernet0/0  192.168.30.1  up  up\n"
                "GigabitEthernet0/1  unassigned    down  down"
            ),
        }
        return interface_outputs.get(
            device["name"], "No simulated interface data for this device."
        )

    if command == "show ip ssh":
        if device["device_type"] == "Cisco Router":
            return "SSH Enabled - version 2.0 (simulated)"
        return "SSH information not available for this simulated switch."

    if command == "show version":
        return (
            f"Device: {device['name']}\n"
            f"Type: {device['device_type']}\n"
            "IOS version: Simulated lab output"
        )

    return "No simulated output available for this command."


def collect_results(devices, commands):
    """Collect simulated command results for all devices."""

    results = {}

    for device in devices:
        results[device["name"]] = {
            "ip": device["ip"],
            "device_type": device["device_type"],
            "status": device["status"],
            "commands": {},
        }

        for command in commands:
            results[device["name"]]["commands"][command] = simulate_command(
                device, command
            )

    return results


def display_results(results):
    """Display collected simulated results."""

    print("\n" + "=" * 75)
    print("                   COMMAND RESULTS (SIMULATION)")
    print("=" * 75)

    for device_name, details in results.items():
        print(f"\nDevice: {device_name}")
        print(f"IP Address: {details['ip']}")
        print(f"Device Type: {details['device_type']}")
        print(f"Status: {details['status']}")

        for command, output in details["commands"].items():
            print(f"\nCommand: {command}")
            print("-" * 50)
            print(output)


def generate_report(results):
    """Save results to a timestamped text report."""

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = "network_report.txt"

    try:
        with open(filename, "w", encoding="utf-8") as report:
            report.write("NETWORK AUTOMATION REPORT v3.0\n")
            report.write("=" * 60 + "\n")
            report.write(f"Generated: {timestamp}\n")
            report.write("Mode: SIMULATION — NOT LIVE DEVICE DATA\n")
            report.write("=" * 60 + "\n")

            for device_name, details in results.items():
                report.write(f"\nDevice: {device_name}\n")
                report.write(f"IP Address: {details['ip']}\n")
                report.write(f"Device Type: {details['device_type']}\n")
                report.write(f"Status: {details['status']}\n")

                for command, output in details["commands"].items():
                    report.write(f"\nCommand: {command}\n")
                    report.write("-" * 50 + "\n")
                    report.write(output + "\n")

                report.write("\n" + "=" * 60 + "\n")

        print(f"\nReport saved successfully: {filename}")
        return True

    except OSError as error:
        print(f"\nUnable to save report: {error}")
        return False


def main():
    print("\n" + "=" * 75)
    print("              NETWORK AUTOMATION TOOL v3.0")
    print("                       SIMULATION MODE")
    print("=" * 75)

    devices = get_devices()

    try:
        validate_devices(devices)
    except ValueError as error:
        print(f"Inventory validation failed: {error}")
        return

    commands = [
        "show ip interface brief",
        "show ip ssh",
        "show version",
    ]

    display_devices(devices)
    results = collect_results(devices, commands)
    display_results(results)
    generate_report(results)

    online_count = sum(
        1 for device in devices if device["status"] == "ONLINE"
    )
    offline_count = len(devices) - online_count

    print("\n" + "=" * 75)
    print("                     SUMMARY")
    print("=" * 75)
    print(f"Total devices: {len(devices)}")
    print(f"Online: {online_count}")
    print(f"Offline: {offline_count}")
    print("Mode: Simulation — no live devices were contacted")
    print("=" * 75)


if __name__ == "__main__":
    main()
