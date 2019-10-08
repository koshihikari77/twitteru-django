from .settings import *

DEBUG = True
INTERNAL_IPS = ['127.0.0.1']
SECRET_KEY = '*78qidg^^u=($&djk8d)$m)u8s@xge&_6w2vdp3#l@4cm7r$rz'

if DEBUG:
    def show_toolbar(request):
        return True

    INSTALLED_APPS += (
        'debug_toolbar',
    )
    MIDDLEWARE += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': show_toolbar,
    }
