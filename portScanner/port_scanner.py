#!/usr/bin/env python3
import sys
import socket
import argparse
import signal

def signal_handler(sig, frame):
    print('\nScan interrupted by user. Showing results (not all but from start to cancel)...')
    display_results()
    sys.exit(0)

def probe_port(ip, port, result=1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        r = sock.connect_ex((ip, port))
        if r == 0:
            result = r
        sock.close()
    except Exception as e:
        pass
    return result

def scan_ports(ip, start_port, end_port):
    global open_ports
    open_ports = []
    try:
        for port in range(start_port, end_port + 1):
            sys.stdout.write(f"\rScanning port {port}")
            sys.stdout.flush()
            response = probe_port(ip, port)
            if response == 0:
                open_ports.append(port)
    except KeyboardInterrupt:
        print('\nScan interrupted by user. Showing results so far...')
    finally:
        sys.stdout.write("\n")
    return open_ports

def display_results():
    if open_ports:
        print("\nOpen Ports are: ")
        print(sorted(open_ports))
    else:
        print("\nNo open ports found")

def main():
    parser = argparse.ArgumentParser(description="Simple Python Port Scanner")
    parser.add_argument("ip", help="IP address to scan")
    parser.add_argument("-s", "--start", type=int, default=1, help="Start port (default: 1)")
    parser.add_argument("-e", "--end", type=int, default=65535, help="End port (default: 65535)")
    args = parser.parse_args()

    print("Simple Python Script Port Scanner")
    print(f"Scanning {args.ip} from port {args.start} to {args.end}")
    print("Press Ctrl+C to interrupt the scan and see results")

    signal.signal(signal.SIGINT, signal_handler)

    open_ports = scan_ports(args.ip, args.start, args.end)
    display_results()

if __name__ == "__main__":
    main()