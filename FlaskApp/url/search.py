from flask import Flask, session, request

from app import db, models,app
from flask_restful import Resource, Api, reqparse, abort
from flask import Flask, session, request,render_template,url_for
import flask
from flask_bootstrap import Bootstrap
from flask import Blueprint
import time,json


bsearch=Blueprint('bsearch', __name__)

@bsearch.route('/search')
def search():
    return render_template('/search.html', title='搜索',myid=session["uid"])

@bsearch.route('/search/searching',methods=['GET','POST'])
def searching():
    req=request.get_json()
    content=req["content"]
    uid=session["uid"]
    topics=models.topic.query.all()
    questions=models.question.query.all()
    topic=[]
    question=[]
    msg="0"
    for key in topics:
        if content in key.topic:
            topic.append({
                "id":key.id,
                "topic":key.topic,
                "time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(key.time)),
                "topicIntro":key.topicIntro
            })
            msg="1"
    for key in questions:
        if content in key.question:
            question.append({
                "id":key.id,
                "question":key.question,
                "time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(key.time)),
                "queContent":key.queContent
            })
            msg="1"
    if msg=="0":
        ms="no"
    elif msg=="1":
        ms="good"
    return json.dumps({
        "msg":ms,
        "topic":topic,
        "question":question
    })

