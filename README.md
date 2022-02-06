# udp-transfer

A client-server UDP messaging script, with dropped packets handling.
Sends a file provided by the client to the server line by line, prints the output on the server's console.

### Running the program

**1. Prerequisites:**
  - Get the IP the server machine by using `ifconfig` or `ip a`
  - Select an available port (anything above 1000 should be fine)

**2. Executing the program:**
  - First, run `python server.py portnumber` on the designated server macine. 
    - `port` being the desired listening port.
    - for example, `python server.py 12345` will make the server listen to port 12345.
  - Now, run `python client.py port, ipaddr, filename` on the clinet machine.
    - `port` is the server's listening port.
    - `ipaddr` is the server's address.
    - `filename` is the path to the desired file.
    - for example, `python client.py 12345, 127.0.0.1, file.txt` will send `file.txt`'s contents to port 12345 of machine using address 127.0.0.1
