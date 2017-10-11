import os
from nick import create_nick

# open user csv file
with open('users.csv') as userfile:
    # read the lines
    for row in userfile.readlines():
        # split line on ","
        user = row.strip().split(',')
        # assign values
        firstname = user[0]
        lastname = user[1]

        # call create_nick to build a username
        nickname = create_nick(firstname, lastname)

        # write user and nickname to file,

        with open('usernicks.csv', 'a') as usernicksfile:
            line = firstname + ',' + lastname + ',' + nickname + '\n'
            usernicksfile.write(line)
            with open('usernicks.csv'):
                if user[0] == user[0]:
                    from random import randint
                    number = randint(0, 9)
                if user[1] == user[1]:
                    from random import randint
                    number = randint(0, 9)
