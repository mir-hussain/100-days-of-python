from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
all_posts = response.json()


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route("/post/<int:index>")
def get_post(index):
    post = [post for post in all_posts if post['id'] == index]
    print(post)

    return render_template("post.html", title=post[0]['title'], subtitle=post[0]['subtitle'], body=post[0]['body'])


if __name__ == "__main__":
    app.run(debug=True)
