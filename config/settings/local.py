from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-h5_uzdcov=!czf*&ncc&ays&&&$^3@z1uf7ds7dy(h*l-$d1xk'

############
# DataBase #
############

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# postgresql@docker用設定
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'admin',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': '0.0.0.0',
        'PORT': 5433,
    }
}

# ローカル確認用
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# 本番環境用
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'xxx@gmail.com'
EMAIL_HOST_PASSWORD = 'xxx'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'xxx@gmail.com'
