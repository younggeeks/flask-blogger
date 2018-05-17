import arrow
from flask import Flask, render_template, request, redirect, url_for
from markupsafe import Markup

from models.Project import Project
from models.Post import Post

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True


def dictify(resource):
    resource_dict = resource.to_dict().copy()
    resource_dict["id"] = resource.id
    if "published_at" in resource_dict:
        resource_dict["published_at"] = arrow.get(resource_dict['published_at']).humanize()

    return resource_dict


@app.template_filter()
def limit(string, words_limit=120):
    return Markup('%.{}s'.format(words_limit) % string)


@app.route("/")
def index():
    posts = [dictify(post) for post in Post.all()]
    return render_template("index.html", posts=posts)


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/projects", methods=["POST", "GET"])
def projects():
    if request.method == "GET":
        projects = [dictify(project) for project in Project.all()]
        return render_template("projects/projects.html", projects=projects)
    else:
        title = request.form.get("title")
        description = request.form.get("description")
        owner = request.form.get("owner")
        image = request.files.get("image")
        start = request.form.get("start")
        technologies = request.form.get("technologies")
        role = request.form.get("role")
        status = request.form.get("status")
        url = request.form.get("url")

        new_project = Project(
            title=title,
            description=description,
            start=start,
            owner=owner,
            technologies=technologies,
            status=status,
            role=role,
            image=image,
            url=url
        )
        new_project.save(new_project.json(), cover=image)

        return redirect(url_for("projects"))


@app.route("/projects/register")
def register_project():
    return render_template("projects/register.html")


@app.route("/show/<post_id>")
def show(post_id):
    post = dictify(Post.get_one(id=post_id))
    return render_template("show.html", post=post)


@app.route("/search")
def search():
    pass


@app.route("/posts/edit/<post_id>", methods=["GET", "POST"])
def edit(post_id):
    if request.method == "GET":
        post = dictify(Post.get_one(id=post_id))
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
        cover = request.files.get("cover")
        title = str(request.form.get("title"))
        body = request.form.get("body")
        category = request.form.get("category")
        user_id = "samjunior101"

        new_post = Post(title=title, body=body, user_id=user_id, category=category, cover=cover)

        Post.save(data=new_post.json(), cover=cover)

        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
