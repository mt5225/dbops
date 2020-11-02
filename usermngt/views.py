from django.shortcuts import render
from django.db import connections
import logging

# This retrieves a Python logging instance (or creates it)
logger = logging.getLogger(__name__)


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


# Create your views here.
def homepage_view(request):
    # Create your views here.
    cursor1 = connections['db001'].cursor()
    cursor2 = connections['db002'].cursor()
    # Query Result
    db_users = {
        'db001': get_users(cursor1),
        'db002': get_users(cursor2)
    }
    return render(request, "home.html", db_users)
