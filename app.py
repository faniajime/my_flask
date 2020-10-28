from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

subscribers = []

@app.route('/')
def index():
	#title = "Fabiolas blog"
	return render_template("index.html")

@app.route('/about')
def about():
	#title = "about fabiola"
	names = ["John", "Fabiola", "Berta"]
	return render_template("about.html", names=names)

@app.route('/subscribe')
def subscribe():
	title = "Subscribe to my email newsletter"
	return render_template("subscribe.html")

@app.route('/form', methods=["POST"])
def form():
	first_name = request.form.get("first_name")
	last_name = request.form.get("last_name")
	email = request.form.get("email")

	message = "You have been subscribed to my email newsletter"
	#server = smtplib.SMTP("smtp.gmail.com", 587)
	#server.starttls()
	#server.login("faniajime@gmail.com", "PASSWORD")
	#server.sendmail("faniajime@gmail.com", email, message) 

	if not first_name or not last_name or not email:
		error_statement = "All Form Fields Required"
		return render_template("subscribe.html", error_statement= error_statement, first_name=first_name, last_name=last_name, email=email)
	else:
		subscribers.append(f"{first_name} {last_name} ~ {email}")
	title = "Subscribe to my email newsletter"
	return render_template("form.html", subscribers=subscribers)

