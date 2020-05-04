friends_last_seen = {
    'Rolf': 8,
    'Ann': 5,
    'Jen': 10
}


def see_friend(friend, name):
    print(id(friend))
    friend['name'] = 0


print(id(friends_last_seen))
print('ID Rolf', id(friends_last_seen['Rolf']))
see_friend(friends_last_seen, 'Rolf')
print(id(friends_last_seen))
print('ID Rolf', id(friends_last_seen['Rolf']))
