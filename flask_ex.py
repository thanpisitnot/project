import os
from flask import Flask, render_template, jsonify, request, json, redirect, url_for, session,flash
from flask_cors import CORS
from werkzeug import utils
import cx_Oracle

os.environ["NLS_LANG"] = ".UTF8"
UPLOAD_FOLDER = './dist/static/image/tour_picture'
app = Flask(__name__,
            static_folder="./static",
            template_folder="./templates")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = '1234'
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

USER = 'tkivieemee'
PASS = 'mee0886203137'
# USER = 'tkivieemee2'
# PASS = 'mee0886203137'
DB_URL = '203.158.131.65:1521/usfm'
# DB_URL = '10.10.100.65:1521/usfm'

# con = cx_Oracle.connect('pythonhol/welcome@127.0.0.1/orcl')
# print(con.version)


@app.route('/userinfo')
def userinfo():
    try:
        con = cx_Oracle.connect(session['username'] + '/' + session['password'] + '@' + DB_URL)
        cur = con.cursor()
        sql = "select ID,Name,Surname,username,address," \
              "depart,work_hours from user_table"
        cur.execute(sql)
        rows = cur.fetchall()
        data = {}
        for row in rows:
            data['ID'] = row[0]
            data['NAME'] = row[1]
            data['SURNAME'] = row[2]
            data['USERNAME'] = row[3]
            data['ADDRESS'] = row[4]
            data['DEPART'] = row[5]
            data['WORK_HOURS'] = row[6]
        return render_template('userinfo.html', data=data, usernavbar=session['username'], usertype=session['depart'])
    except:
        redirect(url_for('m'))
    finally:
        cur.close()
        con.close()


@app.route('/admininfo')
def admininfo():
    return render_template('admininfo.html', usernavbar=session['username'], usertype=session['depart'])


@app.route('/nnews/<ID>')
def nnews(ID):
    try:
        con = cx_Oracle.connect(session['username'] + '/' + session['password'] + '@' + DB_URL)
        cur = con.cursor()
        sql = " select ID,topic,detail,id_user,type_id,name,surname," \
              " active,username,address,depart,type_name from table_news" \
              " where id = '" + ID + "'"
        print(sql)
        cur.execute(sql)
        rows = cur.fetchall()
        data = {}
        for row in rows:
            data['ID'] = row[0]
            data['TOPIC'] = row[1]
            data['DETAIL'] = row[2]
            data['ID_USER'] = row[3]
            data['TYPE_ID'] = row[4]
            data['NAME'] = row[5]
            data['SURNAME'] = row[6]
            data['ACTIVE'] = row[7]
            data['USERNAME'] = row[8]
            data['ADDRESS'] = row[9]
            data['DEPART'] = row[10]
            data['TYPE_NAME'] = row[11]
        return render_template('nnews.html', data=data, usernavbar=session['username'], usertype=session['depart'])
    except:
        return redirect(url_for('m'))
    finally:
        cur.close()
        con.close()


@app.route('/comdetail/<ID>')
def comdetail(ID):
    try:
        con = cx_Oracle.connect(session['username'] + '/' + session['password'] + '@' + DB_URL)
        cur = con.cursor()
        sql = " select c.id,u.name,u.surname,u.username,u.depart,u.leveltype,c.salary," \
              " c.remuneration, to_char(c.datecompen,'yyyy-MM-DD'), c.work_hours" \
              " from user1 u " \
              " inner join compensation c on u.id = c.id_user" \
              " where c.id = '"+ID+"'"
        print(sql)
        cur.execute(sql)
        rows = cur.fetchall()
        data = {}
        for row in rows:
            data['ID'] = row[0]
            data['NAME'] = row[1]
            data['SURNAME'] = row[2]
            data['USERNAME'] = row[3]
            data['DEPART'] = row[4]
            data['LEVELTYPE'] = row[5]
            data['SALARY'] = row[6]
            data['REMUNERATION'] = row[7]
            data['DATECOMPEN'] = row[8]
            data['WORK_HOURS'] = row[9]
        return render_template('comdetail.html', data=data, usernavbar=session['username'],usertype=session['depart'])
    except:
        return redirect(url_for('m'))
    finally:
        cur.close()
        con.close()


