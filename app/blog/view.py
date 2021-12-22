from flask import render_template

from . import blog


@blog.route('/', methods=['GET', 'POST'])
def main():
    return render_template('blog/main.html')
