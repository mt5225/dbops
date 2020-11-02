# generate random user and prividges

sql = '''
CREATE USER 'new_user'@'localhost' IDENTIFIED BY 'password';
GRANT new_user_prividges ON *.* TO 'new_user'@'localhost';
'''

prividges = ['CREATE', 'SELECT', 'DELETE', 'INSERT', 'DROP']

from random_username.generate import generate_username
import random

for user in generate_username(20):
    priv = random.sample(range(4), 2)
    priv_str = ','.join([prividges[int(p)] for p in priv])
    out = sql.replace('new_user_prividges', priv_str).replace('new_user', user)
    print(out)


