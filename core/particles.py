import math
import random

def create_sparkles(canvas, count, center):
    sparkles = []

    for _ in range(count):
        angle = random.uniform(0, math.tau)
        radius = random.uniform(25, 50)
        size = random.uniform(1, 2.5)

        s = canvas.create_oval(0, 0, size, size, fill="#fff4a3", outline="")
        sparkles.append({
            "id": s,
            "angle": angle,
            "radius": radius,
            "size": size,
            "phase": random.uniform(0, math.tau)
        })

    return sparkles


def update_sparkles(canvas, sparkles, center, t):
    for s in sparkles:
        s["phase"] += 0.08

        px = center + math.cos(s["angle"] + t * 0.2) * s["radius"]
        py = center + math.sin(s["angle"] + t * 0.2) * s["radius"]

        alpha = (math.sin(s["phase"]) + 1) / 2
        size = s["size"] * (0.7 + alpha * 0.6)

        canvas.coords(
            s["id"],
            px - size, py - size,
            px + size, py + size
        )