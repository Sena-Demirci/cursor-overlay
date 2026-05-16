def update_trail(trail_points, x, y, max_len):
    trail_points.append((x, y))

    if len(trail_points) > max_len:
        trail_points.pop(0)

    return trail_points


def draw_trail(canvas, trail_points):
    for i, (x, y) in enumerate(trail_points):
        size = i * 1.2

        canvas.create_oval(
            65-size, 65-size,
            65+size, 65+size,
            outline="#ffffff",
            tags="trail"
        )