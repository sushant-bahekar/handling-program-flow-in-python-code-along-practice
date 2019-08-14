# --------------
import json
from collections import Counter
with open(path) as f:
    data = json.load(f)
#print(data) 
# Code starts here
#  Can you find how many deliveries were faced by batsman  `SC Ganguly`.
a = (data['innings'][0]['1st innings']['deliveries'])
count = 0
for i in a:
    for n,info in i.items():
        if info['batsman'] == 'SC Ganguly':
            count = count + 1
print(count)
#  Who was man of the match and how many runs did he scored 
print(data['info']['player_of_match'])
runs_scored = 0
a = (data['innings'][0]['1st innings']['deliveries'])
for runs in a:
    for delivery_number, info in runs.items():
        if info['batsman'] == 'BB McCullum':
            runs_scored = runs_scored + info['runs']['batsman']
print(runs_scored)
#  Which batsman played in the first inning?
batsman = []
for balls in a:
    for ball, info in balls.items():
        batsman.append(info['batsman'])
print(set(batsman))
# Which batsman had the most no. of sixes in first inning ?
most_sixes = []
for sixes in a:
    for delivery_number, info in sixes.items():
        if 'runs' in info and info['runs']['batsman'] == 6:
            most_sixes.append(info['batsman'])
bats_sixes = Counter(most_sixes)
print(bats_sixes)
# Find the names of all players that got bowled out in the second innings.
second_innings_deliveries = data['innings'][1]['2nd innings']['deliveries']
bowled_players = []
for bowled_out in second_innings_deliveries:
    for delivery_number, delivery_info in bowled_out.items():
        if 'wicket' in delivery_info and delivery_info['wicket']['kind'] == 'bowled':
            bowled_players.append(delivery_info['wicket']['player_out'])
print(bowled_players)
# How many more "extras" (wides, legbyes, etc) were bowled in the second innings as compared to the first inning?
extras_1st_inning = [ delivery_info
                    for delivery in a
                    for delivery_number, delivery_info in delivery.items()
                    if 'extras' in delivery_info]
extras_2nd_inning = [ delivery_info
                    for delivery in second_innings_deliveries
                    for delivery_number, delivery_info in delivery.items()
                    if 'extras' in delivery_info]
difference = len (extras_1st_inning) - len (extras_2nd_inning)
print(difference)


# Code ends here


