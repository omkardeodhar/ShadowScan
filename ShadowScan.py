import socket
from colorama import Fore, Back, Style, init

def get_ip (domain):
    try:
        ip_addr = socket.gethostbyname (domain)
        return ip_addr
    except socket.gaierror:
        print("Could not resolve domain. Check for any errors in the spelling.")
        exit()

def port_scan (target_ip , port_range):
    for port in range (port_range[0], port_range[1] + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        
        try:
            sock.connect ((target_ip , port))
            print(f"Port {port} is OPEN.")
        except (socket.timeout , socket.error):
            print(f"Port {port} is CLOSED.")
        finally:
            sock.close()

background = Back.BLACK
text_style = Style.BRIGHT
banner = f"""
{Fore.RED}{background}{text_style}
*******************************************************
*             SHADOWSCAN PORT SCANNER                 *
*                                                     *
*   WARNING: THIS TOOL IS FOR EDUCATIONAL AND         *
*   AUTHORIZED USE ONLY. USE WITH CAUTION AND         *
*   PROPER PERMISSION; MAY VIOLATE PRIVACY LAWS.      *
*                                                     *
*   Developed by: Omkar Deodhar                       *
*   Version: 1.0                                      *
*******************************************************
{Style.RESET_ALL}
"""
print(banner)

target_domain = input("Enter the Domain name: ")
target_ip = get_ip (target_domain)
if target_ip:
    port_range_start = int(input("Enter the start of the port range: "))
    port_range_end = int(input("Enter the end of the port range: "))
    port_range = (port_range_start , port_range_end)
    print(f"Scanning Ports from {port_range_start} to {port_range_end}: ")
    port_scan(target_ip , port_range)
else:
    print("There was some error resolving the ip.")
    exit()
