## find out remote laptop's IP

### on remote laptop

ipconfig

### on client laptop

nmap 192.168.0.0/24

Nmap scan report for 192.168.0.154
Host is up (0.0096s latency).
Not shown: 999 closed ports
PORT STATE SERVICE
22/tcp open ssh

## connect

ssh marc@192.168.0.154

## Setup UDP in F1 2016

Settings > Enable UDP > IP address: remote laptop's IP address (192.168.0.154) > Port: UDP port (default 20777)

## Run soc.py

Must be done in remote laptop terminal

## To-Do

1. Port forward remote laptop's UDP port to client laptop's

2. Handle connection/disconnection

3. Investigate broadcast (helps with port mapping)
