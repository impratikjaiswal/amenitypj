import os
import sqlite3

from flask import Flask, render_template, request, url_for, flash, redirect
from flask_sitemap import Sitemap
from werkzeug.exceptions import abort

from amenity_pj_app.helper import app_tlv_play, app_asn1_play, app_qr_play
from amenity_pj_app.helper.constants import Const
from amenity_pj_app.helper.constants_config import ConfigConst

app = Flask(__name__)

ext = Sitemap(app=app)
app.config['SECRET_KEY'] = 'Pj Test'


# app.config['SITEMAP_MAX_URL_COUNT'] = 10

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


@ext.register_generator
def index():
    # Not needed if you set SITEMAP_INCLUDE_RULES_WITHOUT_PARAMS=True
    yield Const.END_POINT_INDEX, {}
    yield Const.END_POINT_ASN1_PLAY, {}
    yield Const.END_POINT_TLV_PLAY, {}
    yield Const.END_POINT_QR_PLAY, {}
    yield Const.END_POINT_EXCEL_PLAY, {}
    yield Const.END_POINT_SPONSORSHIP, {}
    yield Const.END_POINT_ABOUT_US, {}
    yield Const.END_POINT_TESTIMONIALS, {}


@app.context_processor
def utility_processor():
    def title_for(end_point=None):
        return Const.END_POINT_AND_TITLE_MAPPING.get(end_point, ConfigConst.TOOL_TITLE)

    return dict(title_for=title_for)


@app.route(Const.URL_INDEX)
def index():
    default_data = {
        'app_title': ConfigConst.TOOL_TITLE,
        'app_version': f'v{ConfigConst.TOOL_VERSION}',
        'app_github_url': Const.GITHUB_URL_DEFAULT,
    }
    return render_template(Const.TEMPLATE_INDEX, **default_data)


@app.route(Const.URL_ASN1_PLAY, methods=('GET', 'POST'))
def asn1_play():
    return app_asn1_play.handle_requests()


@app.route(Const.URL_TLV_PLAY, methods=('GET', 'POST'))
def tlv_play():
    return app_tlv_play.handle_requests()


@app.route(Const.URL_QR_PLAY, methods=('GET', 'POST'))
def qr_play():
    return app_qr_play.handle_requests()


@app.route(Const.URL_EXCEL_PLAY, methods=('GET', 'POST'))
def excel_play():
    default_data = {
        'app_title': Const.TITLE_EXCEL_PLAY,
        'app_version': Const.VERSION_DEFAULT,
        'app_github_url': Const.GITHUB_URL_EXCEL_PLAY,
    }
    return render_template(Const.TEMPLATE_WIP, **default_data)


@app.route(Const.URL_SPONSORSHIP, methods=('GET', 'POST'))
def sponsorship():
    default_data = {
        'app_title': Const.TITLE_SPONSORSHIP,
        'app_version': Const.VERSION_DEFAULT,
        'app_github_url': Const.GITHUB_URL_DEFAULT,
    }
    return render_template(Const.TEMPLATE_WIP, **default_data)


@app.route(Const.URL_ABOUT_US, methods=('GET', 'POST'))
def about_us():
    default_data = {
        'app_title': Const.TITLE_ABOUT_US,
        'app_version': Const.VERSION_DEFAULT,
        'app_github_url': Const.GITHUB_URL_DEFAULT,
    }
    return render_template(Const.TEMPLATE_ABOUT_US, **default_data)


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template(Const.TEMPLATE_POST, post=post)


@app.route(Const.URL_TESTIMONIALS, methods=('GET', 'POST'))
def testimonials():
    default_data = {
        'app_title': Const.TITLE_TESTIMONIALS,
        'app_version': Const.VERSION_DEFAULT,
        'app_github_url': Const.GITHUB_URL_DEFAULT,
    }
    if request.method == 'GET':
        conn = get_db_connection()
        posts = conn.execute('SELECT * FROM posts').fetchall()
        conn.close()
        return render_template(Const.TEMPLATE_TESTIMONIALS, posts=posts, **default_data)
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
            return redirect(url_for(Const.END_POINT_TESTIMONIALS))
    return render_template(Const.TEMPLATE_TESTIMONIALS, **default_data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')
