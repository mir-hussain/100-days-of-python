@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route("/post/<int:index>")
def post():
    pass


if __name__ == "__main__":
    app.run(debug=True)
