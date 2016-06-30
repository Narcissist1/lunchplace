# coding: utf-8
from flask_sqlalchemy import SQLAlchemy, BaseQuery
from datetime import datetime
from functools import wraps
from sqlalchemy.types import TypeDecorator, CHAR, TypeEngine
from sqlalchemy.dialects.postgresql import UUID
import uuid

db = SQLAlchemy()


class GUID(TypeDecorator):
    """Platform-independent GUID type.

    Uses Postgresql's UUID type, otherwise uses
    CHAR(32), storing as stringified hex values.

    """
    impl = TypeEngine

    def load_dialect_impl(self, dialect):
        if dialect.name == 'postgresql':
            return dialect.type_descriptor(UUID())
        else:
            return dialect.type_descriptor(CHAR(32))

    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        elif dialect.name == 'postgresql':
            return str(value)
        else:
            if not isinstance(value, uuid.UUID):
                return "%.32x" % uuid.UUID(value)
            else:
                # hexstring
                return "%.32x" % value

    def process_result_value(self, value, dialect):
        if value is None:
            return value
        else:
            return uuid.UUID(value)


def handle_exception(f):
    @wraps(f)
    def decoed(*args, **kwargs):
        raise_e = kwargs.pop("raise_e", True)
        try:
            return f(*args, **kwargs)
        except Exception as e:
            db_rollback()
            if raise_e is True:
                raise
            elif isinstance(raise_e, type) and issubclass(raise_e, Exception):
                if isinstance(e, raise_e):
                    raise
    return decoed


def cs_update(instance, **kwargs):
        """ 批量修改属性值
        :**kwargs: 属性值的dict
        """
        for k in instance._csupdate_keys:
            if k in kwargs:
                setattr(instance, k, kwargs.pop(k))
        # 检查是否有多余的参数
        if len(kwargs) > 0:
            raise KeyError("unknown argument found", kwargs.keys())
        if hasattr(instance, "update_time"):
            instance.update_time = datetime.utcnow()


@handle_exception
def db_commit(confirm=True):
    if confirm: db.session.commit()
    return True


@handle_exception
def db_flush(confirm=True):
    if confirm: db.session.flush()
    return True


@handle_exception
def db_rollback(confirm=True):
    if confirm: db.session.rollback()
    return True


@handle_exception
def db_add(item, commit=False, flush=False):
    if isinstance(item, (list, tuple)):
        for it in item:
            if hasattr(it, "update_fts"):
                it.update_fts()
        db.session.add_all(item)
    elif isinstance(item, db.Model):
        if hasattr(item, "update_fts"):
            item.update_fts()
        db.session.add(item)
    else:
        raise NotImplementedError
    if commit:
        db.session.commit()
    elif flush:
        db.session.flush()
    return item


@handle_exception
def db_delete(item, commit=False, flush=False, force=False):
    def _delete(item):
        if hasattr(item, "set_deleted") and not force:
            item.set_deleted()
        else:
            db.session.delete(item)

    if isinstance(item, db.Model):
        _delete(item)
    elif isinstance(item, (list, tuple)):
        map(_delete, item)
    elif isinstance(item, BaseQuery):
        item.delete()
    else:
        raise NotImplementedError
    if commit:
        if db_commit():
            return True
    elif flush:
        if db_flush():
            return True