@app.route('/newsdetail/<ID>')
def newsdetail(ID):
    try:
        con = cx_Oracle.connect(session['username'] + '/' + session['password'] + '@' + DB_URL)
        cur = con.cursor()
        sql = " select ID,topic,detail,datenews,ID_USER,type_id" \
              " from news" \
              " where id = '" + ID + "'"
        print(sql)
        cur.execute(sql)
        rows = cur.fetchall()
        data = {}
        for row in rows:
            data['ID'] = row[0]
            data['TOPIC'] = row[1]
            data['DETAIL'] = row[2]
            data['DATENEWS'] = row[3]
            data['ID_USER'] = row[4]
            data['TYPE_ID'] = row[5]
        return render_template('newsdetail.html', data=data, usernavbar=session['username'],usertype=session['depart'])
    except:
        return redirect(url_for('m'))
    finally:
        cur.close()
        con.close()


@app.route('/userdetail/<ID>')
def userdetail(ID):
    try:
        con = cx_Oracle.connect(session['username'] + '/' + session['password'] + '@' + DB_URL)
        cur = con.cursor()
        sql = " select ID,name,surname,active,username,address,depart,leveltype" \
              " from user1" \
              " where id = '" + ID + "'"
        print(sql)
        cur.execute(sql)
        rows = cur.fetchall()
        data = {}
        for row in rows:
            data['ID'] = row[0]
            data['NAME'] = row[1]
            data['SURNAME'] = row[2]
            data['ACTIVE'] = row[3]
            data['USERNAME'] = row[4]
            data['ADDRESS'] = row[5]
            data['DEPART'] = row[6]
            data['LEVELTYPE'] = row[7]
        return render_template('userdetail.html', data=data, usernavbar=session['username'],usertype=session['depart'])
    except:
        return redirect(url_for('m'))
    finally:
        cur.close()
        con.close()


@app.route('/hello1')
def hello1():
    return render_template('blank.html')


@app.route('/listuser')
def listuser():
    try:
        con = cx_Oracle.connect(session['username'] + '/' + session['password'] + '@' + DB_URL)
        cur = con.cursor()
        sql = " select ID,name,surname,active,username," \
              " address,depart,leveltype from user1" \
              " order by 1"

        print(sql)
        cur.execute(sql)
        rows = cur.fetchall()
        return render_template('listuser.html', rows=rows, usernavbar=session['username'],usertype=session['depart'])
    except:
        return redirect(url_for('m'))
    finally:
        cur.close()
        con.close()


@app.route('/updateuser')
def updateuser():
    try:
        con = cx_Oracle.connect(session['username'] + '/' + session['password'] + '@' + DB_URL)
        cur = con.cursor()
        sql = " SELECT id,name,surname,active,username,address," \
              " depart  from user1 "
        print(sql)
        cur.execute(sql)
        rows = cur.fetchall()
        data = {}
        for row in rows:
            data['ID'] = row[0]
            data['NAME'] = row[1]
            data['SURNAME'] = row[2]
            data['ACTIVE'] = row[3]
            data['USERNAME'] = row[4]
            data['ADDRESS'] = row[5]
            data['DEPART'] = row[6]
        return render_template('updateuser.html', data=data, link='/updateuserp', usernavbar=session['username'],usertype=session['depart'])
    except cx_Oracle.DatabaseError as e:
        con.rollback()
        return redirect(url_for('m'))
    finally:
        cur.close()
        con.close()


@app.route('/updateuserp', methods=['POST'])
def updateuserp():
    try:
        con = cx_Oracle.connect(session['username'] + '/' + session['password'] + '@' + DB_URL)
        cur = con.cursor()

        iduser = request.form['iduser']
        name = request.form['name']
        surname = request.form['surname']
        active = request.form['active']
        usern = request.form['usern']
        address = request.form['address']
        depart = request.form['depart']
        sql = " UPDATE user1 " \
              " SET name = '" + name + "' , surname='" + surname + "', username='" + usern + "', active='" + active + "', " \
              " address='" + address + "', depart='" + depart + "' " \
              " WHERE id='" + iduser + "'"
        print(sql)
        cur.execute(sql)
        con.commit()
        return redirect(url_for('userinfo'))
    except cx_Oracle.DatabaseError as e:
        con.rollback()
        return redirect(url_for('m'))
    finally:
        cur.close()
        con.close()


