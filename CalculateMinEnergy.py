def calc_drone_min_energy(route):

    if not route:
        return

    maxHeight = route[0][2]

    for i in range(1, len(route)):
        if route[i][2] > maxHeight:
            maxHeight = route[i][2]
    return maxHeight - route[0][2]


route = [[0,   2, 10],
         [3,   5,  0],
         [9,  20,  6],
         [10, 12, 15],
         [10, 10,  8]]
print(calc_drone_min_energy(route))
