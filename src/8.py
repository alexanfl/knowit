from numpy import ones

num_players = 1337
progress = ones(num_players) 


def move(pos, eyes, player_number):
    ladders = [[3,17], [8,10], [15,44], [22,5], [39,56], [49,75], [62,45], [64,19], [65,73], [80,12], [87,79]]
    hit_ladder = 0
    new_pos = pos + eyes if pos+eyes <= 90 else pos
    print("Player #%d rolled a %d and moved to %d" % (player_number, eyes, new_pos))
    for elem in ladders:
        if new_pos == elem[0]:
            print("    ... but hit a ladder and moved to %d" % elem[1])
            hit_ladder = 1
            return elem[1], hit_ladder

    return new_pos, hit_ladder

infile = open("../res/8.dat")

player = 0
ladders_hit = 0
for line in infile:
    if player == num_players:
        player = 0

    the_move = move(progress[player], int(line), player)
    progress[player] = the_move[0]
    ladders_hit += the_move[1]

    if progress[player] == 90:
        print("The Winner is player #%d" % (player+1))
        winner = player+1
        break

    player += 1

print("The player number times ladders hit:", winner*ladders_hit)
