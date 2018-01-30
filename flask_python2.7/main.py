#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sys, os
from conf import setting 

app = Flask(__name__)
# FLASKR_SETTINGS = os.path.join(os.path.abspath('./'),'conf')
# print FLASKR_SETTINGS
# print setting.DEBUG
app.config.from_object(setting)     #模块下的setting文件名，不用加py后缀 
# app.config.from_envvar(FLASKR_SETTINGS)   #环境变量，指向配置文件setting的路径

db = SQLAlchemy(app)