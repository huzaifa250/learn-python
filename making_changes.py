users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

print("Active users are : ", users)
##----------------------------------------------------------------------
# ex : 4 = 2 *2 , 9 = 3*3 , 6 = 3*2 , 8 = 2*4
for n in range(2, 10):
    for x in range(n, 2):
        if x % n == 0:
            print("")
