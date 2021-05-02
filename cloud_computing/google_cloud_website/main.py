# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_cloudsql_mysql]
import os
from flask import json, Response,jsonify,request
from flask import Flask
import pymysql
import json
from flask_cors import CORS, cross_origin
from google.cloud import storage
import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')
CLOUD_STORAGE_BUCKET = os.environ['CLOUD_STORAGE_BUCKET']

app = Flask(__name__)

CORS(app)

def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )

@app.route('/upload', methods=['POST'])
def upload():
    """Process the uploaded file and upload it to Google Cloud Storage."""
    uploaded_file = request.files.get('file')

    if not uploaded_file:
        return 'No file uploaded.', 400

    # Create a Cloud Storage client.
    gcs = storage.Client()

    # Get the bucket that the file will be uploaded to.
    bucket = gcs.get_bucket(CLOUD_STORAGE_BUCKET)

    # Create a new blob and upload the file's content.
    blob = bucket.blob(uploaded_file.filename)

    blob.upload_from_string(
        uploaded_file.read(),
        content_type=uploaded_file.content_type
    )
    if os.environ.get('GAE_ENV') == 'standard':
        unix_socket = '/cloudsql/{}'.format(db_connection_name)
        cnx = pymysql.connect(user=db_user, password=db_password,unix_socket=unix_socket, db=db_name)
    else:
        host = '127.0.0.1'
        cnx = pymysql.connect(user=db_user, password=db_password,host=host, db=db_name)
    with cnx.cursor() as cursor:
        # The public URL can be used to directly access the uploaded file via HTTP.
        typ = request.form.get("type")
        if typ == "food":
            image_url=  blob.public_url
            user_id = request.form.get("user_id")
            comments = request.form.get("comments")
            price = request.form.get("price")
            cuisine = request.form.get("cuisine")
            quantity = request.form.get("quantity")
        
            cursor.execute("Insert into food (id,user_id,comments,price,cuisine,image_url,quantity) Values (NULL,%s,%s,%s,%s,%s,%s)",(user_id,comments,price,cuisine,image_url,quantity))
            cnx.commit()
            cnx.close()
            
            return custom_response("Success",200)
        elif typ =="art":
            image_url=  blob.public_url
            user_id = request.form.get("user_id")
            comments = request.form.get("comments")
            price = request.form.get("price")
            size = request.form.get("size_of_art")
            weight = request.form.get("weight")
            quantity = request.form.get("quantity")
        
            cursor.execute("Insert into art (id,user_id,comments,price,size_of_art,weight, image_url,quantity) Values (NULL,%s,%s,%s,%s,%s,%s, %s)",(user_id,comments,price,size, weight,image_url,quantity))
            cnx.commit()
            cnx.close()
            return custom_response("Success",200)
        else:
            return custom_response("error in form",400)
            

@app.route('/getart', methods=['GET'])
def getart():
    if os.environ.get('GAE_ENV') == 'standard':
        unix_socket = '/cloudsql/{}'.format(db_connection_name)
        cnx = pymysql.connect(user=db_user, password=db_password,unix_socket=unix_socket, db=db_name)
    else:
        host = '127.0.0.1'
        cnx = pymysql.connect(user=db_user, password=db_password,host=host, db=db_name)
    with cnx.cursor() as cursor:
        cursor.execute('Select * from art where quantity >0 ;')
        result = cursor.fetchall()
       # return custom_response(result,200)
        count=1
        rec={}
        for res in result:
            cursor.execute("select address from user,art where user.id=art.user_id and art.user_id=" + str(res[1]))
            add=cursor.fetchone()
            #print(add[0])
            temp={'image':res[6],
                    'cost':res[3],
                    'comment' : res[2],
                    'type_of_art':res[2],
                    'quantity': res[7],
		    'weight': res[5],
		     'size_of_art':res[4],
                    'address': add[0],
                    'id':res[0]
                   }
            rec[count]=temp
            count+=1
        return custom_response(rec,"200") 

