time = 2503

deers = []
for line in open('input.txt'):
    (_, _, _, speed_str, _, _,
     air_str, *_, rest_str, _) = line.split()  # type: ignore
    air, rest, speed = int(air_str), int(rest_str), int(speed_str)
    deers.append({'air': air, 'rest': rest, 'speed': speed,
                  'flying': True, 'time': 1, 'distance': 0, 'points': 0})

best = 0
for _ in range(time):  # type: ignore
    lead = 0
    leaders: list = []
    for deer in deers:
        if deer['flying']:
            deer['distance'] += deer['speed']
            if deer['time'] == deer['air']:
                deer['flying'] = False
                deer['time'] = 0
        elif deer['time'] == deer['rest']:
            deer['flying'] = True
            deer['time'] = 0

        deer['time'] += 1

        if deer['distance'] > lead:
            lead = deer['distance']
            leaders = [deer]
        elif deer['distance'] == lead:
            leaders.append(deer)

    for leader in leaders:
        leader['points'] += 1

scores = list(deer['points'] for deer in deers)
scores.sort(reverse=True)
for i, score in enumerate(scores):
    print(i+1, score)
