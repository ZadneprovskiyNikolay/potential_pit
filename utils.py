def remove_close_values(xs, dif):
    res = []
    for x in xs:
        if len(res) == 0 or abs(res[-1] - x) > dif:
            res.append(x)

    return res