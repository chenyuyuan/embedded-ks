from flask import Flask, session, request
import time,datetime
from app import db, models,app
from flask_restful import Resource, Api, reqparse, abort
from flask import Flask, session, request,render_template,url_for
from flask_bootstrap import Bootstrap
from flask import Blueprint


bquestion=Blueprint('bquestion', __name__)

@bquestion.route('/question/<questionid>/hotanswer')
def test(questionid):
    #print(questionid)
    uid = session['uid']
    answercontent = []
    #本问题页的问题的基本信息
    thisquestion = models.question.query.filter_by(id=questionid).first()
    flag0="0"
    if models.queStar.query.filter_by(uid=uid,queid=questionid).first():
        flag0="1"
    thistopic=models.topic.query.filter_by(id=thisquestion.reltopicid).first()
    sql = "select *  from answer where qid="+questionid
    answer = list()
    answered=[]
    answer = db.session.execute(sql)
    user=models.user.query.filter_by(id=uid).first()
    users=models.user.query.all()
    count=0
    for key in answer:
        for k in users:
            if k.id==key.uid:
                flag = "0"
                flag2 = "0"
                if models.ansLike.query.filter_by(uid=uid, ansid=key.id).first():
                    flag = "1"
                if models.ansStar.query.filter_by(uid=uid, ansid=key.id).first():
                    print("查到")
                    flag2 = "1"
                answered.append({
                    "id":key.id,
                    "qid":key.qid,
                    "like":key.like,
                    "ilike":flag,
                    "istar":flag2,
                    "comCount":key.comCount,
                    "uid":key.uid,
                    "account":k.account,
                    "shortIntro":k.shortIntro,
                    "time":time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(key.time)),
                    "score":key.score,
                    "queTitle":key.queTitle,
                    "topicid":key.topicid,
                    "delete":key.delete
                })
                break
    answered=answered[::-1]
    print(answered)
    # for i in range(0,len(answered)):
    #     print(answered[i]['id'])
    # for key in answered:
    #     print(key['uid'])
    for key in answered:
        with open("C://Users//梅西//Desktop//forserver//answer//"+str(key['id'])+".txt","r+") as f:
            h=f.read()
        answered[count]["content"]=h
        count=count+1
    # for key in answercontent:
    #      print('qq'+key+'\n')
    return render_template('/question.html', title='问题',users=users,myid=session["uid"],flag0=flag0,questionid=questionid,thistopic=thistopic,thisquestion=thisquestion,answered=answered,answercontent=answercontent)