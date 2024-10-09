# Python Port Scanner

A simple Python port scanner script for educational purposes.

## Features

- Scan IP addresses for open ports.
- Specify custom port ranges.
- Interruptible (Ctrl+C to stop and show results).
- Cross-platform (Windows, Linux, macOS).

## Usage

Run the script using the following command:

```bash
python port_scanner.py <ip_address> [-s START_PORT] [-e END_PORT]
```

Example:
```bash
python port_scanner.py 127.0.0.1 -s 1 -e 1000
```

## Disclaimer

For educational use only. Ensure you have permission before scanning any network or system.
