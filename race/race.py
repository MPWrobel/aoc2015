time = 2503

best = 0
for line in open('input.txt'):
    (deer, _, _, speed, _, _,
     air, *_, rest, _) = line.split()  # type: ignore
    air, rest, speed = int(air), int(rest), int(speed)  # type: ignore
    cycle = air + rest
    cycles = int(time / cycle)  # type: ignore
    remainder = time % cycle  # type: ignore
    total = cycles * air
    total += remainder if remainder < air else air  # type: ignore
    distance = total * speed  # type: ignore
    if distance > best:  # type: ignore
        best = distance  # type: ignore

print(best)
