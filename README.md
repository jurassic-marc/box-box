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

## Run

In remote laptop terminal

Open a pyq shell, using /usr/local/bin/pyq

Note: pyq has been appended to /usr/bin but given error

## To-Do

1. Port forward remote laptop's UDP port to client laptop's

2. Handle connection/disconnection

3. Investigate broadcast (helps with port mapping)

4. pyq executible issue

## Notes

### 4. pyq executible

- currently had to manually install pyq v4.2.1 off GH

- used ci.sh as guide for how to install

- led to problems due to my mutliple q installs, i.e. l32 and l64
  - echo $QHOME was /home/marc/q/l64/ as per this guide: https://code.kx.com/q/kb/versions/, however pyq installation uses QHOME to understand what bit machine is at and where to look and install pyq config files and scripts, example: https://github.com/KxSystems/pyq/blob/master/setup.py#L174
  - fix was to make QHOME /home/marc so it could pick up l64 folder
  - had to bring down the q.k from l64 folder which has caused issue with the pyq executible
    - pyq => '2022.12.07T01:01:40.412 q.k does not match q version
    - /usr/local/bin/pyq => works
    - can replicate the 1st issue if I copy the l32 q.k to QHOME, i.e. cp ~/q/l32/q.k ~/q/
      - pyq => '2022.12.07T01:06:25.269 /home/marc/q/l32/./pyq.so: cannot open shared object file: No such file or directory [4] /home/marc/q/p.k:2: (`:./pyq 2:(`p_init;1)).pyq.python_dl
      - /usr/local/bin/pyq => '2022.12.07T01:01:40.412 q.k does not match q version
