from django.shortcuts import render
from django.db import connections
import logging

# This retrieves a Python logging instance (or creates it)
logger = logging.getLogger(__name__)

# List of target database
target_dbs = ['db001', 'db002']


def get_users(cursor):
    qstr = """ SELECT CONCAT('SHOW GRANTS FOR ''',user,'''@''',host,''';') FROM mysql.user """
    users = []
    with cursor as cursor:
        cursor.execute(qstr)
        result = cursor.fetchall()
        for item in result:
            cursor.execute(item[0])
            usr_info = cursor.fetchall()
            logger.debug(usr_info)
            users.append(usr_info[0][0])
    return users


# Create homepage views here.
def homepage_view(request):
    db_users_dict = {db: get_users(
        connections[db].cursor()) for db in target_dbs}
    return render(request, "home.html", db_users_dict)
