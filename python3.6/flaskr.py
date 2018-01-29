#!/usr/bin/env python
# coding:UTF-8

import os
import sqlite3
from flask import Flask,request,session,g, redirect, url_for, abort, render_template, flash


def connect_db():
  """Connects to the specific database."""
  rv = sqlite3.connect(app.config['DATABASE'])
  rv.row_factory = sqlite3.Row
  return rv