import socket
from colorama import Fore, Back, Style

def get_ip (domain):
    try:
        ip_addr = socket.gethostbyname (domain)
        return ip_addr
    except socket.gaierror:
        print("Could not resolve domain. Check for any errors in the spelling or IPv4 address.")
        exit()

def port_scan (ip , ports):
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if port == 443 or port == 80:
            sock.settimeout(2.0)
        else:
            sock.settimeout(0.5)
        try:
            sock.connect ((target_ip , port))
            print(f"Port {port} is OPEN.")
            service_enum = sock.recv(1024).decode('utf-8').strip()
            print(f"Service information for Port {port}: {service_enum}")
        except (socket.timeout , socket.error):
            continue
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

target_domain = input("Enter the IPv4 address or Domain name of the target (without http/https/www) : ")
target_ip = get_ip (target_domain)
if target_ip:
    common_ports = [21,22,23,25,53,80,137,138,139,389,443,445,1433,3306,3389,8080]
    print(f"Scanning most common ports: ")
    port_scan(target_ip , common_ports)
else:
    print("There was some error resolving the ip.")
    exit()