@app.route('/upload_food_history', methods=['POST'])
def upload_food_history():
    if os.environ.get('GAE_ENV') == 'standard':
        unix_socket = '/cloudsql/{}'.format(db_connection_name)
        cnx = pymysql.connect(user=db_user, password=db_password,unix_socket=unix_socket, db=db_name)
    else:
        host = '127.0.0.1'
        cnx = pymysql.connect(user=db_user, password=db_password,host=host, db=db_name)
    with cnx.cursor() as cursor:
        recs=request.get_json()
        usr_id = recs['user_id']
        cursor.execute('Select * from food where user_id = '+ str(usr_id)+ ";")
        result = cursor.fetchall()
       # return custom_response(result,200)
        count=1
        rec={}
        for res in result:
            cursor.execute("select address from user,food where user.id=food.user_id and food.user_id=" + str(usr_id))
            add=cursor.fetchone()
            #print(add[0])
            temp={'image':res[5],
                    'cost':res[3],
                    'comment' : res[2],
                    'cuisine':res[4],
                    'quantity': res[6],
                    'address': add[0],
                    'id':res[0]
                   }
            rec[count]=temp
            count+=1
        return custom_response(rec,"200") 
        
@app.route('/upload_art_history', methods=['POST'])
def upload_art_history():
    if os.environ.get('GAE_ENV') == 'standard':
        unix_socket = '/cloudsql/{}'.format(db_connection_name)
        cnx = pymysql.connect(user=db_user, password=db_password,unix_socket=unix_socket, db=db_name)
    else:
        host = '127.0.0.1'
        cnx = pymysql.connect(user=db_user, password=db_password,host=host, db=db_name)
    with cnx.cursor() as cursor:
        recs=request.get_json()
        usr_id = recs['user_id']
        cursor.execute('Select * from art where user_id = ' + str(usr_id) + ";")
        result = cursor.fetchall()
       # return custom_response(result,200)
        count=1
        rec={}
        for res in result:
            cursor.execute("select address from user,art where user.id=art.user_id and art.user_id=" + str(usr_id))
            add=cursor.fetchone()
            #print(add[0])
            temp={'image':res[6],
                    'cost':res[3],
                    'comment' : res[2],
                    'type_of_art':res[2],
                    'quantity': res[7],
		    'weight': res[5],
		     'size_of_art':res[4],
                     'address' : add[0],
                    'id':res[0]
                   }
            rec[count]=temp
            count+=1
        print(rec)    
        return custom_response(rec,"200")




    
@app.route('/getfood', methods=['GET'])
def getfood():
    if os.environ.get('GAE_ENV') == 'standard':
        unix_socket = '/cloudsql/{}'.format(db_connection_name)
        cnx = pymysql.connect(user=db_user, password=db_password,unix_socket=unix_socket, db=db_name)
    else:
        host = '127.0.0.1'
        cnx = pymysql.connect(user=db_user, password=db_password,host=host, db=db_name)
    with cnx.cursor() as cursor:
        cursor.execute('Select * from food where quantity >0 ;')
        result = cursor.fetchall()
       # return custom_response(result,200)
        count=1
        rec={}
        for res in result:
            cursor.execute("select address from user,food where user.id=food.user_id and food.user_id=" + str(res[1]))
            add=cursor.fetchone()
            #print(add[0])
            temp={'image':res[5],
                    'cost':res[3],
                    'comment' : res[2],
                    'cuisine':res[4],
                    'quantity': res[6],
                    'address': add[0],
                    'id':res[0]
                   }
            rec[count]=temp
            count+=1
        return custom_response(rec,"200") 

