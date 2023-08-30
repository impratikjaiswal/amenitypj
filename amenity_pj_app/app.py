import os
import sqlite3

from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

from amenity_pj_app.helper import app_tlv_play, app_asn1_play
from amenity_pj_app.helper.constants_config import ConfigConst

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Pj Test'


@app.route('/')
def index():
    page_url = 'index.html'
    default_data = {
        'version': f'v{ConfigConst.TOOL_VERSION}',
    }
    return render_template(page_url, **default_data)


@app.route('/asn1Play', methods=('GET', 'POST'))
def asn1_play():
    return app_asn1_play.handle_requests()


@app.route('/tlvPlay', methods=('GET', 'POST'))
def tlv_play():
    return app_tlv_play.handle_requests()


@app.route('/excelPlay', methods=('GET', 'POST'))
def excel_play():
    return render_template('wip.html', page='excelPlay', git_end_point='excelPlay')


@app.route('/sponsorship', methods=('GET', 'POST'))
def sponsorship():
    return render_template('wip.html', page='sponsorship')


@app.route('/about', methods=('GET', 'POST'))
def about():
    return render_template('aboutus.html')


def get_db_connection():
    # conn = sqlite3.connect(r'database.db')
    path = os.sep.join([os.path.dirname(os.path.realpath(__file__)), 'db', 'database.db'])
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)


@app.route('/testimonials', methods=('GET', 'POST'))
def testimonials():
    if request.method == 'GET':
        conn = get_db_connection()
        posts = conn.execute('SELECT * FROM posts').fetchall()
        conn.close()
        return render_template('testimonials.html', posts=posts)
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        publisher = request.form['publisher']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content, publisher) VALUES (?, ?, ?)',
                         (title, content, publisher))
            conn.commit()
            conn.close()
            return redirect(url_for('testimonials'))
    return render_template('testimonials.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')
