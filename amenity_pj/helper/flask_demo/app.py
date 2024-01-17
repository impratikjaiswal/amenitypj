import io
import os
import sqlite3

import segno
from flask import Flask, render_template, request, url_for, flash, redirect, send_file, abort
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Pj Test'


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


###################################

@app.route('/blog')
def blog():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('blog.html', posts=posts)


@app.route('/blog_create', methods=('GET', 'POST'))
def blog_create():
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
            return redirect(url_for('blog'))
    return render_template('blog_create.html')


@app.route('/<int:id>/blog_delete', methods=('GET', 'POST'))
def blog_delete(id):
    post = get_post(id)
    if request.method == 'POST':
        get_delete(id)
        return redirect(url_for('blog'))
    return render_template('blog_delete.html', post=post)


@app.route('/<int:id>/blog_edit', methods=('GET', 'POST'))
def blog_edit(id):
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
            return redirect(url_for('blog'))
    return render_template('blog_edit.html', post=post)


@app.route('/<int:id>/blog_edit_wo_delete', methods=('GET', 'POST'))
def blog_edit_wo_delete(id):
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
            return redirect(url_for('blog'))
    return render_template('blog_edit_wo_delete.html', post=post)


@app.route('/<int:post_id>')
def blog_post(post_id):
    post = get_post(post_id)
    return render_template('blog_post.html', post=post)


@app.route('/blog_view_only')
def blog_view_only():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('blog_view_only.html', posts=posts)


@app.route('/button_samples')
def button_samples():
    return render_template('button_samples.html')


@app.route('/drop_down_samples')
def drop_down_samples():
    colours = ['Red', 'Blue', 'Black', 'Orange']
    return render_template('drop_down_samples.html', colours=colours, default_colour='Black')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index_static')
def index_static():
    return render_template('index_static.html')


@app.route('/segno_samples')
def segno_samples():
    qr = segno.make('The Continuing Story of Bungalow Bill')
    return render_template('segno_samples.html', qr=qr)


@app.route('/segno_qrcode_svg/')
def segno_qrcode_svg():
    data = request.args.get('data')
    if data not in ('Savoy Truffle', 'Rocky Raccoon'):
        return abort(404)
    buff = io.BytesIO()
    segno.make(data, micro=False).save(buff, kind='svg', scale=4)
    buff.seek(0)
    return send_file(buff, mimetype='image/svg+xml')


@app.route('/segno_qr-png/')
def segno_qrcode_png():
    data = request.args.get('data')
    if data not in ('Savoy Truffle', 'Rocky Raccoon'):
        return abort(404)
    buff = io.BytesIO()
    segno.make(data, micro=False) \
        .save(buff, kind='png', scale=4, dark='darkblue', data_dark='#474747',
              light='#efefef')
    buff.seek(0)
    return send_file(buff, mimetype='image/png')


@app.route('/span_samples')
def span_samples():
    return render_template('span_samples.html')
