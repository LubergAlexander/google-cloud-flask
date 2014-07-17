import sys
import os
sys.path.insert(1, os.path.join(os.path.abspath('.'), os.path.abspath('venv/lib/python2.7/site-packages')))

from flask import Flask
import settings

app = Flask('blog')
app.config.from_object('blog.settings')

import views