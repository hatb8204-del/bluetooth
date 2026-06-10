import os

print("📡 Bluetooth Scanner Tool (Educational)")

print("\nScanning nearby devices...\n")

# Try real scan (Linux support)
try:
    result = os.popen("hcitool scan").read()
    if result.strip() == "":
        print("No devices found OR Bluetooth not supported on this device.")
    else:
        print(result)

except Exception as e:
    print("Error:", e)

print("\nScan finished.")
