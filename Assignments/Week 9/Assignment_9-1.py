def orangecap(d):
    player_totals = {}
    for match in d.values():
        for player, runs in match.items():
            player_totals[player] = player_totals.get(player, 0) + runs

    max_scorer = max(player_totals.items(), key=lambda x: x[1])
    return max_scorer

d = eval(input())
print(orangecap(d), end='')