@app.route('/active/<idcom>')
def active(idcom):
    try:
        con = cx_Oracle.connect(session['username'] + '/' + session['password'] + '@' + DB_URL)
        cur = con.cursor()
        sql = "UPDATE user1 SET active = 'yes' WHERE username='" + idcom + "'"
        print(sql)
        cur.execute(sql)
        sql = "ALTER USER " + idcom + " ACCOUNT UNLOCK "
        print(sql)
        cur.execute(sql)
        con.commit()
        return redirect(url_for('listuser'))

    except cx_Oracle.DatabaseError as e:
        con.rollback()
        return redirect(url_for('m'))
    finally:
        cur.close()
        con.close()


@app.route('/inactive/<idcom>')
def inactive(idcom):
    try:
        con = cx_Oracle.connect(session['username'] + '/' + session['password'] + '@' + DB_URL)
        cur = con.cursor()
        sql = "UPDATE user1 SET active = 'no' WHERE username ='" + idcom + "'"
        print(sql)
        cur.execute(sql)
        sql = " ALTER USER " + idcom + " ACCOUNT LOCK "
        print(sql)
        cur.execute(sql)
        con.commit()
        return redirect(url_for('listuser'))
    except cx_Oracle.DatabaseError as e:
        con.rollback()
        return redirect(url_for('m'))
    finally:
        cur.close()
        con.close()


@app.route('/compensation')
def compensation():
    try:
        con = cx_Oracle.connect(session['username'] + '/' + session['password'] + '@' + DB_URL)
        cur = con.cursor()
        sql = " select c.id, u.name,c.salary, c.remuneration, to_char(c.datecompen,'yyyy-MM-DD'), c.work_hours" \
              " from user1 u" \
              " inner join compensation c on u.id = c.id_user"
        print(sql)
        cur.execute(sql)
        rows = cur.fetchall()
        return render_template('compensation.html', rows=rows, usernavbar=session['username'],usertype=session['depart'])
    except:
        return redirect(url_for('m'))
    finally:
        cur.close()
        con.close()


@app.route('/listnews')
def listnews():
    try:
        con = cx_Oracle.connect(session['username'] + '/' + session['password'] + '@' + DB_URL)
        cur = con.cursor()
        sql = " select ID,Topic,detail,to_char(datenews,'yyyy-MON-dd'),ID_user,Type_ID from News"
        print(sql)
        cur.execute(sql)
        rows = cur.fetchall()
        return render_template('listnews.html', rows=rows, usernavbar=session['username'],usertype=session['depart'])
    except:
        return redirect(url_for('m'))
    finally:
        cur.close()
        con.close()


@app.route('/depart')
def depart():
    try:
        con = cx_Oracle.connect(session['username'] + '/' + session['password'] + '@' + DB_URL)
        cur = con.cursor()
        sql = " select ID,Name_Depart from department"
        print(sql)
        cur.execute(sql)
        rows = cur.fetchall()
        return render_template('department.html', rows=rows, usernavbar=session['username'],usertype=session['depart'])
    except:
        return redirect(url_for('m'))
    finally:
        cur.close()
        con.close()


@app.route('/type')
def type():
    try:
        con = cx_Oracle.connect(session['username'] + '/' + session['password'] + '@' + DB_URL)
        cur = con.cursor()
        sql = " select type_ID,type_name from type"
        print(sql)
        cur.execute(sql)
        rows = cur.fetchall()
        return render_template('Type.html', rows=rows, usernavbar=session['username'],usertype=session['depart'])
    except:
        return redirect(url_for('m'))
    finally:
        cur.close()
        con.close()


