dx = [0, 0, -0.5, 0.5]
dy = [-0.5, 0.5, 0, 0]
 
for tc in range(int(input())):
    totalReleased = 0
    count = 0
    N = int(input())
    atoms = []
    for _ in range(N):
        x, y, direction, energy = input().split()
        atoms.append((float(x), float(y), int(direction), int(energy)))
    while atoms:
        length = len(atoms)
        spots = []
        for idx in range(length):
            x, y, direction, energy = atoms.pop(0)
            if x >= -1000 and x <= 1000 and y >= -1000 and y <= 1000:
                x += dx[direction]
                y += dy[direction]
                spots.append((x, y))
                atoms.append((x, y, direction, energy))
        if len(set(spots)) != len(spots):
            indexs = []
            for idx in range(len(spots)):
                if not idx in indexs and spots.count(spots[idx]) != 1:
                    indexs.append(idx)
            indexs = list(reversed(sorted(indexs)))
            for index in indexs:
                x, y, direction, energy = atoms.pop(index)
                totalReleased += energy
    print("#{} {}".format(tc+1, totalReleased))