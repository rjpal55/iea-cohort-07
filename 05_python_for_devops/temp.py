import os

def get_db_host():
    host = os.getenv("DATABASE_HOST")
    my_host = "mysql://" + host
    return my_host