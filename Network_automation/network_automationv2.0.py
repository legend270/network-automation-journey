from datetime import datetime

# ============================================================
# NETWORK AUTOMATION TOOL v2.0
# SIMULATION MODE
# ============================================================


def get_devices():
    """Return the network device inventory."""

    devices = [
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

    return devices


def display_devices(devices):
    """Display all devices in the inventory."""

    print("\n" + "=" * 75)
    print("                 NETWORK DEVICE INVENTORY")
    print("=" * 75)

    print(
        f"{'Name':<12}"
        f"{'Device Type':<22}"
        f"{'IP Address':<20}"
        f"{'Status':<12}"
    )

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

        if device["name"] == "R1":
            return (
                "GigabitEthernet0/0  192.168.10.1  up  up\n"
                "GigabitEthernet0/1  unassigned    down  down"
            )

        elif device["name"] == "S1":
            return (
                "FastEthernet0/1  unassigned  up  up\n"
                "FastEthernet0/2  unassigned  up  up\n"
                "Vlan1            192.168.10.2 up  up"
            )

    elif command == "show ip ssh":
        if device["device_type"] == "Cisco Router":
            return "SSH Enabled - version 2.0"

        return "SSH information not available for this simulated switch."

    elif command == "show version":
        return (
            f"Device: {device['name']}\n"
            f"Type: {device['device_type']}\n"
            "IOS version: Simulated lab output"
        )

    return "No simulated output available for this command."


def collect_results(devices, commands):
    """Collect command results for all devices."""

    results = {}

    for device in devices:

        results[device["name"]] = {
            "ip": device["ip"],
            "device_type": device["device_type"],
            "status": device["status"],
            "commands": {},
        }

        for command in commands:

            output = simulate_command(device, command)

            results[device["name"]]["commands"][command] = output

    return results


def display_results(results):
    """Display collected results."""

    print("\n" + "=" * 75)
    print("                   COMMAND RESULTS")
    print("=" * 75)

    for device_name, details in results.items():

        print(f"\nDevice: {device_name}")
        print(f"IP Address: {details['ip']}")
        print(f"Status: {details['status']}")

        for command, output in details["commands"].items():

            print(f"\nCommand: {command}")
            print("-" * 50)
            print(output)


def generate_report(results):
    """Save results to a text report."""

    filename = "network_report.txt"

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        with open(filename, "w", encoding="utf-8") as file:

            file.write("NETWORK AUTOMATION REPORT v2.0\n")
            file.write("=" * 60 + "\n")
            file.write(f"Generated: {timestamp}\n")
            file.write("Mode: SIMULATION — NOT LIVE DEVICE DATA\n")
            file.write("=" * 60 + "\n")

            for device_name, details in results.items():

                file.write(f"\nDevice: {device_name}\n")
                file.write(f"IP Address: {details['ip']}\n")
                file.write(f"Device Type: {details['device_type']}\n")
                file.write(f"Status: {details['status']}\n")

                for command, output in details["commands"].items():

                    file.write(f"\nCommand: {command}\n")
                    file.write("-" * 50 + "\n")
                    file.write(output + "\n")

                file.write("\n" + "=" * 60 + "\n")

        print(f"\nReport saved successfully: {filename}")

    except OSError as error:
        print(f"\nUnable to save report: {error}")


def main():

    print("\n" + "=" * 75)
    print("              NETWORK AUTOMATION TOOL v2.0")
    print("                       SIMULATION MODE")
    print("=" * 75)

    devices = get_devices()

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
        1 for device in devices
        if device["status"] == "ONLINE"
    )

    offline_count = len(devices) - online_count

    print("\n" + "=" * 75)
    print("                     SUMMARY")
    print("=" * 75)

    print(f"Total devices: {len(devices)}")
    print(f"Online: {online_count}")
    print(f"Offline: {offline_count}")
    print("Mode: Simulation")
    print("=" * 75)


if __name__ == "__main__":
    main()
