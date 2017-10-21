NeoPixel latern, powered by an esp8266 running MicroPython

## Getting started
Clone the repository  
Create a virtualenv and activate it  
`pip install -r requirements.txt`

## Flashing the hardware
To erase the existing firmware,
`esptool.py --port $(PORT) erase_flash`
To write micropython firmware,
`esptool.py --port $(PORT) --baud 46080 write_flash --flash_size=detect 0 $(FIRMWARE)

## Deploying the code
Activate the virtualenv  
Copy secrets.blank.py to secrets.py and edit as needed.  
Upload secrets.py to the hardware with adafruit-ampy,  
`ampy --port $(PORT) put secrets.py`
Upload lantern.py to the hardware as main.py 
`ampy --port $(PORT) put lantern.py main.py`
