# Type2Color

Type2Color is a Python application that interfaces with an LED strip and allows you to change the color of a randomly selected LED by pressing keys on an input device (keyboard, buttons, etc.). The project also includes files to set up a systemd service to run the application at startup.

## Dependencies

Before running the Type2Color application, make sure you have the following components installed:

- Python 3
- [rpi_ws281x](https://github.com/rpi-ws281x/rpi-ws281x-python) library for controlling the LED strip
- [evdev](https://python-evdev.readthedocs.io/) library for interacting with input devices
- A compatible LED strip (number of LEDs and pin configuration as specified in the `type2color.py` file)
- Target platform: Raspberry Pi
- [evtest](https://gitlab.freedesktop.org/libevdev/evtest) tool to monitor the input device event

## Installation

1. Install the required Python libraries:

```bash
pip install rpi_ws281x evdev
```

2. Install the evtest to get the input id, if necessary:

```bash
dnf install evtest
```

## Usage
### Configure the input id
To read the input event keys is necessary to configure the input device id. For that, use the evtest application:
```bash
sudo evtest
```

And update it on code line:
```bash
dev = InputDevice('/dev/input/event[input id]')
```

### Running the Application

To run the Type2Color application, execute the `type2color.py` script with Python 3:

```bash
python3 type2color.py
```

The application will start, and the LED strip will light up with a random color. Whenever a key is pressed on the input device, a randomly selected LED will change to a new color. The application will log the key pressed, the LED ID, and the RGB values of the new color.

To stop the application, press `Ctrl + C`.

### Setting up systemd Service

The project includes a systemd service file `type2color-startup.service`, which allows you to run the application at system startup.

Follow these steps to set up the systemd service:

1. Copy the `type2color-startup.service` file to the systemd services directory:

```bash
sudo cp type2color-startup.service /etc/systemd/system/
```

2. Reload the systemd manager configuration:

```bash
sudo systemctl daemon-reload
```

3. Enable the `type2color-startup.service` to run at startup:

```bash
sudo systemctl enable type2color-startup.service
```

4. Start the service:

```bash
sudo systemctl start type2color-startup.service
```

Now, the Type2Color application will automatically start whenever your system boots up.

## Customization

Feel free to modify the `type2color.py` script and systemd service file `type2color-startup.service` according to your specific requirements. You can change LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_BRIGHTNESS, and other variables in the `type2color.py` script to adapt it to your LED strip configuration.

## Troubleshooting

If you encounter any issues or errors, you can check the logs using the following command:

```bash
journalctl -u type2color-startup.service
```

This will display the logs related to the Type2Color systemd service and help you diagnose any problems.

---
Feel free to add additional details or instructions if necessary. Ensure that you provide accurate information about the installation steps and other prerequisites required to run the application successfully.
