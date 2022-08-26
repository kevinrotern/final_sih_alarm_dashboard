
from flask import Flask, request, render_template
import pymongo
import json
import requests
import winsound
from twilio.rest import Client 
from twilio.twiml.voice_response import VoiceResponse, Say

app = Flask(__name__) 
@app.route("/")
def data():
    lid=lastid()
    len=currentid()
    len1=int(len)
    url = "http://13.235.103.138:3000/senders"
    url1= "http://13.235.103.138:3000/getMessageById"

    for count in range(lid+1,len1+1):
     x=str(count)
     x1='id='+x

     payload=x1
     print("-----------"+x1+"-----------------------------------------------")
     headers = {'Content-Type': 'application/x-www-form-urlencoded'}
     response = requests.request("GET", url, headers=headers, data=payload)
     data = json.loads(response.text)
     response1 = requests.request("GET", url1, headers=headers, data=payload)
     data1 = json.loads(response1.text)
     str1=data1['message']['message']
     print(str1)
     #print the type of data variable
     a1=data['data']['senders']
     #-------------------------------------------
     print(str1)
     if 'kill' in str1:
       sus="True"
       uval={'_id':x1,'origin1':a1,'message':str1,'suspect':sus}
       row.insert_one(uval)
       sus=""
       suscall(str1)
     elif 'shoot' in str1:
       sus="True"
       uval={'_id':x1,'origin1':a1,'message':str1,'suspect':sus}
       row.insert_one(uval)
       sus=""
       suscall(str1)
     elif 'murder' in str1:
       sus="True"
       uval={'_id':x1,'origin1':a1,'message':str1,'suspect':sus}
       row.insert_one(uval)
       sus=""
       suscall(str1)
     elif 'kidnap' in str1:
      sus="True"
      uval={'_id':x1,'origin1':a1,'message':str1,'suspect':sus}
      row.insert_one(uval)
      sus=""
      suscall(str1)
     elif 'bomb' in str1:
       sus="True"
       uval={'_id':x1,'origin1':a1,'message':str1,'suspect':sus}
       row.insert_one(uval)
       sus=""
       suscall(str1) 
     else:
       sus="False"
       uval={'_id':x1,'origin1':a1,'message':str1,'suspect':sus}
       row.insert_one(uval)
       sus=""

     #-------------------------------------------
     for f in a1:
      print(f)
    return render_template('dashboard.html',usdata=row.find(),mydoc=row.count_documents({}))
 
def lastid():
  x=row.find()
  y1=""
  for y in x:
   y1=y['_id']
  #print("-------------------------------")
  print(str(y1))
  y2=y1[3:]
  y3=int(y2)
  print(type(y3))
  return y3

def suscall(str1):
     print("Yes, 'S Eductation' found in List : ",str1)
     winsound.Beep(440, 500)
    #------------------------------------
    #------------------------0
     account_sid = "ACb925b17c0f27b807f9d4985da6667ba6"
     auth_token = "66196ec63d9d1db1801eb7e2e7f13329" 
     client = Client(account_sid, auth_token) 
     call = client.calls.create( to="+919967294776", from_="+18775613610", url="http://demo.twilio.com/docs/voice.xml" )
     print(call.sid)   

def currentid():
 url = "http://13.235.103.138:3000/total"
 payload={}
 headers = {}
 response = requests.request("GET", url, headers=headers, data=payload)
 data1 = json.loads(response.text)
 str12=data1['messages']
 print(str12)
 return str12

def mssg(): 
 url = "http://13.235.103.138:3000/getMessageById"
 payload='id=66'
 headers = {'Content-Type': 'application/x-www-form-urlencoded'}
 response = requests.request("GET", url, headers=headers, data=payload)
 print(response.text)
 data1 = json.loads(response.text)
 return data1
    
if __name__ == "__main__":
 client= pymongo.MongoClient("mongodb+srv://kevinrotern:jayesh@cluster0.h7nnxmo.mongodb.net/test")
 db= client['blockchain_data']
 row=db['sus']

 app.run(debug=True)