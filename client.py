import sys
from socket import socket,AF_INET,SOCK_DGRAM,timeout


def main(port, ipaddr, filename):
    ## input check
    if (len(ipaddr.split('.')) != 4):
        raise Exception("Invalid IP address")
    try:
        int(port)
    except ValueError:
        print("Invalid port number")
        exit()
    s = socket(AF_INET, SOCK_DGRAM)
    s.settimeout(5)
    counter = 1
    flg = False
    with open(filename, "rb") as f:
        while True:
            # Adds an index to the current package
            counterBit = bytes(str(counter).zfill(10), 'utf-8')
            output = counterBit +f.read(90)
            # nothing left to send
            # send an empty packet that indicates that all packages were sent.
            # The program will stop running the second time it gets here
            if output[10:len(output)] == b'':
                if not flg:
                    flg = True
                else:
                    break
            # Send-receive loop. Sends a message over and over,
            # until it receives a reponse from the server
            while True:
                try:
                    s.sendto(output, (ipaddr, int(port)))
                    recvd, addr = s.recvfrom(1024)
                    if recvd == output:
                        counter += 1
                        break
                except timeout:
                    continue
    s.close()


"""
program assumes that v[1] - port, argv[2] - IP address. argv[3] - filename
"""
if __name__ == "__main__":
    if (len(sys.argv)) != 4:
        raise Exception("Expected 3 arguments")
    main(sys.argv[1], sys.argv[2], sys.argv[3])
