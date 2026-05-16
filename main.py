import tkinter as tk
import pyautogui
import math
import os
from PIL import ImageTk

from config import *
from core import (
    smooth_follow,
    create_sparkles,
    update_sparkles,

)
from utils.loader import load_image


# PATH
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(BASE_DIR, AVAILABLE_SKINS[CURRENT_SKIN])


# WINDOW
root = tk.Tk()
root.overrideredirect(True)
root.attributes("-topmost", True)
root.attributes("-topmost", True)
root.focus_force()

TRANSPARENT = "#123456"
root.config(bg=TRANSPARENT)
root.wm_attributes("-transparentcolor", TRANSPARENT)

WIN = 130

canvas = tk.Canvas(
    root,
    width=WIN,
    height=WIN,
    bg=TRANSPARENT,
    highlightthickness=0
)
canvas.pack()

center = WIN // 2


# IMAGE
img = load_image(IMAGE_PATH, SIZE)
photo = ImageTk.PhotoImage(img)
canvas.create_image(center, center, image=photo)


# SYSTEMS
sparkles = create_sparkles(canvas, 6, center) if ENABLE_SPARKLES else []

x, y = 500, 300
t = 0


def close_app(event=None):
    root.destroy()


def animate():
    global x, y, t

    mx, my = pyautogui.position()

    target_x = mx + OFFSET_X
    target_y = my + OFFSET_Y

    x = smooth_follow(x, target_x, FOLLOW_SPEED)
    y = smooth_follow(y, target_y, FOLLOW_SPEED)

    float_offset = math.sin(t) * FLOAT_STRENGTH
    t += 0.12

    root.geometry(
        f"{WIN}x{WIN}+{int(x - WIN/2)}+{int(y - WIN/2 + float_offset)}"
    )

    # SPARKLES
    if ENABLE_SPARKLES:
        update_sparkles(canvas, sparkles, center, t)

    root.after(16, animate)

# EXIT
root.bind("<Escape>", close_app)
root.focus_force()

animate()
root.mainloop()