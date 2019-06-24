from flask import Flask, session, request
import time,datetime
from app import db, models,app
from flask import Flask, session, request,render_template,url_for
from flask import Blueprint
import json
import time

btopic=Blueprint('btopic', __name__)

@btopic.route('/topic/<topicid>/hotanswer')
def test(topicid):
    answercontent = []
    thistopic = models.topic.query.filter_by(id=topicid).first()
    sql = "select *  from answer where topicid="+topicid
    answer = list()
    answered=[]
    answer = db.session.execute(sql)
    uid =session['uid']
    user=models.user.query.filter_by(id=uid).first()
    username=user.account
    users=models.user.query.all()
    count=0
    for key in answer:
        for k in users:
            if k.id==key.uid:
                flag = "0"
                flag2="0"
                if models.ansLike.query.filter_by(uid=uid, ansid=key.id).first():
                    flag= "1"
                if models.ansStar.query.filter_by(uid=uid,ansid=key.id).first():
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
    print(answered)
    answered=answered[::-1]
    # for i in range(0,len(answered)):
    #     print(answered[i]['id'])
    # for key in answered:
    #     print(key['uid'])
    for key in answered:
        with open("C://Users//梅西//Desktop//forserver//answer//"+str(key['id'])+".txt","r+") as f:
            h=f.read()
        answered[count]["content"]=h
        count=count+1
    topicstar = models.topicStar.query.filter_by(uid=uid,topicid=topicid).first()
    thisstar=False
    if topicstar:
        thisstar=True
    print(thisstar)
    print(str(uid)+"+"+str(topicid))
    return render_template('/topic.html', title='话题',thisstar=thisstar,myid=session["uid"],username=username,uid=uid,users=users,topicid=topicid,thistopic=thistopic,answered=answered,answercontent=answercontent)

@btopic.route('/topic/<topicid>/question',methods=['GET','POST'])
def topicquestion(topicid):
    answercontent = []
    thistopic = models.topic.query.filter_by(id=topicid).first()
    sql = "select *  from question where reltopicid="+topicid
    answer = list()
    question=[]
    question0 = db.session.execute(sql)
    uid =session['uid']
    user=models.user.query.filter_by(id=uid).first()
    username=user.account
    users=models.user.query.all()
    count=0
    for key in question0:
        flag = "0"
        flag2="0"
        if models.queLike.query.filter_by(uid=uid, queid=key.id).first():
            print("查到")
            flag = "1"
        if models.queStar.query.filter_by(uid=uid,queid=key.id).first():
            flag2="1"
        question.append({
            "id": key.id,
            "question": key.question,
            "like": key.like,
            "ilike":flag,
            "istar":flag2,
            "ansCount": key.ansCount,
            "uid": key.uid,
            "time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(key.time)),
            "score": key.score,
            "watch":key.watch,
            "reltopicid": key.reltopicid,
            "followerCount":key.followerCount,
            "queContent":key.queContent,
            "delete": key.delete
        })

    print(question)
    question=question[::-1]
    topicstar = models.topicStar.query.filter_by(uid=uid,topicid=topicid).first()
    thisstar=False
    if topicstar:
        thisstar=True
    # print(thisstar)
    # print(str(uid)+"+"+str(topicid))
    return render_template('/topicquestion.html',title='话题',myid=session["uid"],thisstar=thisstar,username=username,uid=uid,users=users,topicid=topicid,thistopic=thistopic,question=question)

@btopic.route('/topic/star',methods=['GET','POST'])
def staringtopic():
    req=request.get_json()
    flag=req["flag"]
    topicid=int(req["topicid"])
    #flag=1进行关注话题
    topictitle=models.topic.query.filter_by(id=topicid).first()
    title=topictitle.topic
    print(title)
    alltopicstar=models.topicStar.query.all()
    maxid=alltopicstar[len(alltopicstar)-1].id+1
    uid=session['uid']
    if flag=='1':
        topicstar=models.topicStar()
        topicstar.id=maxid
        topicstar.uid=uid
        topicstar.topicid=topicid
        topicstar.topic=title
        db.session.add(topicstar)
        db.session.commit()
        thistopic=models.topic.query.filter_by(id=topicid).first()
        thistopic.starCount=thistopic.starCount+1
        db.session.commit()
        return json.dumps({"msg":"starok"})
    elif flag=="0":
        thistopic=models.topic.query.filter_by(id=topicid).first()
        thistopic.starCount=thistopic.starCount-1
        topicstar=models.topicStar.query.filter_by(uid=uid,topicid=topicid).first()
        if topicstar:
            topicstar.uid = 0
        db.session.commit()
        return json.dumps({"msg":"cancelok"})
