import machine
import neopixel
# secrets are stored in secrets.py
import secrets
import time


def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(secrets.WIFI_SSID, secrets.WIFI_PASS)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig()


def cycle(np):
    n = np.n
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (255, 255, 255)
        np.write()
        time.sleep_ms(25)


def bounce_blue(np):
    n = np.n
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 128)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        time.sleep_ms(60)


def fade_red(np):
    n = np.n
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, 0, 0)
        np.write()


# Turn off all the LEDs
def clear(np):
    n = np.n
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()


# Make a nice red-orange glow
def fire(np, red=(240, 0, 0), orange=(240, 120, 0)):
    for i in range(np.n):
        if i % 2 == 0:
            np[i] = red
        else:
            np[i] = orange
    np.write()

def calc_orange(max_bright, current):
    return (max_bright - current, (max_bright - current) // 2 + 1, 0)

def flame(np):
    max_brightness = 120
    for f in range(4, max_brightness):
        red = (f, 0, 0)
        orange = calc_orange(max_brightness, f)
        # After this, the orange ones are dim and the red ones are bright
        fire(np, red, orange)
    for f in range(max_brightness, 4, -1):
        red = (f, 0, 0)
        orange = calc_orange(max_brightness, f)
        fire(np, red, orange)

if __name__ == '__main__':
    # Data line is on pin 13
    # and there are 12 LEDs
    np = neopixel.NeoPixel(machine.Pin(13), 12)
