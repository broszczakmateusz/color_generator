import numpy as np
import matplotlib.pyplot as plt
import random


def generate_color():
    r = hex(random.randrange(0,255))
    g = hex(random.randrange(0,255))
    b = hex(random.randrange(0,255))
    r = r.split("0x")
    g = g.split("0x")
    b = b.split("0x")
    rgb = f"#{r[1].zfill(2)}{g[1].zfill(2)}{b[1].zfill(2)}"
    return rgb

def split_r_g_b(rgb_color):
    rgb_color = rgb_color.replace("#","")
    r = int(f"0x{rgb_color[0]}{rgb_color[1]}", 16)
    g = int(f"0x{rgb_color[2]}{rgb_color[3]}", 16)
    b = int(f"0x{rgb_color[4]}{rgb_color[5]}", 16)
    return r,g,b

def make_float_rgb(rgb_color):
    r,g,b = split_r_g_b(generated_rgb)

    r = r / 255
    g = g / 255
    b = b / 255
    return [r,g,b]


generated_rgb = generate_color()

plt.plot([0, 0], label=generated_rgb, color=generated_rgb)
plt.legend()

img = make_float_rgb(generated_rgb)
plt.imshow([[img]])
plt.show()
