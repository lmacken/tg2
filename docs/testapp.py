#!/usr/bin/python
from wsgiref.simple_server import make_server
import sys
import tg
from tg.configuration import AppConfig
from tg import TGController, expose

class RootController(TGController):
    @expose()
    def index(self, *args, **kw):
        return 'HELLO FROM %s' % tg.request.path

    @expose()
    def somewhere(self):
        return 'WELCOME SOMEWHERE'

    @expose('testapp.mak')
    def test(self):
        return dict(ip=tg.request.remote_addr)

app_config = AppConfig()
app_config.use_toscawidgets = False
app_config['tg.root_controller'] = RootController()

#Setup support for MAKO.
app_config.renderers = ['mako']
app_config.default_renderer = 'mako'
app_config.use_dotted_templatenames = False

app_config.init_config({}, {})
app_config.setup_renderers()

app = app_config.setup_tg_wsgi_app(None)({}, full_stack=False)
make_server('', 8080, app).serve_forever()

