import os

class Config(object):
    base = 'mysql://'
    user = "user123"
    password = "password123"
    host = "db02"
    database = "webapp"

    #base = 'mysql+pymysql://root:@'
    #mysql://scott:tiger@localhost/foo
    #'mysql://user123:password123@db02/webapp'

    SQLALCHEMY_DATABASE_URI = base + user + ':' + password + '@' + host + '/' + database
    SQLALCHEMY_TRACK_MODIFICATIONS = False

