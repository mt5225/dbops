## create folder for db data

`mkdir ./dbdata`

## startup

- `docker-compose up -d`

## prepare mysql client [for django backup db]

- review setting on `./cnf/default.cnf`

## migrate to mysql backend [init django backup db]

`docker-compose exec web python /app/manage.py migrate`

expected output:

```bash
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
```

## verify

- open url `http://localhost:8080` and login as root/root, you should see the database name `dbops`, explore the tables
- open url `http://localhost:8000` for init django page