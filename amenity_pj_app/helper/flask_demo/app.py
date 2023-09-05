import io
import os
import sqlite3

import segno
from flask import Flask, render_template, request, url_for, flash, redirect,  send_file, abort
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Pj Test'


@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)


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


def get_delete(post_id):
    post = get_post(post_id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (post_id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))


@app.route('/static')
def index_static():
    return render_template('index_static.html')


@app.route('/span_samples')
def span_samples():
    return render_template('span_samples.html')


@app.route('/drop_down_samples')
def drop_down_samples():
    colours = ['Red', 'Blue', 'Black', 'Orange']
    return render_template('drop_down_samples.html', colours=colours, default_colour='Black')


@app.route('/button_samples')
def button_samples():
    return render_template('button_samples.html')


@app.route('/template')
def index_template():
    return render_template('index_plain_template.html')


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('create.html')


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('edit.html', post=post)


@app.route('/<int:id>/delete', methods=('GET', 'POST'))
def delete(id):
    post = get_post(id)
    if request.method == 'POST':
        get_delete(id)
        return redirect(url_for('index'))
    return render_template('delete.html', post=post)


@app.route('/<int:id>/delete_w_edit', methods=('POST',))
def delete_w_edit(id):
    get_delete(id)
    return redirect(url_for('index'))


@app.route('/segno_sample')
def segno_sample():
    qr = segno.make('The Continuing Story of Bungalow Bill')
    return render_template('segno_sample.html', qr=qr)


@app.route('/qr-svg/')
def qrcode_svg():
    data = request.args.get('data')
    if data not in ('Savoy Truffle', 'Rocky Raccoon'):
        return abort(404)
    buff = io.BytesIO()
    segno.make(data, micro=False).save(buff, kind='svg', scale=4)
    buff.seek(0)
    return send_file(buff, mimetype='image/svg+xml')


@app.route('/qr-png/')
def qrcode_png():
    data = request.args.get('data')
    if data not in ('Savoy Truffle', 'Rocky Raccoon'):
        return abort(404)
    buff = io.BytesIO()
    segno.make(data, micro=False) \
        .save(buff, kind='png', scale=4, dark='darkblue', data_dark='#474747',
              light='#efefef')
    buff.seek(0)
    return send_file(buff, mimetype='image/png')