@app.route('/usertype')
def usertype():
    try:
        con = cx_Oracle.connect(session['username'] + '/' + session['password'] + '@' + DB_URL)
        cur = con.cursor()
        sql = " select usertype,leveltype from usertype"
        print(sql)
        cur.execute(sql)
        rows = cur.fetchall()
        return render_template('usertype.html', rows=rows, usernavbar=session['username'],usertype=session['depart'])
    except:
        return redirect(url_for('m'))
    finally:
        cur.close()
        con.close()


@app.route('/userworking')
def userworking():
    try:
        con = cx_Oracle.connect(session['username'] + '/' + session['password'] + '@' + DB_URL)
        cur = con.cursor()
        sql = " SELECT working_hours.id_row,user1.id,user1.name,user1.username,user1.depart," \
              " TO_CHAR(working_hours.starttime,'yyyy-mm-dd HH24:MI')," \
              " TO_CHAR(working_hours.endtime,'yyyy-mm-dd HH24:MI')" \
              " FROM working_hours" \
              " INNER JOIN user1 ON working_hours.username = user1.username "
        print(sql)
        cur.execute(sql)
        rows = cur.fetchall()
        return render_template('userworking.html', rows=rows, usernavbar=session['username'],usertype=session['depart'])
    except:
        return redirect(url_for('m'))
    finally:
        cur.close()
        con.close()


@app.route('/userworkdetail/<ID>')
def userworkdetail(ID):
    try:
        con = cx_Oracle.connect(session['username'] + '/' + session['password'] + '@' + DB_URL)
        cur = con.cursor()
        sql = " SELECT working_hours.id_row,user1.id,user1.name,user1.username,user1.active,user1.depart,user1.leveltype," \
              " TO_CHAR(working_hours.starttime,'yyyy-mm-dd HH24:MI')," \
              " TO_CHAR(working_hours.endtime,'yyyy-mm-dd HH24:MI')" \
              " FROM working_hours" \
              " INNER JOIN user1 ON working_hours.username = user1.username" \
              " WHERE id_row = '" + ID + "'"
        print(sql)
        cur.execute(sql)
        rows = cur.fetchall()
        data = {}
        for row in rows:
            data['ID_ROW'] = row[0]
            data['ID'] = row[1]
            data['NAME'] = row[2]
            data['USERNAME'] = row[3]
            data['ACTIVE'] = row[4]
            data['DEPART'] = row[5]
            data['LEVELTYPE'] = row[6]
            data['STARTTIME'] = row[7]
            data['ENDTIME'] = row[8]
        return render_template('userworkdetail.html', data=data, usernavbar=session['username'],usertype=session['depart'])
    except:
        return redirect(url_for('m'))
    finally:
        cur.close()
        con.close()


@app.route('/ot')
def ot():
    try:
        con = cx_Oracle.connect(session['username'] + '/' + session['password'] + '@' + DB_URL)
        cur = con.cursor()
        sql = " select name,surname,username,depart,starttime,endtime,work_hours," \
              " remuneration,over_time,total_time,total_compensation" \
              " from ot " \
              " order by starttime desc"
        print(sql)
        cur.execute(sql)
        rows = cur.fetchall()
        return render_template('ot.html', rows=rows, usernavbar=session['username'],usertype=session['depart'])
    except:
        return redirect(url_for('m'))
    finally:
        cur.close()
        con.close()


@app.route('/userxtype')
def userxtype():
    try:
        con = cx_Oracle.connect(session['username'] + '/' + session['password'] + '@' + DB_URL)
        cur = con.cursor()
        sql = " SELECT userxtype.type_id,usertype.usertype,type.type_name" \
              " FROM userxtype" \
              " INNER JOIN usertype ON userxtype.leveltype = usertype.leveltype" \
              " INNER JOIN type ON userxtype.type_id = type.type_id"
        print(sql)
        cur.execute(sql)
        rows = cur.fetchall()
        return render_template('userxtype.html', rows=rows, usernavbar=session['username'],usertype=session['depart'])
    except:
        return redirect(url_for('m'))
    finally:
        cur.close()
        con.close()


