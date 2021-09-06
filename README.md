# Raspberry Pi QRCode Scanner

Raspberry Pi Python based QR Code scanner that will follow a simple webhook to initiate an API action.

# Installation

    sudo apt-get update

    sudo apt-get install python3-opencv

    sudo apt-get install libqt4-test python3-sip python3-pyqt5 libqtgui4 libjasper-dev libatlas-base-dev -y

    pip3 install opencv-contrib-python==4.1.0.25

    sudo modprobe bcm2835-v4l2

# Run

    python3 /path/to/folder/scanner.py

# Start on GUI Boot (Raspberry Pi)

1. Create a .desktop file

    mkdir /home/pi/.config/autostart
    nano /home/pi/.config/autostart/clock.desktop

2. Input the following into the new file (assuming the repo was cloned into the pi home directory)

    [Desktop Entry]
    Type=Application
    Name=Scanner
    Exec=/usr/bin/python3 /home/pi/qrcode-scanner/scanner.py

3. Reboot