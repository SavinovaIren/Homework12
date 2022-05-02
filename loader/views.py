from flask import Blueprint, render_template, request
import logging
from loader.utils import *
from main.utils import *

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')
logging.basicConfig(filename="logging.log", level=logging.INFO)

@loader_blueprint.route('/post', methods=["GET"])
def new_page():
    return render_template("post_form.html")


@loader_blueprint.route('/post', methods=["POST"])
def add_new_page():
    picture = request.files.get("picture")
    content = request.form.get("content")
    if not picture or not content:
        logging.info("Данные не загружены, отсутствует часть данных")
        return 'Данные не загружены, отсутствует часть данных'
    posts = load_json('posts.json')
    try:
        new_post = {"pic": save_pic(picture), "content": content}
    except WrongImageType:
        return 'Неверный тип файла'
    else:
        posts.append(new_post)
        with open('posts.json', "w", encoding="UTF-8") as file:
            json.dump(posts, file, ensure_ascii=False)
        return render_template("post_uploaded.html", new_post=new_post)