@app.route('/insertuxt')
def insertuxt():
    return render_template('insertuserxtype.html', usernavbar=session['username'],usertype=session['depart'])


@app.route('/insertuxtp', methods=['POST'])
def insertuxtp():
    try:
        con = cx_Oracle.connect(session['username'] + '/' + session['password'] + '@' + DB_URL)
        cur = con.cursor()

        userx = request.form['userx']
        typex = request.form['typex']
        sql = " MERGE INTO userxtype a USING ( SELECT '"+typex+"' type_id,'"+userx+"' leveltype" \
              " FROM dual ) " \
              " b ON ( a.type_id = b.type_id" \
              " AND a.leveltype = b.leveltype )" \
              " WHEN NOT MATCHED THEN" \
              " INSERT ( type_id,leveltype )" \
              " VALUES( '"+typex+"','"+userx+"' )"
        print(sql)
        cur.execute(sql)
        con.commit()
        return render_template('insertsuccess.html', usernavbar=session['username'],usertype=session['depart'])
    except cx_Oracle.DatabaseError as e:
        con.rollback()
        return redirect(url_for('m'))
    finally:
        cur.close()
        con.close()


@app.route('/insertcompen')
def insertcompen():
    return render_template('insertcompen.html', usernavbar=session['username'],usertype=session['depart'])


@app.route('/insertcompenp', methods=['POST'])
def insertcompenp():
    try:
        con = cx_Oracle.connect(session['username'] + '/' + session['password'] + '@' + DB_URL)
        cur = con.cursor()

        # idcom = request.form['idcom']
        salary = request.form['salary']
        remuneration = request.form['remuneration']
        datecompen = request.form['datecompen']
        workhours = request.form['workhours']
        iduser = request.form['iduser']
        sql = " insert into compensation(salary,remuneration,datecompen,work_hours,id_user) " \
              " values('" + salary + "','" + remuneration + "',to_date('" + datecompen + "','yyyy-mm-dd')," \
              "'" + workhours + "','" +iduser + "')"
        print(sql)
        cur.execute(sql)
        con.commit()

        return redirect(url_for('compensation', usernavbar=session['username']))

    except cx_Oracle.DatabaseError as e:
        con.rollback()
        return redirect(url_for('m'))
    finally:
        cur.close()
        con.close()


@app.route('/updatecompen/<ID>')
def updatecompen(ID):
    try:
        con = cx_Oracle.connect(session['username'] + '/' + session['password'] + '@' + DB_URL)
        cur = con.cursor()
        sql = " select c.id, u.name,c.salary, c.remuneration, to_char(c.datecompen,'yyyy-MM-DD'),c.work_hours" \
              " from user1 u inner join compensation c on u.id = c.id_user" \
              " WHERE c.ID = '"+ID+"'"
        print(sql)
        cur.execute(sql)
        rows = cur.fetchall()
        data = {}
        for row in rows:
            data['ID'] = row[0]
            data['NAME'] = row[1]
            data['SALARY'] = row[2]
            data['REMUNERATION'] = row[3]
            data['DATECOMPEN'] = row[4]
            data['WORK_HOURS'] = row[5]
        return render_template('updatecompen.html', data=data, link='/updatecompenp', usernavbar=session['username'],usertype=session['depart'])
    except:
        return redirect(url_for('m'))
    finally:
        cur.close()
        con.close()


@app.route('/updatecompenp', methods=['POST'])
def updatecompenp():
    try:
        con = cx_Oracle.connect(session['username'] + '/' + session['password'] + '@' + DB_URL)
        cur = con.cursor()

        idcom = request.form['idcom']
        # name = request.form['name']
        salary = request.form['salary']
        remuneration = request.form['remuneration']
        # datecompen = request.form['datecompen']
        # workhours = request.form['workhours']
        sql = "  UPDATE compensation " \
              " set salary ='"+salary+"',remuneration ='"+remuneration+"'" \
              " WHERE ID = '"+idcom+"'"
        print(sql)
        cur.execute(sql)
        con.commit()
        return redirect(url_for('compensation'))

    except cx_Oracle.DatabaseError as e:
        con.rollback()
        return redirect(url_for('m'))
    finally:
        cur.close()
        con.close()


