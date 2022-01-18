# item_drop_watcher

Python program designed to monitor the avaliability of products at select retailers online stores. The program was designed with Ubuntu Linux systems in mind, but with a few tweaks may be compatible with your OS!

## Getting Started
### Installation

1. Install Python3
2. Make sure to have pip installed
  2.1. `python3 -m pip install --user --upgrade pip`
3. Install Python virtual environment
  3.1 `pip install --user virtualenv`

### Running Program

1. Provide the bash script with executable permissions
  1.1. `chmod +x start.sh`
2. Start the program
  2.1 `./start.sh`

Once the script starts it will do the rest of the setting up process. This includes creating and starting virtual environment, installing required dependencies, and starting main python script.

## Other Notes
### Browser Drivers

By defualt the programs utilizes Firefox's  geckodriver and repository includes a 32 and 64 bit version that the program will automatically choose from. However, these may not be the correct driver for your system. A possible solution is to download Firefox onto your system and copying the driver included in the download into the root of the application.
