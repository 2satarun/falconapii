import falcon
from main.settings import *
from main.views.Abc1 import *
app = falcon.App()
appi = abc1()
app.add_route('/abc1', appi)


