import configparser
import os
import sys

def load_config(file_path):

    config = configparser.ConfigParser()

    if os.path.exists(file_path):
        print(f"Found existing config file: {file_path}")
        config.read(file_path)
    else:
        print(f"Config file not found: {file_path}")
        print("Please create a config.ini file with the appropriate structure.")
        exit(1)
    
    return config

def prompt_user_for_values(config):

    for section in config.sections():
        print(f"\n[{section}]")
        for key, value in config.items(section):
            current_value = value.strip() or "blank"
            user_input = input(f"{key} (current: {current_value}): ").strip()
            if user_input:  # If the user provides a value, update it
                config.set(section, key, user_input)

def save_config(config, file_path):

    with open(file_path, 'w') as configfile:
        config.write(configfile)
    print(f"Updated configuration saved to {file_path}")

def main():
    config_path = "config.ini"

    print("Welcome to the Config.ini Setup Utility!")
    print("This utility will scan your current configuration and walk you through setting each variable.")
    proceed = input("Do you wish to continue? (y/n): ").strip().lower()

    if proceed != 'y':
        print("Setup aborted. Exiting.")
        sys.exit(0)

    config = load_config(config_path)

    prompt_user_for_values(config)

    save_config(config, config_path)

if __name__ == "__main__":
    main()
