import os
import psutil
import subprocess
import time

def find_vlc_on_usb(usb_path):
    # Search for vlc.exe on the USB drive
    for root, dirs, files in os.walk(usb_path):
        if 'vlc.exe' in files:
            return os.path.join(root, 'vlc.exe')
    return None

def check_for_usb():
    # Get a list of connected USB devices
    connected_devices = [device.device for device in psutil.disk_partitions() if 'removable' in device.opts]

    return connected_devices

def run_vlc(file_path, vlc_exe_path):
    # Specify the path to the MP4 file on the USB
    mp4_file_path = os.path.join(file_path, 'your_video.mp4')  # Adjust the filename as needed

    # Check if the MP4 file exists on the USB
    if os.path.exists(mp4_file_path):
        # Run VLC with the specified file using the VLC executable from the USB
        subprocess.run([vlc_exe_path, mp4_file_path])
    else:
        print(f"No MP4 file found on the USB.")

def main():
    while True:
        # Check for connected USB devices
        usb_devices = check_for_usb()

        if usb_devices:
            print("USB device detected!")

            # Run VLC with the MP4 file from each USB device
            for usb_device in usb_devices:
                vlc_exe_path = find_vlc_on_usb(usb_device)
                if vlc_exe_path:
                    run_vlc(usb_device, vlc_exe_path)
                else:
                    print(f"VLC executable not found on the USB device: {usb_device}")

        # Sleep for a while before checking again
        time.sleep(5)

if __name__ == "__main__":
    main()
