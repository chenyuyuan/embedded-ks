from flask import Flask, session, request
import time,datetime
from app import db, models,app
from flask_restful import Resource, Api, reqparse, abort
from flask import Flask, session, request,render_template,url_for
from flask_bootstrap import Bootstrap
from flask import Blueprint
import time,json


bhome=Blueprint('bhome', __name__)

@bhome.route('/home')
def home():
    uid=session["uid"]
    user=[]
    temptopic=[]
    users=models.user.query.all()
    temptopics=models.tempTopic.query.all()
    for key in users:
        if key.id==uid:
            user=key
    for key in temptopics:
        flag0="0"
        if models.tempTopicSupport.query.filter_by(uid=uid,temptopicid=key.id).first():
            flag0="1"
        temptopic.append({
            "id":key.id,
            "uid":key.uid,
            "topic":key.topic,
            "isupport":flag0,
            "topicIntro":key.topicIntro,
            "support":key.support,
            "time": time.strftime("%m-%d %H:%M:%S", time.localtime(key.time))
        })
    temptopic=temptopic[::-1]
    answers=models.answer.query.all()
    answercontent = []
    answered = []
    uid = session['uid']
    user = models.user.query.filter_by(id=uid).first()
    username = user.account
    users = models.user.query.all()
    count = 0
    for key in answers:
        for k in users:
            if k.id == key.uid:
                flag = "0"
                flag2 = "0"
                if models.ansLike.query.filter_by(uid=uid, ansid=key.id).first():
                    flag = "1"
                if models.ansStar.query.filter_by(uid=uid, ansid=key.id).first():
                    print("查到")
                    flag2 = "1"
                answered.append({
                    "id": key.id,
                    "qid": key.qid,
                    "like": key.like,
                    "ilike": flag,
                    "istar": flag2,
                    "comCount": key.comCount,
                    "uid": key.uid,
                    "account": k.account,
                    "shortIntro": k.shortIntro,
                    "time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(key.time)),
                    "score": key.score,
                    "queTitle": key.queTitle,
                    "topicid": key.topicid,
                    "delete": key.delete
                })
                break
    print(answered)
    answered = answered[::-1]
    for key in answered:
        with open("C://Users//梅西//Desktop//forserver//answer//" + str(key['id']) + ".txt", "r+") as f:
            h = f.read()
        answered[count]["content"] = h
        count = count + 1
    return render_template('/home.html',user=user,myid=session["uid"],temptopic=temptopic,answered=answered,username=username,uid=uid,users=users)
@bhome.route('/home/like')
def homelike():
    uid=session["uid"]
    user=[]
    temptopic=[]
    users=models.user.query.all()
    temptopics=models.tempTopic.query.all()
    for key in users:
        if key.id==uid:
            user=key
    for key in temptopics:
        flag0="0"
        if models.tempTopicSupport.query.filter_by(uid=uid,temptopicid=key.id).first():
            flag0="1"
        temptopic.append({
            "id":key.id,
            "uid":key.uid,
            "topic":key.topic,
            "isupport":flag0,
            "topicIntro":key.topicIntro,
            "support":key.support,
            "time": time.strftime("%m-%d %H:%M:%S", time.localtime(key.time))
        })
    temptopic=temptopic[::-1]
    answers=models.answer.query.all()
    answercontent = []
    answered = []
    uid = session['uid']
    user = models.user.query.filter_by(id=uid).first()
    username = user.account
    users = models.user.query.all()
    count = 0
    for key in answers:
        for k in users:
            if k.id == key.uid:
                flag = "0"
                flag2 = "0"
                if models.ansLike.query.filter_by(uid=uid, ansid=key.id).first():
                    flag = "1"
                if models.ansStar.query.filter_by(uid=uid, ansid=key.id).first():
                    print("查到")
                    flag2 = "1"
                answered.append({
                    "id": key.id,
                    "qid": key.qid,
                    "like": key.like,
                    "ilike": flag,
                    "istar": flag2,
                    "comCount": key.comCount,
                    "uid": key.uid,
                    "account": k.account,
                    "shortIntro": k.shortIntro,
                    "time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(key.time)),
                    "score": key.score,
                    "queTitle": key.queTitle,
                    "topicid": key.topicid,
                    "delete": key.delete
                })
                break
    l=len(answered)
    print(answered)
    for i in range(0,l-1):
        index=i
        for j in range(i+1,l):
            if answered[index]["like"]<answered[j]["like"]:
                index=j
        answered[i],answered[index]=answered[index],answered[i]
    #answered = answered[::-1]
    for key in answered:
        with open("C://Users//梅西//Desktop//forserver//answer//" + str(key['id']) + ".txt", "r+") as f:
            h = f.read()
        answered[count]["content"] = h
        count = count + 1
    return render_template('/homelike.html',user=user,myid=session["uid"],temptopic=temptopic,answered=answered,username=username,uid=uid,users=users)
