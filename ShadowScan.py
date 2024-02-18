import socket
import ssl
import time
from colorama import Fore, Back, Style

def port_scan (domain , ports):
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        try:
            sock.connect ((domain , port))
            print(f"\n{Fore.GREEN}# PORT {port} IS OPEN: {Style.RESET_ALL}")
            if port == 80 or port == 443 or port == 8080:
                header_info (sock, port)
            else:
                service_info = sock.recv(1024).decode('utf-8').strip()
                print(f"Service information for Port {port}: \n{service_info}")
        except (socket.timeout , socket.error):
            pass
        finally:
            sock.close()

def header_info (sock, port):
    if port == 80 or port == 8080:
        try:
            url = f"GET / HTTP/1.1\r\nHost: {target_domain}\r\n\r\n"
            sock.send(url.encode('utf-8'))
            response_header = sock.recv(4096).decode('utf-8')
            print(f"Recieved Response: ")
            for line in response_header.split('\n'):
                print(line)
        except (socket.timeout , socket.error) as e:
            print("Error: ",e)
        
    elif port == 443:
        url = f"GET / HTTP/1.1\r\nHost: {target_domain}\r\n\r\n"
        context = ssl.create_default_context()
        with context.wrap_socket(sock, server_hostname = target_domain) as ssl_sock:
            try:
                ssl_sock.send(url.encode('utf-8'))
                response_header = ssl_sock.recv(4096).decode('utf-8')
                print(f"Recieved Response: ")
                for line in response_header.split('\n'):
                    print(line)
            except (socket.timeout , socket.error) as e:
                print("Error: ",e)
            
def main ():
    global timeout,target_domain
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
    *   Version: 2.0                                      *
    *******************************************************
    {Style.RESET_ALL}
    """
    print(banner)
    
    try:
        target_domain = input("Enter the name of the Target Domain to scan (without http/https/www): ")
        socket.gethostbyname(target_domain)
        timeout = float(input("Enter Socket timeout in seconds (Higher socket timeout will result in a slower scan): "))
    except (ValueError , socket.gaierror) as e:
        print("Message: ",e)
        exit()
    if target_domain:
        time.sleep (1)
        common_ports = [21,22,23,25,53,80,110,135,137,138,139,389,443,445,636,995,1433,1434,3306,3389,8080]
        print("\nStarting port scan for: ",socket.gethostbyname(target_domain))
        port_scan(target_domain , common_ports)
    else:
        print("There was some error resolving the IP.")
        exit()
        
if __name__ == "__main__":
    main()
