# webgarden
Webpage on Pi3 to monitor temperatures and a camera view of growing chamber

Requirements: Python3.6+
              Django2.1+
              Raspberry Pi 3
              Temperature sensor: DS18B20 (wiring diagram: https://www.14core.com/wp-content/uploads/2015/11/Single-DS18B20-Temperature-Sensor-Wiring-diagram-Wired.jpg)
              Camera: Standard camera for Raspberry Pi, 2.0MP+
              

install python 3.6+
install django:
  pip install django
Unpack files into a directory
  git clone https://github.com/nelzon1/webgarden
run webserver:
  python manage.py runserver
