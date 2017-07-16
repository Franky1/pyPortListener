# pyPortListener
A simple Python script that listens on a socket (TCP or UDP) and prints incoming data to the console.

## Configuration
If you want to use it, you should change settings to your needs:
- IP address, usually '0.0.0.0'
- PORT number
- Protocol (TCP or UDP)

## Issues
1. Currently everything is hardcoded (IP, Port, TCP/UDP)...  
Would be better with ARGS or ENV or INI file...  
INI file not recommended for Docker deployment, better with ENV variables.  
2. No setup/pip installation provided.
## Python
Script was tested and run with:
- Python 3.5.3.1 on Windows 64 (WinPython)
- Python 3.5.2 on Ubuntu 16.04

## Dependencies
External libraries installed py pip:
- requests

If you run it on your local machine, you have to install it manually.  
If you use the Dockerfile, it will be installed in Docker image.

## Docker
The Python script could be run as a Docker container.  
A Dockerfile is provided in the Git repository.

#### docker build  
Build the Docker image from the remote Dockerfile and Source Code in the GitHub:
```Bash
docker build -t pyportlistener https://github.com/Franky1/pyPortListener.git
```

#### docker run  
Run the Container with Console and Expose Port:
```Bash
docker run -it -p 5055:5055 --rm --name portlistener pyportlistener
```