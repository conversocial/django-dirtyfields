# Minimum files that are needed to run django test suite

SECRET_KEY = 'WE DONT CARE ABOUT IT'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

INSTALLED_APPS = ('tests', )
