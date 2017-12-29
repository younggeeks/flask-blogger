import uuid
from datetime import datetime

import arrow
from flask import Flask, render_template, request, redirect, url_for
from markupsafe import Markup

from models.Post import Post

app = Flask(__name__)


def dictify(post):
    post_dict = post.to_dict().copy()
    post_dict["id"] = post.id
    post_dict["published_at"] = arrow.get(post_dict['published_at']).humanize()
    return post_dict


@app.template_filter()
def limit(string, words_limit=120):
    return Markup('%.{}s'.format(words_limit) % string)


@app.route("/")
def index():
    posts = [dictify(post) for post in Post.all()]
    return render_template("index.html", posts=posts)


@app.route("/show/<post_id>")
def show(post_id):
    post = dictify(Post.get_one(post_id=post_id))
    return render_template("show.html", post=post)


@app.route("/search")
def search():
    pass


@app.route("/posts/edit/<post_id>", methods=["GET", "POST"])
def edit(post_id):
    if request.method == "GET":
        post = dictify(Post.get_one(post_id=post_id))
        return render_template("edit.html", post=post)
    else:
        title = str(request.form.get("title"))
        body = request.form.get("body")
        category = request.form.get("category")
        user_id = "samjunior101"

        data = {
            u'title': title,
            u'body': body,
            u'user_id': user_id,
            u'category': category
        }

        Post.save(data=data, post_id=post_id)
        return redirect(url_for("index"))


@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template("create.html")
    else:

        title = str(request.form.get("title"))
        body = request.form.get("body")
        category = request.form.get("category")
        published_at = str(datetime.utcnow())
        user_id = "samjunior101"

        new_post = Post(title=title, body=body, user_id="samjunior101", category=category)

        data = {
            u'title': title,
            u'body': body,
            u'published_at': published_at,
            u'user_id': user_id,
            u'category': category
        }

        Post.save(data=data)

        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