@app.route('/confirm', methods=['POST'])
def confirm():
    if os.environ.get('GAE_ENV') == 'standard':
        unix_socket = '/cloudsql/{}'.format(db_connection_name)
        cnx = pymysql.connect(user=db_user, password=db_password,unix_socket=unix_socket, db=db_name)
    else:
        host = '127.0.0.1'
        cnx = pymysql.connect(user=db_user, password=db_password,host=host, db=db_name)
    with cnx.cursor() as cursor:
        recs=request.get_json()
        item=recs['type']
        quant = recs['quant']
        cust_id = recs['cust_id']
        item_id = recs['id']

        if item =="food":
            cursor.execute("Select * from food where id="+str(recs['id'])+";")
            ans=cursor.fetchall()
            if int(quant) > int(ans[0][6]):
                return custom_response("Please enter qppropiate quanrity",400)
            cursor.execute("Update food set quantity=quantity- "+ quant+" where id="+str(recs['id'])+";")
            cursor.execute("Select * from food where id="+str(recs['id'])+";")
            result=cursor.fetchall()
            image_url=result[0][5]
            comment=result[0][2]
            userid=result[0][1]
            cursor.execute("Select * from user where id ="+ str(userid)+";")
            rex=cursor.fetchall()
            address=rex[0][6]
            cursor.execute("select * from user where id = " +str(cust_id)+ ";")
            ress = cursor.fetchall()

            cursor.execute("insert into transaction (id,user_id,item_id,type,quantity,image_url,comments,address) values(NULL, %s, %s, %s, %s,%s,%s,%s)", (cust_id, item_id,item,quant,image_url,comment,address)) 
            cnx.commit()
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("sinhaswarnim1@gmail.com", "QWERTY1234!")
            message = "Dear Customer, " + "\n" +" Greetings from Inhouse Enterpreneur." + "\n" + " Someone has ordered your itme. . Persons phone number is "+str(result[0][5])+ " Please contact them if needed"
            s.sendmail("sinhaswarnim1@gmail.com", rex[0][2], message)
            msg="Dear Customer , "+"\n"+"Greeting from In house Entrepreneur."+"\n"+"You order has been placed . Please contact Mr/Mrs "+ str(ress[0][1])+". Comtact him on "+str(ress[0][5])+"Thanks a lot"
            s.sendmail("sinhaswarnim1@gmail.com",ress[0][2],msg)
            s.quit()
            return custom_response("Success",200)
        elif item=="art":
            cursor.execute("Select * from art where id="+str(recs['id'])+";")
            ans=cursor.fetchall()
            if int(quant)>int(ans[0][7]):
                return custom_response("Cant order",400 )
            cursor.execute("Update art set quantity=quantity- "+ quant+" where id="+str(recs['id'])+";")
            cursor.execute("Select * from art where id="+str(recs['id'])+";")
            result=cursor.fetchall()
            image_url=result[0][6]
            comment=result[0][2]
            userid=result[0][1]
            cursor.execute("Select * from user where id ="+ str(userid)+";")
            rex=cursor.fetchall()
            address=rex[0][6]
            cursor.execute("select * from user where id = " +str(cust_id)+ ";")
            ress = cursor.fetchall()
            cursor.execute("insert into transaction (id,user_id,item_id,type,quantity,image_url,comments,address) values(NULL, %s, %s, %s, %s,%s,%s,%s)", (cust_id, item_id,item,quant,image_url,comment,address)) 
            cnx.commit()
            
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("sinhaswarnim1@gmail.com", "QWERTY1234!")
            message = "Dear Customer, " + "\n" +" Greetings from Inhouse Enterpreneur." + "\n" + " Someone has ordered your itme.Person phone number is  "+ str(rex[0][1])+ ". Persons phone number is "+str(rex[0][5])+ " Please contact them if needed"
            s.sendmail("sinhaswarnim1@gmail.com", rex[0][2], message)
            msg="Dear Customer , "+"\n"+"Greeting from In house Entrepreneur."+"\n"+"You order has been placed . Please contact Mr/Mrs "+ str(ress[0][1])+". Comtact him on "+str(ress[0][5])+"Thanks a lot"
            s.sendmail("sinhaswarnim1@gmail.com",ress[0][2],msg)
            s.quit()
            return custom_response("Sucess",200)
        else:
            return custom_response("Error",400)  


