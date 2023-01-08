task1 = '1h 45m,360s,25m,30m 120s,2h 60s'
overall = 0


for i in task1.split(','):
    for r in i.split(' '):
        if r[-1] == 'h':
            overall += int(r.replace('h', '')) * 60
        elif r[-1] == 'm':
            overall += int(r.replace('m', ''))
        elif r[-1] == 's':
            overall += int(r.replace('s', '')) / int(60)
        else:
            print("Warning: found unexpected value")

print(int(overall))
