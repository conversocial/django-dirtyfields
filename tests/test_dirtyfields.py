from unittest import TestCase
from tests.models import Animal
from django.core.management import call_command
from django.db import connection, DatabaseError


class TestDirtyFields(TestCase):
    def setUp(self):
        cur = connection.cursor()
        try:
            cur.execute("DROP TABLE tests_animal")
        except DatabaseError:
            pass
        call_command('syncdb')

    def test_original_state_is_stashed_on_init(self):
        a = Animal(name='Duck')
        self.assertEqual(
            a._original_state,
            {'id': None,
             'name': 'Duck',
             'list_of_things': []})

    def test_is_dirty(self):
        a = Animal()
        self.assertTrue(a.is_dirty())
        a.save()
        self.assertFalse(a.is_dirty())
        a.name = 'Fred'
        self.assertTrue(a.is_dirty())

    def test_get_dirty_fields(self):
        a = Animal(name='Bobcat')
        a.save()

        a.name = 'House cat'
        self.assertEqual(a.get_dirty_fields(), {'name': 'Bobcat'})

    def test_clears_dirty_fields_on_save(self):
        a = Animal(name='Shark')
        self.assertEqual(a.get_dirty_fields(), {})
        a.save()
        self.assertEqual(a.get_dirty_fields(), {})

    def test_makes_copy_of_mutable_field(self):
        a = Animal(name='Duck',
                   list_of_things=['wing', 'bill', 'webbed foot'])
        self.assertNotEqual(
            id(a.list_of_things),
            id(a._original_state['list_of_things']))
        a.list_of_things[0] = 'tail'
        self.assertEqual(a.get_dirty_fields(),
                         {'list_of_things': ['wing', 'bill', 'webbed foot']})
