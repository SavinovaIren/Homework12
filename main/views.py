import logging

from flask import Blueprint, render_template, request
from main.utils import *
from extentions import *

# Затем создаем новый блюпринт, выбираем для него имя
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

@main_blueprint.route('/')
def main_page():
    logging.info('Открытие главной страницы')
    return render_template("index.html")


@main_blueprint.route('/search')
def search_page():
    s = request.args.get('s', '')
    logging.info('Выполняется поиск')
    try:
        posts = load_json('posts.json')
    except DataJsonError:
        return 'Проблемы с открытием файла'
    path = search_post_by_string(posts, s)
    return render_template("post_list.html", posts=path, s=s)