@app.route('/history', methods=['POST'])
def history():
    if os.environ.get('GAE_ENV') == 'standard':
        unix_socket = '/cloudsql/{}'.format(db_connection_name)
        cnx = pymysql.connect(user=db_user, password=db_password,unix_socket=unix_socket, db=db_name)
    else:
        host = '127.0.0.1'
        cnx = pymysql.connect(user=db_user, password=db_password,host=host, db=db_name)
    with cnx.cursor() as cursor:
        recs=request.get_json()
        user_id = recs['user_id']
        cursor.execute('Select * from transaction where user_id = ' + str(user_id)+'; ')
        #user_id = ' + str(recs['user_id']+ ';')
        result = cursor.fetchall()
        count=1
        
        usr_id = recs['user_id']
        rec={}
        for res in result:
            temp={'item_id':res[2],
                    'type':res[3],
                    'trans_id' : res[0],
                    'quantity': res[7],
                    'address':res[5],
                    'image_url':res[4],
                    'comments':res[6] 
                   }
            rec[count]=temp
            count+=1
        return custom_response(rec,"200")


@app.route('/signup', methods=['PUT'])
def signup():
    recs=request.get_json()
    if os.environ.get('GAE_ENV') == 'standard':
        unix_socket = '/cloudsql/{}'.format(db_connection_name)
        cnx = pymysql.connect(user=db_user, password=db_password,unix_socket=unix_socket, db=db_name)
    else:
        host = '127.0.0.1'
        cnx = pymysql.connect(user=db_user, password=db_password,host=host, db=db_name)
    with cnx.cursor() as cursor:
        cursor.execute('Select * from user where username=\''+ str(recs['username'])+ "\';")
        result = cursor.fetchall()
        name=recs['name']
        email=recs['email']
        phone_no=recs['phone_no']
        address=recs['address']
        username=recs['username']
        password=recs['password']
        if not result:
            cursor.execute("Insert into user (id,name,email,username,password,phone_no,address) Values (NULL,%s,%s,%s,%s,%s,%s)",(name,email,username,password,phone_no,address))
            cnx.commit()
            cnx.close()
            #cnx.close()
            return custom_response("Success",201)
        else:
           # cnx.close()
            return custom_response("Username already exist",400)

     

@app.route('/login',methods=['POST'])
def login():
    recs=request.get_json()
    if os.environ.get('GAE_ENV') == 'standard':
        unix_socket = '/cloudsql/{}'.format(db_connection_name)
        cnx = pymysql.connect(user=db_user, password=db_password,unix_socket=unix_socket, db=db_name)
    else:
        host = '127.0.0.1'
        cnx = pymysql.connect(user=db_user, password=db_password,host=host, db=db_name)
    with cnx.cursor() as cursor:
        cursor.execute('Select * from user where username=\''+ str(recs['username'])+ "\' and password=\'" + str(recs['password']) + "\';")
        result = cursor.fetchall()
        if not result:
            cnx.close()
            return custom_response("Failure",400)
        else:
            cnx.close()
            return custom_response(result[0][0],200)
        


@app.route('/')
def main():
    # When deployed to App Engine, the `GAE_ENV` environment variable will be
    # set to `standard`
    if os.environ.get('GAE_ENV') == 'standard':
        # If deployed, use the local socket interface for accessing Cloud SQL
        unix_socket = '/cloudsql/{}'.format(db_connection_name)
        cnx = pymysql.connect(user=db_user, password=db_password,
                              unix_socket=unix_socket, db=db_name)
    else:
        # If running locally, use the TCP connections instead
        # Set up Cloud SQL Proxy (cloud.google.com/sql/docs/mysql/sql-proxy)
        # so that your application can use 127.0.0.1:3306 to connect to your
        # Cloud SQL instance
        host = '127.0.0.1'
        cnx = pymysql.connect(user=db_user, password=db_password,
                              host=host, db=db_name)
    rec=[]
    with cnx.cursor() as cursor:
        cursor.execute('select *  from user;')
        result = cursor.fetchall()
        rec = {"id": result[0][0],"name":result[0][1]}
        
    cnx.close()
    #current_msg="hello"
    return jsonify(rec)
# [END gae_python37_cloudsql_mysql]


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

