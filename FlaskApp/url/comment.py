from flask import Flask, session, request
import time,datetime
from app import db, models,app
from flask_restful import Resource, Api, reqparse, abort
from flask import Flask, session, request,render_template,url_for
from flask_bootstrap import Bootstrap
from flask import Blueprint
import json
import time

bcomment=Blueprint('bcomment', __name__)

@bcomment.route('/comment/answer',methods=['GET','POST'])
def answer():
    thistime=int(time.time())
    data=request.get_json()
    #print("ansid:"+data["ansid"])
    anscomment=models.ansComment.query.filter_by(ansid=data["ansid"]).all()
    users=models.user.query.all()
    #print(anscomment[1].content)
    if anscomment:
        datas=[]
        for key in anscomment:
            for king in users:
                if king.id==key.uid:
                    datas.append({
                        "id":key.id,
                        "uid":key.uid,
                        "account":king.account,
                        "fid":key.fid,
                        "pid":key.pid,
                        "like":key.like,
                        "content":key.content,
                        "time":time.strftime("%m-%d %H:%M:%S",time.localtime(key.time)),
                        "ansid":key.ansid
                    })
        return json.dumps({"msg":"1","data":datas})
    else:
        return json.dumps({"msg":"2","data":{}})
@bcomment.route('/comment/answer/submit',methods=['GET','POST'])
def anscommentsubmit():
    thistime = int(time.time())
    #请求参数
    req=request.get_json()
    print(req["content"])
    #获取anscomment最大id
    uid=session["uid"]
    myname=''
    users=models.user.query.all()
    for key in users:
        if key.id==uid:
            myname=key.account
    print("uid:"+str(uid))
    fid=0
    anscomment=models.ansComment.query.all()
    for key in anscomment:
        if key.id==req["pid"]:
            fid=key.uid
    maxid=anscomment[len(anscomment)-1].id
    maxid=maxid+1
    insertcomment=models.ansComment()
    insertcomment.id=maxid
    insertcomment.like=0
    insertcomment.time=thistime
    insertcomment.delete=0
    insertcomment.content=req["content"]
    insertcomment.pid=req["pid"]
    insertcomment.uid=uid
    insertcomment.fid=fid
    insertcomment.ansid=req["ansid"]
    db.session.add(insertcomment)
    db.session.commit()
    count=0
    for key in anscomment:
        if key.id==req["pid"]:
            break
        count=count+1
    anss=models.answer.query.filter_by(id=req["ansid"]).first()
    if anss:
        anss.comCount=anss.comCount+1
    db.session.commit()
    return json.dumps({"msg":"good","count":count,"myname":myname,"myuid":uid,"content":req["content"],"time":thistime,"data":{"id":"1"}})
@bcomment.route('/comment/answer/tipoff',methods=['GET','POST'])
def anscommenttipoff():
    data=request.get_json()
    anscomment=models.ansComment.query.filter_by(id=data["anscomment"]).first()
    anscomment.delete=1
    db.session.commit()
    return json.dumps({"msg":"good"})