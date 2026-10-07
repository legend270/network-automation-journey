import subprocess

def check_device(ip):
    
    result =subprocess.run(
        ["ping", "-n", "1", ip],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        return "ONLINE"
    else:
        return "OFFLINE"
    
def monitor_devices(devices):
    online = 0
    offline = 0
    
    print("\n" + "=" * 65)
    print("    NETWORK DEVICE MONITOR v1.0    ")
    print("=" * 65)
    
    print(
        f"{'Device Name':<25}"
        f"{'IP Address':<18}"
        f"{'Status':<10}"
    )
    
    print("=" * 65)
    
    for name, ip in devices.items():
        status = check_device(ip)
        print(f"{name:<25}" 
              f"{ip:<18}" 
              f"{status:<10}"
              )
    
   
    
        if status == "ONLINE":
            online += 1
        else:
            offline += 1
    
    print("-" * 65)

    print(f"Total devices  : {len(devices)}")
    print(f"Online         : {online}")
    print(f"Offline        : {offline}")

    print("=" * 65)


def main():

    devices = {
        "Google DNS": "8.8.8.8",
        "Cloudflare DNS": "1.1.1.1",
        "My Router": "172.20.10.1",
        "Google Secondary DNS": "8.8.4.4",
        "Cloudflare Secondary": "1.0.0.1"
    }
    monitor_devices(devices)
    
    
if __name__ == "__main__":
    main()


    
