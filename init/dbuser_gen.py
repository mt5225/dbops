# generate random user and prividges
from random_username.generate import generate_username
import random

sql = '''
CREATE USER 'new_user'@'localhost' IDENTIFIED BY 'password';
GRANT new_user_prividges ON *.* TO 'new_user'@'localhost';
'''

prividges = ['CREATE', 'SELECT', 'DELETE', 'INSERT', 'DROP']

def gen_priv():
    priv = random.sample(range(4), 2)
    priv_str = ','.join([prividges[int(p)] for p in priv])
    return priv_str

def deleteContent(pfile):
    pfile.seek(0)
    pfile.truncate()

if __name__ == "__main__":
    with open('init_001.sql', 'a') as f001, open('init_002.sql', 'a') as f002: 
        deleteContent(f001)
        deleteContent(f002)
        for user in generate_username(20):
            for f in [f001, f002]:
                f.write(sql.replace('new_user_prividges', gen_priv()).replace('new_user', user))
        

