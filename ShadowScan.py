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
            print(f"\nPort {port} is OPEN: ")
            if port == 80 or port == 443 or port == 8080:
                header_info (target_ip , port)
            else:
                service_enum = sock.recv(1024).decode('utf-8').strip()
                print(f"Service information for Port {port}: {service_enum}")
        except (socket.timeout , socket.error):
            pass
        finally:
            sock.close()

def header_info (ip , ports):
        try:
            url1 = f"http://{ip}:{ports}"
            url2 = f"https://{ip}:{ports}"
            if ports == 80 or ports == 8080:
                response = requests.get(url1)
            elif ports == 443:
                response = requests.get(url2)
            else:
                pass
            if response.status_code == 200:
                print(f"Server information: {response.headers['Server']}")
                print(f"Date: {response.headers.get('Date')}")
                print(f"Content-Type: {response.headers.get('Content-Type')}")
                print(f"Content-Length: {response.headers.get('Content-Length')}")
                print(f"Cache-Control: {response.headers.get('Cache-Control')}")
                print(f"Expires: {response.headers.get('Expires')}")
            else:
                print(f"HTTP status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error getting information: {e}")
            
def main ():
    global timeout,target_ip
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
