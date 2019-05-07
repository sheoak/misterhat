"""emoji.py

Lists containing emoji to print on the sense-hat leds

"""

# colors definitions
y = (255, 255, 0) # Yellow
g = (0, 255, 0) # Green
c = (0, 0, 255) # Blue
r = (255, 0, 0) # Red
b = (0, 0, 0) # Black

EMOJI_TEMP_HIGH = [
    r, r, r, b, b, r, r, r,
    r, r, r, b, b, r, r, r,
    r, r, r, b, b, r, r, r,
    r, r, r, b, b, r, r, r,
    r, r, r, b, b, r, r, r,
    r, r, r, r, r, r, r, r,
    r, r, r, b, b, r, r, r,
    r, r, r, b, b, r, r, r
]

EMOJI_TEMP_LOW = [
    c, c, c, b, b, c, c, c,
    c, c, c, b, b, c, c, c,
    c, c, c, b, b, c, c, c,
    c, c, c, b, b, c, c, c,
    c, c, c, b, b, c, c, c,
    c, c, c, c, c, c, c, c,
    c, c, c, b, b, c, c, c,
    c, c, c, b, b, c, c, c
]

EMOJI_HUMIDITY_HIGH = [
    b, b, b, b, c, b, b, b,
    b, b, b, c, c, c, b, b,
    b, b, c, c, c, c, c, b,
    b, c, c, c, c, c, c, b,
    b, c, c, c, c, c, c, b,
    b, c, c, c, c, c, c, b,
    b, b, c, c, c, c, b, b,
    b, b, b, c, c, b, b, b
]

EMOJI_HUMIDITY_LOW = [
    b, b, b, b, r, b, b, b,
    b, b, b, r, r, r, b, b,
    b, b, r, r, r, r, r, b,
    b, r, r, r, r, r, r, b,
    b, r, r, r, r, r, r, b,
    b, r, r, r, r, r, r, b,
    b, b, r, r, r, r, b, b,
    b, b, b, r, r, b, b, b
]
EMOJI_PRESSURE_LOW = [
    b, b, b, r, r, b, b, b,
    b, b, b, r, r, b, b, b,
    b, b, b, r, r, b, b, b,
    b, b, b, r, r, b, b, b,
    r, r, r, r, r, r, r, r,
    b, r, r, r, r, r, r, b,
    b, b, r, r, r, r, b, b,
    b, b, b, r, r, b, b, b
]

EMOJI_PRESSURE_HIGH = [
    b, b, b, g, g, b, b, b,
    b, b, b, g, g, b, b, b,
    b, b, b, g, g, b, b, b,
    b, b, b, g, g, b, b, b,
    g, g, g, g, g, g, g, g,
    b, g, g, g, g, g, g, b,
    b, b, g, g, g, g, b, b,
    b, b, b, g, g, b, b, b
]

EMOJI_SHAKE = [
    y, y, y, b, y, y, y, y,
    y, y, b, b, b, y, y, y,
    y, b, b, y, b, b, y, b,
    b, b, y, y, y, b, b, b,
    b, y, y, b, y, y, b, y,
    y, y, b, b, b, y, y, y,
    y, b, b, y, b, b, y, y,
    b, b, y, y, y, b, b, y
]
