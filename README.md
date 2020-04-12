# HBNB

This is the console /command interpreter for the Holberton Airbnb clone project. The console can be used to store objects in and retrieve objects from a JSON.

### Supported classes:
* BaseModel
* User
* State
* City
* Amenity
* Place
* Review

### Commands:
* create - create an object
* show - show an object (based on id)
* destroy - destroy an object
* all - show all objects, of one type or all types
* quit/EOF - quit the console
* help - see descriptions of commands

To start, navigate to the project folder and enter `./console.py` in the shell.

#### Create
`create <class name>`
Ex:
`create BaseModel`

#### Show
`show <class name> <object id>`
Ex:
`show User my_id`

#### Destroy
`destroy <class name> <object id>`
Ex:
`destroy Place my_place_id`

#### All
`all` or `all <class name>`
Ex:
`all` or `all State`

#### Quit
`quit` or `EOF`

#### Help
`help` or `help <command>`
Ex:
`help` or `help quit`

Additionally, the console supports `<class name>.<command>(<parameters>)` syntax.
Ex:
`City.show(my_city_id)`

# 0x02. AirBnB clone - MySQL
Foundations - Higher-level programming ― AirBnB clone

###### :copyright: **[Holberton School](https://www.holbertonschool.com/)**
by _Guillaume_

## Learning Objectives
###### Background Context
Environment variables will be your best friend for this project!

- ```HBNB_ENV```: running environment. It can be “dev” or “test” for the moment (“production” soon!)
- ```HBNB_MYSQL_USER```: the username of your MySQL
- ```HBNB_MYSQL_PWD```: the password of your MySQL
- ```HBNB_MYSQL_HOST```: the hostname of your MySQL
- ```HBNB_MYSQL_DB```: the database name of your MySQL
- ```HBNB_TYPE_STORAGE```: the type of storage used. It can be “file” (using ```FileStorage```) or ```db``` (using DBStorage)
###### General
* Fourth teamwork
* What is Unit testing and how to implement it in a large project
* What is ```*args``` and how to use it
* What is ```**kwargs``` and how to use it
* How to handle named arguments in a function
* How to create a MySQL database
* How to create a MySQL user and grant it privileges
* What ORM means
* How to map a Python Class to a MySQL table
* How to handle 2 different storage engines with the same codebase
* How to use environment variables

## Resources
* [AirBnB clone](https://intranet.hbtn.io/concepts/74)
* [cmd module](https://docs.python.org/3.4/library/cmd.html)
* [packages](https://intranet.hbtn.io/concepts/66)
* [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
* [args/kwargs](https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/)
* [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
* [How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
* [Jimmy’s (My)SQL Cheat Sheet](https://gist.githubusercontent.com/MasterProgrammer200/771e877ff56a4e75f32d/raw/a66990e0935dc95029a1bba05db07c57cf231d9f/mySQLCheatSheet.SQL)
* [Python3 and environment variables](https://docs.python.org/3/library/os.html?highlight=env#os.getenv)
* [Object Relational Mapping with Python’s SQL Alchemy](https://medium.com/@eightlimbed/object-relational-mapping-with-pythons-sql-alchemy-1af658b02679)
* [SQLAlchemy](https://docs.sqlalchemy.org/en/13/)
* [MySQL 5.7 SQL Statement Syntax](https://dev.mysql.com/doc/refman/5.7/en/sql-syntax.html)
* [AirBnB clone - ORM](https://www.youtube.com/watch?v=jeJwRB33YNg&feature=youtu.be)

## Tasks
* [x] 0. Fork me if you can!
* [x] 1. Bug free!
* [x] 2. Console improvements
* [x] 3. MySQL setup development
* [x] 4. MySQL setup test
* [ ] 5. Delete object
* [x] 6. DBStorage - States and Cities
* [x] 7. DBStorage - User
* [x] 8. DBStorage - Place
* [x] 9. DBStorage - Review
* [ ] 10. DBStorage - Amenity... and BOOM!

## Developers
Juan Camilo Esquivel, Javier Andrés Garzón Patarroyo
- [website](https://tecnoayuda.co/)

:man_technologist: :books: :computer: :globe_with_meridians:
