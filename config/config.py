from environs import Env

env = Env()
env.read_env()

DJANGO_SECRET_KEY = env.str("DJANGO_SECRET_KEY")
DJANGO_DEBUG = env.bool("DJANGO_DEBUG")
DJANGO_ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS")
