from flask import Flask, session, request

from app import db, models,app
from flask_restful import Resource, Api, reqparse, abort
from flask import Flask, session, request,render_template,url_for
import flask
from flask_bootstrap import Bootstrap
from flask import Blueprint


btopicSquare=Blueprint('btopicSquare', __name__)

@btopicSquare.route('/topicSquare')
def test():
    alltopic = models.topic.query.all()
    uid = session['uid']
    kk=str(uid)
    sql='select *  from topicstar where uid='+kk
    mystartopic = list()
    mystartopic = db.session.execute(sql)
    count=0

    # for key in mystartopic:
    #     print(key.topic)

    return render_template('/topicSquare.html', title='话题广场',myid=session["uid"],mystartopic=mystartopic,alltopic=alltopic)


