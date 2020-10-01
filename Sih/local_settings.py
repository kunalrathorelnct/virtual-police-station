# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ydahzacfsedf)()sdfvj2v9m#@fe=j+gyk+#myxrkk$+i&m=^5=uey5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['172-31-47-29','13.127.177.145']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'btre_prod',
        'USER': 'dbadmin',
        'PASSWORD': 'redhat',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}