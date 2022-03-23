def intersection(center, circle_radius, pt1, pt2):
    (p1x, p1y), (p2x, p2y), (cx, cy) = pt1, pt2, center
    (x1, y1), (x2, y2) = (p1x - cx, p1y - cy), (p2x - cx, p2y - cy)
    dx, dy = (x2 - x1), (y2 - y1)
    dr = (dx ** 2 + dy ** 2) ** .5
    big_d = x1 * y2 - x2 * y1
    discriminant = circle_radius ** 2 * dr ** 2 - big_d ** 2
    intersections = [
        (cx + (big_d * dy + sign * (-1 if dy < 0 else 1) * dx * discriminant ** .5) / dr ** 2,
         cy + (-big_d * dx + sign * abs(dy) * discriminant ** .5) / dr ** 2)
        for sign in ((1, -1) if dy < 0 else (-1, 1))]
    if len(intersections) == 2 and abs(discriminant) <= 1e-9:
        return [intersections[0]]
    else:
        return intersections