@app.route('/deletecompen/<idcom>')
def deletecompen(idcom):
    try:
        con = cx_Oracle.connect(session['username'] + '/' + session['password'] + '@' + DB_URL)
        cur = con.cursor()
        sql = "DELETE FROM compensation WHERE id='" + idcom + "' "
        print(sql)
        cur.execute(sql)
        con.commit()
        return ('dele com')

    except cx_Oracle.DatabaseError as e:
        con.rollback()
        return redirect(url_for('m'))
    finally:
        cur.close()
        con.close()


@app.route('/Datanews')
def Datanews():
    return render_template('Datanews.html', usernavbar=session['username'], usertype=session['depart'])


@app.route('/insertnews', methods=['POST'])
def insertnews():
    try:
        con = cx_Oracle.connect(session['username'] + '/' + session['password'] + '@' + DB_URL)
        cur = con.cursor()

        topic = request.form['topic']
        comment = request.form['comment']
        typenews = request.form['typenews']
        sql = " insert into news (topic,detail,datenews,id_user,type_id)" \
              " values ('" + topic + "','" + comment + "',SYSDATE,'" + session['uid'] + "','" + typenews + "')"
        print(sql)
        cur.execute(sql)
        con.commit()
        return render_template('insertsuccess.html', usernavbar=session['username'],usertype=session['depart'])
    except cx_Oracle.DatabaseError as e:
        con.rollback()
        return redirect(url_for('m'))
    finally:
        cur.close()
        con.close()


@app.route('/')
def loginmain():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def do_admin_login():
    session['username'] = request.form['username']
    session['password'] = request.form['password']
    try:
        con = cx_Oracle.connect(session['username'] + '/' + session['password'] + '@' + DB_URL)
        cur = con.cursor()
        sql = ' select depart,id from user_table'
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()
        con.close()
        session['uid'] = ''
        session['depart'] = ''
        for row in rows:
            session['depart'] = row[0]
            session['uid'] = row[1]
            print(row[1])
        if session['depart'] == 'Admin':
            return redirect(url_for('a'))
        else:
            return redirect(url_for('f'))
    except cx_Oracle.DatabaseError as e:
        flash('Username หรือ Password ไม่ถูกต้อง')
        return redirect(url_for('loginmain'))


@app.route('/tablenews')
def tablenews():
    try:
        con = cx_Oracle.connect(session['username'] + '/' + session['password'] + '@' + DB_URL)
        cur = con.cursor()
        sql = " select id,topic,detail,datenews,id_user,type_id,name,surname,active," \
              " username,address,depart,type_name " \
              " from table_news " \
              " order by datenews desc"
        print(sql)
        cur.execute(sql)
        rows = cur.fetchall()
        return render_template('tablenews.html', rows=rows, usernavbar=session['username'], usertype=session['depart'])
    except:
        return redirect(url_for('m'))
    finally:
        cur.close()
        con.close()

@app.route('/deletenews/<id>')
def deletenews(id):
    try:
        con = cx_Oracle.connect(session['username'] + '/' + session['password'] + '@' + DB_URL)
        cur = con.cursor()
        sql = "DELETE FROM news WHERE id='" + id + "' "
        print(sql)
        cur.execute(sql)
        con.commit()
        return render_template ('DeleteSuccess.html',usertype=session['depart'],usernavbar=session['username'])
    except cx_Oracle.DatabaseError as e:
        con.rollback()
        return redirect(url_for('m'))
    finally:
        cur.close()
        con.close()


@app.route('/working')
def working():
    try:
        con = cx_Oracle.connect(session['username'] + '/' + session['password'] + '@' + DB_URL)
        cur = con.cursor()
        sql = " select id_row,id_employee,to_char(starttime,'yyyy-MON-dd HH24:MI')," \
              " to_char(endtime,'yyyy-MON-dd HH24:MI'), username" \
              " from working_hours"
        print(sql)
        cur.execute(sql)
        rows = cur.fetchall()
        return render_template('working.html', rows=rows, usernavbar=session['username'], usertype=session['depart'])
    except:
        return redirect(url_for('m'))
    finally:
        cur.close()
        con.close()


