# Config.ini Setup Utility

A simple Python script designed to make configuring your `config.ini` file quick, easy, and user-friendly. This utility scans your existing configuration file, prompts you to fill in missing or placeholder values, and saves the updated configuration.

## Features

- **Dynamic Configuration**: Automatically detects sections and keys in the `config.ini` file and prompts for missing or placeholder values.
- **Interactive Prompts**: Guides you through updating each variable, showing current values and allowing you to retain or change them.
- **Universal Support**: Works with any `config.ini` structure, making it suitable for a wide variety of projects.
- **Safe Execution**: Includes a confirmation step before making any changes.

## How It Works

1. **Scan Existing Configurations**: Reads the `config.ini` file to identify all sections and keys.
2. **Interactive Setup**: Prompts you to fill in missing or placeholder values for each key.
3. **Save Updates**: Writes the updated configuration back to the `config.ini` file.

## Usage

### Prerequisites

- Python 3.x installed on your system.
- A `config.ini` file in the same directory as the script.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/config-ini-setup.git
   cd config-ini-setup
   
2. Ensure you have a config.ini file in the project directory. If one does not exist, create it manually with your desired sections and keys.

### Running the Script

1. Run the script:
   python configure.py
2. Follow the prompts:

   - The script will display a welcome message and ask if you want to continue.
   - If you type y, the script will scan the config.ini file and guide you through updating values.
   - If you type n, the script will exit without making changes.
  
3. Once complete, the updated configuration will be saved.

### Customization

You can adapt the script to:

- Automatically generate a default config.ini if it doesn’t exist.
- Add validation for specific keys (e.g., checking if a port is an integer).
- Extend support for different configuration formats like JSON or YAML.

## Contributing
Contributions are welcome! Feel free to fork this repository, make improvements, and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
