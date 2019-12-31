from flask import Flask, render_template, url_for, request, redirect, session
from flask_mysqldb import MySQL
import yaml
import json
import pandas as pd


app = Flask(__name__)
app.secret_key = 'grab ur vi'

db = yaml.load(open('guvi_yaml.yaml'), Loader = yaml.FullLoader)

app.config["MYSQL_HOST"] = db["mysql_host"]
app.config["MYSQL_USER"] = db["mysql_user"]
app.config["MYSQL_PASSWORD"] = db["mysql_password"]
app.config["MYSQL_DB"] = db["mysql_db"]

mysql = MySQL(app)



@app.route('/')
def home():
	return render_template('index.html')



@app.route('/signup')
def signup():
	login = url_for('login')
	svg = [url_for('static', filename='svg/contact.svg'), url_for('static', filename='svg/cell-phone.svg'),
	url_for('static', filename='svg/calendar.svg'), url_for('static', filename='svg/lock.svg'),
	url_for('static', filename='svg/envelope.svg'), url_for('static', filename='svg/cityscape.svg')]
	return render_template('sign_up.html', svg = svg, login = login)


@app.route('/signedup', methods = ['POST'])
def signedup():
	if request.method == 'POST':
		firstname = request.form['firstname']
		lastname = request.form['lastname']
		mail = request.form['mail']
		dob = request.form['dob']
		mobile_1 = request.form['mobile1']
		mobile_2 = request.form['mobile2']
		city = request.form['city']
		password = request.form['password']
		s = str(password)
		h_pwd = 7
		for i in range(len(s)):
			h_pwd = (h_pwd*31 + ord(s[i]) + i) + 11


		cur = mysql.connection.cursor()
		query = "INSERT into users (firstname, lastname, mail_id, dob, mobile1, mobile2, city, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
		val = (firstname, lastname, mail, dob, mobile_1, mobile_2, city, h_pwd)
		cur.execute(query, val)
		mysql.connection.commit()
		
		cur.execute("SELECT * from users;")
		data = cur.fetchall()
		data = pd.DataFrame(data, columns = ['id', 'firstname', 'lastname', 'mail_id', 'dob', 'mobile1', 'mobile2', 'city', 'password'])
		data.to_json("users_table.json", orient = 'records')


		mysql.connection.commit()
		cur.close()


		return json.dumps({'status':'OK','firstname': firstname,'lastname': lastname});
	return redirect(url_for('login'))




@app.route('/login', methods = ['POST', 'GET'])
def login():
	svg = [url_for('static', filename='svg/lock.svg'), url_for('static', filename='svg/envelope.svg')]

	if request.method == 'POST':
		mail_log = request.form['mail_log']
		password_log = request.form['password_log']

		s = str(password_log)
		h_pwd = 7
		for i in range(len(s)):
			h_pwd = (h_pwd*31 + ord(s[i]) + i) + 11



		cur = mysql.connection.cursor()
		query = "SELECT mail_id from users;"
		cur.execute(query)
		mail_list = list(cur.fetchall())
		query = "SELECT password from users;"
		cur.execute(query)
		pwd_list = list(cur.fetchall())

		mail_lst = []
		for i in mail_list: mail_lst.append(i[0])

		pwd_lst = []
		for i in pwd_list: pwd_lst.append(str(i[0]))


		dt = {}
		for i in range(len(mail_lst)):
			dt[mail_lst[i]] = pwd_lst[i]
		
		if mail_log in mail_lst and str(h_pwd) == dt[mail_log]:
			session['username'] = mail_log
			return redirect(url_for('profile'))
		else:
			return render_template('login.html', alert = '* Incorrect E-mail or Password', flag = 1, svg = svg)
		
	return render_template('login.html', svg = svg)




