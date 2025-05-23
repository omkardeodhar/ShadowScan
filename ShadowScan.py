import socket
import ssl
import time
from ftplib import FTP
from scapy.all import IP,TCP,sr
from colorama import Fore, Back, Style

def port_scan (domain , ports):
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        try:
            sock.connect ((domain , port))
            print(f"\n{Fore.GREEN}# PORT {port} IS OPEN: {Style.RESET_ALL}")
            if port == 21:
                ftp_info(sock, port)
            elif port == 135 or port == 137 or port == 138 or port == 139 or port == 445:
                windows_services_info (target_domain, port)
            elif port == 80 or port == 8080:
                header_info_http(sock, port)
            elif port == 443 or port == 8443:
                header_info_https(sock, port)
            else:
                try:
                    service_info = sock.recv(4096).decode('utf-8').strip()
                    if service_info:
                        print(f"Service information for Port {port}: \n{service_info}")
                    else:
                        print(f"No Response from Port: {port}")
                except UnicodeDecodeError as e:
                    print(f"WARNING: {e}")
        except (socket.timeout , socket.error):
            pass
        finally:
            sock.close()
            
def windows_services_info (domain, port):
    try:
        smb_packet = IP(dst=domain, version = 4)/TCP(dport=port, flags="S")
        smb_response = sr(smb_packet, timeout=timeout, verbose=0)
        if smb_response:
            print(smb_response)
        else:
            print(f"No Response from Port: {port}")
    except Exception as e:
        print(f"ERROR: {e}")
            
def ftp_info (sock, port):
    try:
        service_info = sock.recv(4096).decode('utf-8').strip()
        if service_info:
            print(f"Service information for Port {port}: \n{service_info}")
            ftp = FTP()
            ftp.connect(sock.getpeername()[0], port)
            ftp.login("anonymous", "")
            print("ANONYMOUS LOGIN SUPPORTED")
            ftp.quit()
        else:
            print(f"No Response from Port: {port}")
    except Exception as e:
        print(f"WARNING: {e}")

def header_info_http (sock, port):
    url = f"HEAD / HTTP/1.1\r\nHost: {target_domain}\r\n\r\n"
    try:
        sock.send(url.encode('utf-8'))
        response_header = sock.recv(4096).decode('utf-8')
        if response_header:
            print(f"Recieved Response: ")
            for line in response_header.split('\n'):
                print(line)
        else:
            print(f"No Response from Port: {port}")
    except (socket.timeout , socket.error) as e:
        print(f"ERROR: {e}")

def header_info_https (sock, port):
    url = f"HEAD / HTTP/1.1\r\nHost: {target_domain}\r\n\r\n"
    context = ssl.create_default_context()
    with context.wrap_socket(sock, server_hostname = target_domain) as ssl_sock:
        try:
            ssl_sock.send(url.encode('utf-8'))
            response_header = ssl_sock.recv(4096).decode('utf-8')
            if response_header:
                print(f"Recieved Response: ")
                for line in response_header.split('\n'):
                    print(line)
            else:
                print(f"No Response from Port: {port}")
        except (socket.timeout , socket.error) as e:
            print(f"ERROR: {e}")
            
def main ():
    global timeout,target_domain
    banner = f""" {Fore.RED}{Back.BLACK}{Style.BRIGHT}
    *******************************************************
    *             SHADOWSCAN PORT SCANNER                 *
    *                                                     *
    *   WARNING: THIS TOOL IS FOR EDUCATIONAL AND         *
    *   AUTHORIZED USE ONLY. USE WITH CAUTION AND         *
    *   PROPER PERMISSION; MAY VIOLATE PRIVACY LAWS.      *
    *                                                     *
    *   Developed by: Omkar Deodhar                       *
    *   Version: 2.5                                      *
    *******************************************************
    {Style.RESET_ALL} """
    print(banner)
    
    try:
        target_domain = input("Enter the name of the Target Domain to scan without http/https/www (ex: target_domain.com or target_domain.in etc): ")
        socket.gethostbyname(target_domain)
        timeout = float(input("Enter Socket timeout in seconds (Higher socket timeout will result in a slower scan): "))
        if target_domain:
            time.sleep (2)
            common_ports = [21,22,23,25,53,80,110,135,137,138,139,389,443,445,636,995,1433,1434,3306,3389,8080,8443]
            print("\nStarting port scan for Domain:",target_domain,", IP:",socket.gethostbyname(target_domain))
            port_scan(target_domain , common_ports)
            print(f"\n{Fore.RED}{Style.BRIGHT}Completed port scan for Domain: {target_domain}, IP: {socket.gethostbyname(target_domain)}{Style.RESET_ALL}")
        else:
            pass
            exit()
    except Exception as e:
        print(f"WARNING: {e}")
        exit()
        
if __name__ == "__main__":
    main()