@btopic.route('/answer/star', methods=['GET', 'POST'])
def answerstar():
    req=request.get_json()
    ansid=req["ansid"]
    flag=req["flag"]
    uid=session["uid"]
    # flag==0要收藏
    if flag=="0":
        ansstarall=models.ansStar.query.all()
        maxid=ansstarall[len(ansstarall)-1].id+1
        ansstar=models.ansStar()
        ansstar.id=maxid
        ansstar.uid=uid
        ansstar.ansid=ansid
        db.session.add(ansstar)
        db.session.commit()
        return json.dumps({"msg":"stared"})
    elif flag=="1":
        ansstar=models.ansStar.query.filter_by(uid=uid,ansid=ansid).first()
        if ansstar:
            ansstar.uid=0
        db.session.commit()
        return json.dumps({"msg":"canceled"})
@btopic.route('/answer/questar', methods=['GET', 'POST'])
def answerquestar():
    req=request.get_json()
    flag=req["flag"]
    queid=req["queid"]
    uid=session["uid"]
    #flag==0要收藏
    if flag=="0":
        questars=models.queStar.query.all()
        maxid=questars[len(questars)-1].id+1
        questar=models.queStar()
        questar.id=maxid
        questar.uid=uid
        questar.queid=queid
        db.session.add(questar)
        db.session.commit()
        return json.dumps({"msg":"stared"})
    elif flag=="1":
        questar=models.queStar.query.filter_by(uid=uid,queid=queid).first()
        if questar:
            questar.uid=0
        db.session.commit()
    ansstarall=models.ansStar.query.all()
    maxid=ansstarall[len(ansstarall)-1].id+1
    return json.dumps({"msg":"canceled"})
@btopic.route('/answer/like', methods=['GET', 'POST'])
def answerlike():
    req=request.get_json()
    ansid=req["ansid"]
    flag=req["flag"]
    uid=session["uid"]
    likes=models.ansLike.query.all()
    maxid=likes[len(likes)-1].id+1
    #flag=0要点赞
    if flag=="0":
        like=models.ansLike()
        like.id=maxid
        like.uid=uid
        like.ansid=ansid
        db.session.add(like)
        db.session.commit()
        answer=models.answer.query.filter_by(id=ansid).first()
        if answer:
            answer.like=answer.like + 1
        db.session.commit()
        return json.dumps({"msg":"liked"})
    elif flag=="1":
        cancellike=models.ansLike.query.filter_by(uid=uid,ansid=ansid).first()
        if cancellike:
            cancellike.uid=0
        db.session.commit()
        answer = models.answer.query.filter_by(id=ansid).first()
        if answer:
            answer.like = answer.like - 1
        db.session.commit()
        return json.dumps({"msg":"canceled"})
#topic下待回答问题的like
@btopic.route('/answer/quelike', methods=['GET', 'POST'])
def answerquelike():
    req=request.get_json()
    queid=req["queid"]
    flag=req["flag"]
    uid=session["uid"]
    likes=models.queLike.query.all()
    maxid=likes[len(likes)-1].id+1
    #flag=0要点赞
    if flag=="0":
        like=models.queLike()
        like.id=maxid
        like.uid=uid
        like.queid=queid
        db.session.add(like)
        db.session.commit()
        question=models.question.query.filter_by(id=queid).first()
        if question:
            question.like=question.like + 1
        db.session.commit()
        return json.dumps({"msg":"liked"})
    elif flag=="1":
        cancellike=models.queLike.query.filter_by(uid=uid,queid=queid).first()
        if cancellike:
            cancellike.uid=0
        db.session.commit()
        question = models.answer.query.filter_by(id=queid).first()
        if question:
            question.like = question.like - 1
        db.session.commit()
        return json.dumps({"msg":"canceled"})


