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
```

## verify

- open url `http://localhost:8080` and login as root/root, you should see the database name `dbops`, explore the tables
- open url `http://localhost:8000` for init django page

## browser target database 

- open url `http://localhost:8080`

### for db001

 - host: db001
 - username: root
 - password: root001

### for db002

 - host: db002
 - username: root
 - password: root002

## debug

`docker-compose logs -f web`