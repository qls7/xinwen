from functools import wraps

from models import db


def set_db_to_read(func):
    """设置使用读数据库"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        db.session().set_to_read()
        return func(*args, **kwargs)

    return wrapper


def set_db_to_write(func):
    """设置使用写数据库"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        db.session().set_to_write()
        return func(*args, **kwargs)

    return wrapper
