from flask import Flask, render_template, request
import requests
import smtplib

MY_EMAIL = ""
PASSWORD = ""

posts = requests.get("https://api.npoint.io/0020a0e345f14e95e0d7").json()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about_me():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact_me():
    if request.method == "POST":
        data = request.form
        username = request.form["username"]
        email = request.form["email"]
        phone_number = request.form["phone"]
        message = request.form["message"]
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Happy Birthday\n\nName: {username}\n\nEmail: {email}\n\nPhone number: {phone_number}\n\nMessage: {message}"
            )
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