@app.route('/profile', methods = ['POST', 'GET'])
def profile():
	svg = [url_for('static', filename='svg/lock.svg')]
	if 'username' in session:
		user = str(session['username'])
		cur = mysql.connection.cursor()
		query = "SELECT * from users where mail_id = %s;"
		val = (user, )
		cur.execute(query, val)
		res = cur.fetchall()
		col = ["", "FIRST NAME", "LAST NAME", "E - MAIL", "DATE OF BIRTH", "MOBILE 1", "MOBILE 2", "CITY"]


		if request.method == 'POST':
			old_password = request.form['old_password']
			new_password = request.form['new_password']
			if 'username' in session:
				user = str(session['username'])
				cur.execute("SELECT id, password from users where mail_id = %s;", (user, ))
				ch = cur.fetchall()
				user_id = ch[0][0]
				pwd = ch[0][1]

				s = str(old_password)
				h_pwd = 7
				for i in range(len(s)):
					h_pwd = (h_pwd*31 + ord(s[i]) + i) + 11

				# print(pwd, h_pwd)

				if str(pwd) == str(h_pwd):
					s = str(new_password)
					hash_pwd = 7
					for i in range(len(s)):
						hash_pwd = (hash_pwd*31 + ord(s[i]) + i) + 11
					# print(hash_pwd, pwd)
					query = "UPDATE users set password = %s where id = %s;"
					val = (str(hash_pwd), user_id)
					cur.execute(query, val)
					mysql.connection.commit()

					cur.execute("SELECT * from users;")
					data = cur.fetchall()
					data = pd.DataFrame(data, columns = ['id', 'firstname', 'lastname', 'mail_id', 'dob', 'mobile1', 'mobile2', 'city', 'password'])
					data.to_json("users_table.json", orient = 'records')

					mysql.connection.commit()
					cur.close()
				else:
					return render_template('profile.html', res = res[0], l = len(res[0]), col = col, svg = svg, flag = 1, alert = "* Incorrect Old Password")


		return render_template('profile.html', res = res[0], l = len(res[0]), col = col, svg = svg)
	else:
		return redirect(url_for('login'))




@app.route('/edit', methods=['POST', 'GET'])
def edit():
	svg = [url_for('static', filename='svg/contact.svg'), url_for('static', filename='svg/cell-phone.svg'),
	url_for('static', filename='svg/calendar.svg'), url_for('static', filename='svg/lock.svg'),
	url_for('static', filename='svg/envelope.svg'), url_for('static', filename='svg/cityscape.svg')]

	if 'username' in session:
		user = str(session['username'])
		cur = mysql.connection.cursor()
		query = "SELECT * from users where mail_id = %s;"
		val = (user, )
		cur.execute(query, val)
		res = cur.fetchall()
		user_id = res[0][0]


		if request.method == 'POST':
		
			firstname = request.form['firstname']
			lastname = request.form['lastname']
			mail = request.form['mail']
			dob = request.form['dob']
			mobile_1 = request.form['mobile1']
			mobile_2 = request.form['mobile2']
			city = request.form['city']

			cur = mysql.connection.cursor()
			query = "UPDATE users set firstname = %s, lastname = %s, mail_id = %s, dob = %s, mobile1 = %s, mobile2 = %s, city = %s where id = %s;"
			val = (firstname, lastname, mail, dob, mobile_1, mobile_2, city, user_id)
			cur.execute(query, val)
			mysql.connection.commit()

			cur.execute("SELECT * from users;")
			data = cur.fetchall()
			data = pd.DataFrame(data, columns = ['id', 'firstname', 'lastname', 'mail_id', 'dob', 'mobile1', 'mobile2', 'city', 'password'])
			data.to_json("users_table.json", orient = 'records')

			mysql.connection.commit()
			cur.close()

			return redirect(url_for('profile'))
	return render_template('edit.html', svg = svg, res = res[0], l = len(res[0]))






@app.route('/logout')
def logout():
	session.clear()
	return redirect(url_for('login'))

if __name__ == '__main__':
	app.run(debug = True)