# type: ignore
# flake8: noqa

# Comando:
# python -c "import string as s;from secrets import SystemRandom as SR;print(''.join(SR().choices(s.ascii_letters + s.digits + s.punctuation, k=64)));"
#SECRET_KEY = '#sYcjfcnS`7b[S>W6r'J{("X%_lD("co6a;]Z.)CBhZM;.7lR^R"k0izuNbepz!m'

# DEBUG DEVE SER False em produção
#DEBUG = False

# Seu domínio ou IP devem vir aqui
#ALLOWED_HOSTS = [
#'34.16.154.229',
#]  # Troque * para seu domínio ou IP

# Config para postgresql
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'projeto',
#        'USER': 'usuario_projeto',
#        'PASSWORD': 'senha_projeto',
#        'HOST': 'localhost',
#        'PORT': '5432',
#    }
#}