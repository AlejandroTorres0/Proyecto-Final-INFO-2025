from .base import *


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR_STR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR_STR, 'media')

DEBUG = False

#ALLOWED HOSTS = ['DOMINIO']
ALLOWED_HOSTS = ['santiagojr.pythonanywhere.com'] #Dominio brindado por pythonanywhere
SECRET_KEY = 'x@t(mrmj%d&i7(xitkka8i_*kx!2_$l+-d=ce2mc*=4p$++lw('