@bhome.route('/home/com')
def homecom():
    uid=session["uid"]
    user=[]
    temptopic=[]
    users=models.user.query.all()
    temptopics=models.tempTopic.query.all()
    for key in users:
        if key.id==uid:
            user=key
    for key in temptopics:
        flag0="0"
        if models.tempTopicSupport.query.filter_by(uid=uid,temptopicid=key.id).first():
            flag0="1"
        temptopic.append({
            "id":key.id,
            "uid":key.uid,
            "topic":key.topic,
            "isupport":flag0,
            "topicIntro":key.topicIntro,
            "support":key.support,
            "time": time.strftime("%m-%d %H:%M:%S", time.localtime(key.time))
        })
    temptopic=temptopic[::-1]
    answers=models.answer.query.all()
    answercontent = []
    answered = []
    uid = session['uid']
    user = models.user.query.filter_by(id=uid).first()
    username = user.account
    users = models.user.query.all()
    count = 0
    for key in answers:
        for k in users:
            if k.id == key.uid:
                flag = "0"
                flag2 = "0"
                if models.ansLike.query.filter_by(uid=uid, ansid=key.id).first():
                    flag = "1"
                if models.ansStar.query.filter_by(uid=uid, ansid=key.id).first():
                    print("查到")
                    flag2 = "1"
                answered.append({
                    "id": key.id,
                    "qid": key.qid,
                    "like": key.like,
                    "ilike": flag,
                    "istar": flag2,
                    "comCount": key.comCount,
                    "uid": key.uid,
                    "account": k.account,
                    "shortIntro": k.shortIntro,
                    "time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(key.time)),
                    "score": key.score,
                    "queTitle": key.queTitle,
                    "topicid": key.topicid,
                    "delete": key.delete
                })
                break
    l=len(answered)
    print(answered)
    for i in range(0,l-1):
        index=i
        for j in range(i+1,l):
            if answered[index]["comCount"]<answered[j]["comCount"]:
                index=j
        answered[i],answered[index]=answered[index],answered[i]
    # print(answered)
    # answered = answered[::-1]
    for key in answered:
        with open("C://Users//梅西//Desktop//forserver//answer//" + str(key['id']) + ".txt", "r+") as f:
            h = f.read()
        answered[count]["content"] = h
        count = count + 1
    return render_template('/homecom.html',user=user,myid=session["uid"],temptopic=temptopic,answered=answered,username=username,uid=uid,users=users)

@bhome.route('/home/applyingtopic',methods=['GET','POST'])
def applyingtopic():
    thistime=int(time.time())
    req=request.get_json()
    topic=req["topic"]
    topicintro=req["topicintro"]
    uid=session["uid"]
    if models.tempTopic.query.filter_by(topic=topic).first():
        return json.dumps({"msg":"existing"})
    else:
        temptopics=models.tempTopic.query.all()
        maxid=temptopics[len(temptopics)-1].id+1
        temptopic=models.tempTopic()
        temptopic.id=maxid
        temptopic.topic=topic
        temptopic.uid=uid
        temptopic.topicIntro=topicintro
        temptopic.support=0
        temptopic.time=thistime
        db.session.add(temptopic)
        db.session.commit()
        return json.dumps({"msg":"good"})
#首页支持话题申请
@bhome.route('/home/supporting',methods=['GET','POST'])
def supporting():
    thistime=int(time.time())
    req=request.get_json()
    flag=req["flag"]
    temptopicid=req["temptopicid"]
    uid=session["uid"]
    #flag=0要支持
    if flag=="0":
        temptopicsupport=models.tempTopicSupport()
        temptopicsupports=models.tempTopicSupport.query.all()
        maxid=temptopicsupports[len(temptopicsupports)-1].id+1
        temptopicsupport.id=maxid
        temptopicsupport.uid=uid
        temptopicsupport.temptopicid=temptopicid
        db.session.add(temptopicsupport)
        db.session.commit()
        temptopic=models.tempTopic.query.filter_by(id=temptopicid).first()
        if temptopic:
            if temptopic.support==9:
                topic=models.topic()
                topics=models.topic.query.all()
                maxid=topics[len(topics)-1].id+1
                topic.id=maxid
                topic.topic=temptopic.topic
                topic.starCount=0
                topic.time=thistime
                topic.topicIntro=temptopic.topicIntro
                topic.queCount=0
                topic.picture=0
                db.session.add(topic)
                db.session.commit()
                db.session.delete(temptopic)
                db.session.commit()
                return json.dumps({"msg":"finished"})
            elif temptopic.support!=9:
                temptopic.support=temptopic.support+1
                db.session.commit()
                return json.dumps({"msg":"supported"})
    elif flag=="1":
        temptopicsupport=models.tempTopicSupport.query.filter_by(uid=uid,temptopicid=temptopicid).first()
        temptopicsupport.uid=0
        db.session.commit()
        temptopic = models.tempTopic.query.filter_by(id=temptopicid).first()
        temptopic.support=temptopic.support-1
        db.session.commit()
        return json.dumps({"msg":"canceled"})

