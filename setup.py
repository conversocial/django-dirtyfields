from setuptools import setup, find_packages

def listify(filename):
    return filter(None, open(filename, 'r').read().split('\n'))

def run_test_suite():
    import unittest
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite

setup(
    name = "django-dirtyfields",
    version = "0.2.4",
    url = 'http://github.com/smn/django-dirtyfields',
    license = 'BSD',
    description = "Tracking dirty fields on a Django model instance",
    long_description = open('README.rst','r').read(),
    author = 'Simon de Haan',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = listify('requirements.pip'),
    classifiers = listify('CLASSIFIERS.txt'),
    test_suite="setup.run_test_suite"
)
