import machine
import neopixel
import time


red = (128, 0, 0)
green = (0, 128, 0)


# Turn off all the LEDs
def off(np):
    for i in range(np.n):
        np[i] = (0, 0, 0)
    np.write()


def evens_green(np):
    for i in range(np.n):
        if i % 2 == 0:
            np[i] = green
        else:
            np[i] = red
    np.write()


def evens_red(np):
    for i in range(np.n):
        if i % 2 == 0:
            np[i] = red
        else:
            np[i] = green
    np.write()


def alternate_colors(np):
    if np[0] == green:
        evens_red(np)
    else:
        evens_green(np)


if __name__ == '__main__':
    # Data line is on pin 13
    # and there are 12 LEDs on our NeoPixel ring
    np = neopixel.NeoPixel(machine.Pin(13), 12)
    for i in range(20):
        alternate_colors(np)
        time.sleep(1)
    # do_connect()
    # at this point we should start a cycle of colors
    # and also start listening for any webrepl or api commands
