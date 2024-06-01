# TOR Changer Ip
- This script utilizes Tor to change the IP address using a specified password and port, along with a local HTTP proxy.

## Features

- Change your IP address using Tor.
- Easy-to-use Python script.
- Customize Tor settings such as `password`, port, and local HTTP proxy.

# Install TOR python

```
zay@tor:/# sudo apt update
zay@tor:/# sudo apt install tor
zay@tor:/# tor --version
```

```
pip3 install requests==2.26.0
```

# Password TOR

```
zay@tor:/# tor --hash-password your_password
zay@tor:/# sudo nano /etc/tor/torrc
HashedControlPassword <hash>
CookieAuthentication 1
zay@tor:/# sudo systemctl restart tor
```

# Install Python

```
zay@tor:/# sudo apt install python3
```

# Donwload

- https://www.torproject.org/download/

# Disclaimers

- Do not go on the dark web, you risk being traumatized so please do not go into
- I don't encourage anyone to go on the dark web

- TOR is not illegal, it just hides your IP, you should not go to illegal sites !