@app.route('/workingu')
def workingu ():
    try:
        con = cx_Oracle.connect(session['username'] + '/' + session['password'] + '@' + DB_URL)
        cur = con.cursor()
        sql = " select id_row,id_employee,to_char(starttime,'yyyy-MON-dd HH24:MI')," \
              " to_char(endtime,'yyyy-MON-dd HH24:MI'), username" \
              " from table_working" \
              " order by starttime desc"

        print(sql)
        cur.execute(sql)
        rows = cur.fetchall()
        return render_template('workinguser.html', rows=rows, usernavbar=session['username'], usertype=session['depart'])
    except:
        return redirect(url_for('m'))
    finally:
        cur.close()
        con.close()


@app.route('/insertwork')
def insertwork():
    return render_template('insertwork.html', usernavbar=session['username'], usertype=session['depart'])


@app.route('/insertworkp', methods=['POST'])
def insertworkp():
    try:
        con = cx_Oracle.connect(session['username'] + '/' + session['password'] + '@' + DB_URL)
        cur = con.cursor()

        # idrow = request.form['idrow']
        # idem = request.form['idem']
        start = request.form['start']
        end = request.form['end']
        username = request.form['username']
        sql = " insert into table_working(starttime,endtime,username) " \
              " values(to_date(TO_CHAR(SYSDATE, 'yyyy-mm-dd')||'" + start + "','yyyy-mm-ddHH24:MI')," \
              " to_date(TO_CHAR(SYSDATE, 'yyyy-mm-dd')||'" + end + "','yyyy-mm-dd HH24:MI'),'" + username + "')"
        print(sql)
        cur.execute(sql)
        con.commit()
        return render_template('insertsuccess.html', usernavbar=session['username'],usertype=session['depart'])
    except cx_Oracle.DatabaseError as e:
        con.rollback()
        return redirect(url_for('m'))
    finally:
        cur.close()
        con.close()


@app.route('/updatework/<ID>')
def updatework(ID):
    try:
        con = cx_Oracle.connect(session['username'] + '/' + session['password'] + '@' + DB_URL)
        cur = con.cursor()
        sql = " select ID_ROW,ID_EMPLOYEE,to_char(starttime,'yyyy-mm-dd')||'T'||to_char(starttime,'HH24:MI')" \
              ",to_char(endtime,'yyyy-mm-dd')||'T'||to_char(endtime,'HH24:MI')," \
              " USERNAME from working_hours " \
              " WHERE ID_ROW = '" + ID + "'"
        print(sql)
        cur.execute(sql)
        rows = cur.fetchall()
        data = {}
        for row in rows:
            data['ID_ROW'] = row[0]
            data['ID_EMPLOYEE'] = row[1]
            data['STARTTIME'] = row[2]
            data['ENDTIME'] = row[3]
            data['USERNAME'] = row[4]
        return render_template('updatework.html', data=data, link='/updateworkp', usernavbar=session['username'],usertype=session['depart'])
    except:
        return redirect(url_for('m'))
    finally:
        cur.close()
        con.close()


@app.route('/updateworkp', methods=['POST'])
def updateworkp():
    try:
        con = cx_Oracle.connect(session['username'] + '/' + session['password'] + '@' + DB_URL)
        cur = con.cursor()

        idrow = request.form['idrow']
        idem = request.form['idem']
        start = request.form['start']
        end = request.form['end']
        username = request.form['username']
        sql = " UPDATE working_hours SET id_employee = '"+idem+"'," \
              " starttime = TO_DATE(replace('"+start+"','T',''), 'yyyy-mm-dd HH24:MI')," \
              " endtime = TO_DATE(replace('"+end+"','T',''), 'yyyy-mm-dd HH24:MI')" \
              " WHERE id_row = '"+idrow+"'"
        print(sql)
        cur.execute(sql)
        con.commit()
        return render_template('updatesuccess.html', usernavbar=session['username'])

    except cx_Oracle.DatabaseError as e:
        con.rollback()
        return redirect(url_for('m'))
    finally:
        cur.close()
        con.close()


