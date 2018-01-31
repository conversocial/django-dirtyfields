from django.db import models
from dirtyfields import DirtyFieldsMixin


class ListField(models.TextField):
    __metaclass__ = models.SubfieldBase

    # Loading from DB, expect value to be "foo,bar,123"
    def to_python(self, value):
        if value is None:
            return None
        if isinstance(value, basestring):
            if value:
                return value.split(",")
            else:
                return []
        return value

    # Saving to DB, expect value to be ["foo", "bar", 123]
    def get_db_prep_value(self, value, connection, prepared=False):
        if value is None:
            return None
        return ",".join(map(str, value))


class Animal(DirtyFieldsMixin, models.Model):
    name = models.CharField(max_length=32)
    list_of_things = ListField()
