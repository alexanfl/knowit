infile = open("../res/3.dat")

friend_list = {}

def add_to_dict(string):
    status = 'friends' if string.split()[0] == 'friends' else 'hates'

    if status == 'friends':
        name = string.split()[1]
        friend = string.split()[2]

        if name not in friend_list:
            friend_list[name] = {} 
            friend_list[name][status] = []

        if status not in friend_list[name]:
            friend_list[name][status] = []

        if friend not in friend_list:
            friend_list[friend] = {} 
            friend_list[friend][status] = []

        if status not in friend_list[friend]:
            friend_list[friend][status] = []

        if friend not in friend_list[name][status]:
            friend_list[name][status].append(friend)
            
        if name not in friend_list[friend][status]:
            friend_list[friend][status].append(name)

    else:
        name = string.split()[0]
        enemy = string.split()[2]

        if name not in friend_list:
            friend_list[name] = {} 
            friend_list[name][status] = []

        if status not in friend_list[name]:
            friend_list[name][status] = []

        if enemy not in friend_list[name][status]:
            friend_list[name][status].append(enemy)

for line in infile:
    add_to_dict(line)

top_bitch = ''
cnt = 0
for name in friend_list:
    tmp = 0
    for friend in friend_list[name]['friends']:
        if friend in friend_list[name]['hates'] and name not in friend_list[friend]['hates']:
            tmp += 1

    top_bitch = name if tmp > cnt else top_bitch
    cnt = tmp if tmp > cnt else cnt

print(cnt, top_bitch)
