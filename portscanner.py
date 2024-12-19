import socket
import termcolor
import pyfiglet

banner = pyfiglet.figlet_format("Ports Scanner")
print(banner)

def scan(target, ports):
    print('\n' + 'Starting The Scan For ' + str(target) + '\n')
    for port in range(1,ports):
        scan_port(target, port)


def scan_port(ipaddress, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        print("[+] Port Opened " + str(port))
        sock.close()
    except:
        pass


if __name__ == "__main__":

    targets = input("[+] Targets To Scan(split them by ,): ")
    ports = int(input("[+] How Many Ports You Want To Scan: "))

    if ',' in targets:
        print(termcolor.colored("[*] Scanning Multiple Targets", 'green'))
        for target in targets.split(','):
            scan(target.strip(' '), ports)
    else:
        scan(targets, ports)
