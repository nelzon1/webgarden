# webgarden
Webpage on Raspberry Pi3 to monitor temperatures and a camera view of growing chamber. Uses a Django webserver.

## Requirements: 
* Python3.5+
* Django2.1+
* Raspberry Pi 3
* Temperature sensor: DS18B20 [(wiring diagram)](https://www.14core.com/wp-content/uploads/2015/11/Single-DS18B20-Temperature-Sensor-Wiring-diagram-Wired.jpg)
* Camera: Standard camera for Raspberry Pi, 2.0MP+
              
## Installation
1. install python 3.5+
    *   sudo apt-get update
    *   sudo apt-get install python3
2. install django:
    *   pip install django
3. Unpack files into a directory
    *   git clone https://github.com/nelzon1/webgarden.git
4. run webserver:
    *   python manage.py runserver
    *   python manage.py runserver 0.0.0.0:8000


## Dockerfile
docker build -t webgarden .
docker run -it --rm --name webgarden-server webgarden
docker run -it --rm --name webgarden-server webgarden -p 8699:8000