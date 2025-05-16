# Shadow-Scan Port Scanner - Project Documentation

## INTRODUCTION

- **Shadow-Scan Port Scanner** is a Python-based port scanning tool developed for educational and authorized use only.
- The tool is designed to identify open ports on a target domain and provides insights into potential vulnerabilities and services running on the system.
- This tool is a simple implementation of a port scanner to understand the basic concepts of networking and information gathering. This tool cannot be solely relied upon to give accurate results.
- For more in-depth analysis, use more advanced tools like **Nmap**, **Masscan**, etc.

## DISCLAIMER

⚠️ **Warning:** This tool is intended for educational and authorized use only. Use with caution and proper permission, as it may violate privacy laws.

## FEATURES

- **Port Scanning:** Identifies the most common open ports on the target domain.
- **Service Information:** Retrieves information about services running on common ports.
- Some of the supported ports for scanning are:
  1. **21** - FTP  
  2. **22** - SSH  
  3. **23** - Telnet  
  4. **25** - SMTP  
  5. **80** - HTTP  
  6. **443** - HTTPS  
  7. **445** - Microsoft SMB

## INSTALLATION

> **NOTE:** This tool is only **LINUX compatible**.

- The project is implemented in Python and uses libraries such as:
  - `socket`
  - `ssl`
  - `time`
  - `ftplib`
  - `scapy`
  - `colorama`

### Step-by-step Instructions:

1. Ensure Python is installed on your system. If not, run:
    ```bash
    sudo apt install python
    ```
    or
    ```bash
    sudo apt install python3
    ```

2. Install non-standard libraries:
    ```bash
    pip install colorama
    pip install scapy
    ```

3. Install Git to clone the repository:
    ```bash
    sudo apt install git
    ```

4. Clone this GitHub repository to your local machine:
    ```bash
    git clone https://github.com/omkardeodhar/ShadowScan.git
    ```

5. Navigate to the project directory:
    ```bash
    cd ShadowScan
    ```

6. Run the tool:
    ```bash
    python ShadowScan.py
    ```
    or (recommended):
    ```bash
    python3 ShadowScan.py
    ```

7. When prompted, enter the **Domain name** and **Socket timeout**.

> Users are encouraged to use the tool responsibly and with proper authorization.

