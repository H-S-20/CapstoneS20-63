Capstone S20-63 Project: H.A.N.D. (Hand Augmented Narration Device)


To install properly, you will need some packages related to python and network communications


## H2 1. Accelerometer setup
    Run the following pip command on the Pi
        ```bash
        sudo pip3 install adafruit-circuitpython-lsm6ds```


## H2 2. MQTT protocol
    This protocol is used to connect the Raspberry Pi to our PC in a method that allows multiple devices to connect to the PC for communications. The PC is able to listen for any incoming messages sent at port 1883 (default) and all Raspberry Pis would send data at that port

    To install:
        On PC:
        1. Using a Windows 10 PC, install the MQTT setup at http://mosquitto.org/download/
        2. Once download is complete, search for Services in the Windows search bar.
        3. Right-click Mosquitto Broker and click Start
        4. Now that Mosquitto is running on your PC, we need to make an exception for port 1883 to allow data to come in through the firewall.
        Note: Taken from https://www.tomshardware.com/news/how-to-open-firewall-ports-in-windows-10,36451.html
            a. Navigate to Control Panel, System and Security and Windows Firewall.
            b. Select Advanced settings and highlight Inbound Rules in the left pane.
            c. Right click Inbound Rules and select New Rule.
            d. Click Port and click Next.
            e. Use protocol TCP and the port number 1883 and click Next.
            f. Select Allow the connection in the next window and hit Next.
            g. Select the network type as you see fit (I chose only private networks) and click Next.
            h. Name the rule something meaningful and click Finish.
        5. Download the paho package to use mqtt in Python with the commands:
            ```bash
            python -m pip install paho-mqtt```

        On Raspberry Pi (taken from https://pastebin.com/Etn59ppp)
        1. Install Mosquitto
            ```bash
            sudo apt-get install mosquitto -y
            sudo apt-get install mosquitto-clients```
 
        2. Configure Mosquitto.
            a. Run the following
            ```bash
            sudo nano /etc/mosquitto/mosquitto.conf```
 
            b. Delete the contents and paste the following:
            # Place your local configuration in /etc/mosquitto/conf.d/
            #
            # A full description of the configuration file is at
            # /usr/share/doc/mosquitto/examples/mosquitto.conf.example
            
            pid_file /var/run/mosquitto.pid
            
            persistence true
            persistence_location /var/lib/mosquitto/
            
            log_dest file /var/log/mosquitto/mosquitto.log
            
            allow_anonymous false
            password_file /etc/mosquitto/pwfile
            listener 1883
            
        3. Setup Mosquitto credentials (Enter any username and password and make sure you remember it)
        ```bash
        sudo mosquitto_passwd -c /etc/mosquitto/pwfile TYPE_YOUR_USERNAME_HERE```
        
        4. Test the Mosquitto by subscribing to a topic
        ```bash
        mosquitto_sub -d -u MOSQUITTO_USERNAME -P MOSQUITTO_PASSWORD -t dev/test```

        5. Install the paho package on this device
        ```bash
        sudo pip3 install paho-mqtt```
    
## H2 3. Keyboard inputs
    To translate sensor input into keyboard input, we used the pynput library:
    ```bash
    python -m pip install pynput```
    
    Information about what types of keyboard inputs we can bind can be found here: https://pynput.readthedocs.io/en/latest/index.html