@bhome.route('/homeadmin')
def homeadmin():
    uid = session["uid"]
    users = models.user.query.all()
    user = []
    for key in users:
        user.append({
            "id": key.id,
            "account": key.account,
            "time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(key.time)),
            "shortIntro": key.shortIntro,
            "grade": key.grade,
            "major": key.major,
            "sex": key.sex
        })
    return render_template('/homeadmin/homeadmin.html', users=user)
@bhome.route('/homeadmintopic')
def homeadmintopic():
    uid = session["uid"]
    users = models.user.query.all()
    topics=models.topic.query.all()
    topic=[]
    for key in topics:
        topic.append({
            "id": key.id,
            "topic": key.topic,
            "time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(key.time)),
            "topicIntro": key.topicIntro,
            "queCount": key.queCount,
            "starCount": key.starCount
        })
    return render_template('/homeadmin/homeadmintopic.html', topic=topic)
@bhome.route('/homeadminquestion')
def homeadminquestion():
    uid = session["uid"]
    topics = models.topic.query.all()
    questions=models.question.query.all()
    question=[]
    for key in questions:
        for say in topics:
            if say.id==key.reltopicid:
                question.append({
                    "id": key.id,
                    "question": key.question,
                    "like":key.like,
                    "ansCount":key.ansCount,
                    "uid":key.uid,
                    "time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(key.time)),
                    "reltopicid":key.reltopicid,
                    "topic":say.topic,
                    "followerCount":key.followerCount
                })
    return render_template('/homeadmin/homeadminquestion.html', question=question)
@bhome.route('/homeadminanswer')
def homeadminanswer():
    uid = session["uid"]
    users = models.user.query.all()
    answers=models.answer.query.all()
    answer=[]
    for key in answers:
        for say in users:
            if key.uid==say.id:
                topic=models.topic.query.filter_by(id=key.topicid).first()
                answer.append({
                    "id":key.id,
                    "qid":key.qid,
                    "like":key.like,
                    "time":time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(key.time)),
                    "queTitle":key.queTitle,
                    "topicid":key.topicid,
                    "topic":topic,
                    "account":say.account,
                    "uid":key.uid,
                    "delete":key.delete
                })
    count=0
    for key in answer:
        with open("C://Users//梅西//Desktop//forserver//answer//"+str(key['id'])+".txt","r+") as f:
            h=f.read()
        answer[count]["content"]=h
        count=count+1
    return render_template('/homeadmin/homeadminanswer.html', answer=answer)
@bhome.route('/homeadmincomment')
def homeadmincomment():
    uid = session["uid"]
    topics = models.topic.query.all()
    users=models.user.query.all()
    comments=models.ansComment.query.all()
    comment=[]
    for key in comments:
        if key.delete==1:
            for say in users:
                if key.uid==say.id:
                    comment.append({
                        "id":key.id,
                        "uid":key.uid,
                        "account":say.account,
                        "content":key.content,
                        "time":time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(key.time)),
                        "delete":key.delete
                    })
    for key in comments:
        if key.delete==0:
            for say in users:
                if key.uid==say.id:
                    comment.append({
                        "id":key.id,
                        "uid":key.uid,
                        "account":say.account,
                        "content":key.content,
                        "time":time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(key.time)),
                        "delete":key.delete
                    })
    return render_template('/homeadmin/homeadmincomment.html', comment=comment)
@bhome.route('/homeadmin/createtopic',methods=['GET','POST'])
def homeadmincreatetopic():
    thistime=int(time.time())
    req=request.get_json()
    topic=req["topic"]
    topicIntro=req["topicintro"]
    if models.topic.query.filter_by(topic=topic).first():
        return json.dumps({"msg":"existed"})
    else:
        topics=models.topic.query.all()
        maxid=topics[len(topics)-1].id+1
        to=models.topic()
        to.id=maxid
        to.topic=topic
        to.starCount=0
        to.time=thistime
        to.topicIntro=topicIntro
        to.queCount=0
        to.picture=0
        db.session.add(to)
        db.session.commit()
        return json.dumps({"msg":"good"})