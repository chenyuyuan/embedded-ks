from flask import Flask, session, request
import time,datetime
from app import db, models,app
from flask_restful import Resource, Api, reqparse, abort
from flask import Flask, session, request,render_template,url_for
from flask_bootstrap import Bootstrap
from flask import Blueprint


btopicapplying=Blueprint('btopicapplying', __name__)

@btopicapplying.route('/topicapplying')
def topicapplying():
    title='topicapplying'
    return render_template('topicapplying.html',title=title)