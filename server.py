import socket, sys

def main(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('', int(port)))
    outputStr = str()
    wasPrinted = False
    currentData = str()
    counter = 1
    while True:
        data, addr = s.recvfrom(1024)
        dataTrimmed = data[10:len(data)]
        # reset the print check and the counter in case new packet was received
        if (dataTrimmed != b'') & (wasPrinted) & (int(data[0:10]) == 1):
            wasPrinted = False
            counter = 1
        # ACK packet was dropped - resend the packet
        if currentData == data:
            s.sendto(data, addr)
            continue
        # after previous two checks -- check if package index matches expected index
        # it it wasn't matching - a package was skipped/delayed.
        if counter != int(data[0:10]):
                continue
        # check if END packet(b'' in this case) was received, print the message
        if (dataTrimmed == b'') & (not wasPrinted):
            print(outputStr[0:len(outputStr)-1])
            outputStr = str()
            wasPrinted = True
        currentData = data
        # string containing decoded bits from received message
        outputStr += data[10:len(data)].decode()
        counter += 1
        s.sendto(data, addr)
        
"""
runs main() function if input is valid
"""
if __name__ == "__main__":
    # check input
    if len(sys.argv) != 2:
        raise Exception("Incorrect input, expected one parameter")
    try:
        int(sys.argv[1])
    except ValueError:
        print("Invalid port number")
        exit()
    main(sys.argv[1])
