from flask import *

from src.dbconnectionnew import *

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('login.html')


@app.route('/adminhome')
def adminhome():
    return render_template('admin_home.html')

@app.route('/addofficer',methods=['post','get'])
def addofficer():
    return render_template('add_officer.html')

@app.route('/viewofficers')
def viewofficers():
    return render_template('view_officers.html')

@app.route('/verifyusers')
def verifyusers():
    return render_template('verify_user.html')

@app.route('/managedoubts')
def managedoubts():
    return render_template('manage_doubts.html')

@app.route('/addschemesandamounts')
def addschemesandamounts():
    return render_template('schemes_amount.html')

@app.route('/sendnotification')
def sendnotification():
    return render_template('send_notification.html')

@app.route('/officerhome')
def officerhome():
    return render_template('officer_home.html')

@app.route('/viewofficer_admin')
def viewofficer_admin():
    return render_template('view_officer.html')

@app.route('/viewusers')
def viewusers():
    return render_template('view_users.html')

@app.route('/viewschemesandsanctionamount')
def viewschemesandsanctionamount():
    return render_template('view_schms_sanctn_amnt.html')

@app.route('/viewveifiedsanctionedscheme')
def viewveifiedsanctionedscheme():
    return render_template('view_vrfd_sanctnd_schm.html')

@app.route('/viewnotifications')
def viewnotifications():
    return render_template('view_notfctns.html')

@app.route('/userhome')
def userhome():
    return render_template('user_home.html')

@app.route('/userregistration')
def userregistration():
    return render_template('User_regstn.html')

@app.route('/viewuserprofile')
def viewuserprofile():
    return render_template('view_user_prfl.html')

@app.route('/viewschemesandsendamount')
def viewschemesandsendamount():
    return render_template('view_send_schms_amnt.html')

@app.route('/viewrequeststatus')
def viewrequeststatus():
    return render_template('view_rqst_stats.html')

@app.route('/senddoubts')
def senddoubts():
    return render_template('send_doubts.html')

@app.route('/viewreplay')
def viewreplay():
    return render_template('view_replay.html')

@app.route('/login_code',methods=['get','post'])
def login_code():
    username=request.form['textfield']
    password=request.form['textfield2']
    arg="select * from login where username = %s and password = %s"
    val=(username,password)
    res = selectone(arg,val)
    if res is None:
        return '''<script alert("invalid");window.location="/"</script>'''
    elif res['type'] == 'admin':
        return '''<script> alert("welcome to admin home");window.location="/adminhome"</script>'''

    elif res['type'] == 'officer':
        session['lid'] = res['id']
        return redirect('/officerhome')
    elif res['type'] == 'user':
        return redirect('/userhome')
    else:
        return '''<script alert("invalid");window.location="/"</script>'''


@app.route('/addofficer1',methods=['get','post'])
def addofficer1():
    f_name = request.form['textfield']
    l_name = request.form['textfield2']
    place = request.form['textfield3']
    post = request.form['textfield4']
    pin = request.form['textfield5']
    email = request.form['textfield6']
    phone = request.form['textfield7']
    username = request.form['textfield8']
    password = request.form['textfield9']

    qry="insert into login values (null,%s,%s,'officer')"
    val = (username,password)
    id = iud(qry,val)
    qry= "insert into officer values(null,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (str(id),f_name,l_name,email,phone,pin,place,post)
    iud(qry,val)
    return '''<script> alert("added");window.location="/viewofficer_admin"</script>'''

app.run(debug=True)
