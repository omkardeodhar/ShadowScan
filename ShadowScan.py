import socket
import requests
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
        sock.settimeout(timeout)
        try:
            sock.connect ((ip , port))
            print(f"\n{Fore.GREEN}# Port {port} is OPEN: {Style.RESET_ALL}")
            if port == 80 or port == 443 or port == 8080:
                header_info (ip , sock)
            else:
                service_enum = sock.recv(1024).decode('utf-8').strip()
                print(f"Service information for Port {port}: \n{service_enum}")
        except (socket.timeout , socket.error):
            pass
        finally:
            sock.close()

def header_info (ip , sock):
        try:
            url = f"GET / HTTP/1.1\r\nHost: {ip}\r\n\r\n"
            sock.send(url.encode('utf-8'))
            response_header = sock.recv(1024).decode('utf-8')
            print("Recieved Response: ")
            for line in response_header.split('\n'):
                print(line)
        except (socket.timeout , socket.error):
            pass
            
def main ():
    global timeout
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
    *   Version: 1.5                                      *
    *******************************************************
    {Style.RESET_ALL}
    """
    print(banner)

    target_domain = input("Enter the IPv4 address or Domain name of the target (without http/https/www): ")
    target_ip = get_ip (target_domain)
    try:
        timeout = float(input("Enter Socket timeout in seconds (Higher socket timeout will result in a slower scan): "))
    except ValueError:
        print("Enter valid timeout value")
        exit()
    if target_ip:
        common_ports = [21,22,23,25,53,80,110,135,137,138,139,389,443,445,636,995,1433,1434,3306,3389,8080]
        print(f"\nStarting port scan for {target_ip}: ")
        port_scan(target_ip , common_ports)
    else:
        print("There was some error resolving the IP.")
        exit()
        
if __name__ == "__main__":
    main()
