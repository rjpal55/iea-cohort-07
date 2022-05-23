import os

def get_db_host():
    host = os.getenv("DATABASE_HOST")
    if not host:
        return None
    my_host = "mysql://" + host
    return my_host


get_db_host()