@app.route('/deletework/<idrow>')
def deletework(idrow):
    try:
        con = cx_Oracle.connect(session['username'] + '/' + session['password'] + '@' + DB_URL)
        cur = con.cursor()
        sql = "DELETE FROM table_working WHERE id_row= '" + idrow + "' "
        print(sql)
        cur.execute(sql)
        con.commit()
        return ('delete work')

    except cx_Oracle.DatabaseError as e:
        con.rollback()
        return redirect(url_for('m'))
    finally:
        cur.close()
        con.close()


@app.route('/register2')
def register2():
    return render_template('register2.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/registerp', methods=['POST'])
def registerp():
    try:
        con = cx_Oracle.connect('tkivieemee'+'/''mee0886203137' + '@' + DB_URL)
        cur = con.cursor()

        name = request.form['name']
        surname = request.form['surname']
        username = request.form['username']
        password = request.form['password']
        address = request.form['address']
        depart = request.form['depart']
        # sql = " GRANT CREATE ANY VIEW TO tkivieemee"
        # cur.execute(sql)
        # print(sql)
        # sql = " create  user '" + username + "' IDENTIFIED by '" + password + "' "
        # print(sql)
        # cur.execute(sql)
        # sql = " insert into user1 (name,surname,username,address,depart) " \
        #       " VALUES ('" + name + "','" + surname + "','" + username + "','" + address + "','" + depart + "')"
        # print(sql)
        outVal = cur.var(int)
        cur.callproc('create_user2', ['not9999', 'not9999'])
        # print(outVal.getvalue())
        con.commit()
        return redirect(url_for('/accounts'))
    except cx_Oracle.DatabaseError as e:
        con.rollback()
        return redirect(url_for('m'))
    finally:
        cur.close()
        con.close()


@app.route('/forgotpassword')
def forgotpassword():
    return render_template('forgot-password.html')


@app.route('/select')
def select():
    try:
        con = cx_Oracle.connect(session['username'] + '/' + session['password'] + '@' + DB_URL)
        cur = con.cursor()
        sql = "select * from test1"
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            print(row)
        return (con.version)
    except:
        return redirect(url_for('m'))
    finally:
        cur.close()
        con.close()


@app.route('/insert')
def insert():
    try:
        con = cx_Oracle.connect(session['username'] + '/' + session['password'] + '@' + DB_URL)
        cur = con.cursor()
        data = {'ID': '01', 'NAME': 'TEST'}
        sql = "insert into test1" \
              "     (ID," \
              "     NAME)" \
              "     values (       " \
              "'" + data['ID'] + "',   " \
              "'" + data['NAME'] + "'" \
                              ")"
        print(sql)
        cur.execute(sql)
        con.commit()
        return ('True')
    except cx_Oracle.DatabaseError as e:
        con.rollback()
        return redirect(url_for('m'))
    finally:
        cur.close()
        con.close()


@app.route('/m')
def m():
    return render_template('404.html', usernavbar=session['username'])


@app.route('/f')
def f():
    return render_template('firstpage.html', usernavbar=session['username'],usertype=session['depart'])

@app.route('/a')
def a():
    return render_template('fadmin.html', usernavbar=session['username'],usertype=session['depart'])

@app.route('/inserts')
def inserts():
    return render_template('insertsuccess.html', usernavbar=session['username'],usertype=session['depart'])


@app.route('/updates')
def updates():
    return render_template('updatesuccess.html', usernavbar=session['username'],usertype=session['depart'])

@app.route('/delete')
def delete():
    return render_template('DeleteSuccess.html', usernavbar=session['username'],usertype=session['depart'])


@app.route('/accounts')
def accounts():
    return render_template('accountsuccess.html', usernavbar=session['username'])


if __name__ == "__main__":
    # reload(sys)
    # sys.setdefaultencoding('utf-8')
    app.run(debug=True)
    # app.run(host ='127.0.0.1',port=5000)
