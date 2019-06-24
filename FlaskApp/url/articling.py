from flask import Flask, session, request
import time,datetime
from app import db, models,app
from flask_restful import Resource, Api, reqparse, abort
from flask import Flask, session, request,render_template,url_for
from flask_bootstrap import Bootstrap
from flask import Blueprint


barticling=Blueprint('barticling', __name__)

@barticling.route('/articling')
def articling():
    title='articling'
    return render_template('articling.html',title=title)