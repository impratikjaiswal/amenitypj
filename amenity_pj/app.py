import os
import sqlite3

from flask import Flask, render_template, request, url_for, flash, redirect
from flask_sitemapper import Sitemapper
from werkzeug.exceptions import abort

from amenity_pj.helper import app_tlv_play, app_asn1_play, app_qr_play
from amenity_pj.helper.constants import Const

app = Flask(__name__)

sitemapper = Sitemapper()
sitemapper.init_app(app)

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


# @sitemap.register_generator
# def index():
# This function is Not needed if you set SITEMAP_INCLUDE_RULES_WITHOUT_PARAMS=True
# https://www.sitemaps.org/protocol.html
# yield Const.END_POINT_INDEX, {}
# yield Const.END_POINT_INDEX, {}, Const.DEPLOYMENT_DATE, 'monthly'


@app.context_processor
def utility_processor():
    def title_for(end_point=None):
        return Const.END_POINT_AND_TITLE_MAPPING.get(end_point, Const.TITLE_AMENITY_PJ)

    return dict(title_for=title_for)


@app.context_processor
def utility_processor_asn1_play_1():
    def is_selected_asn1_schema(asn1_schema, selected_asn1_schema):
        if asn1_schema == selected_asn1_schema:
            return 'SELECTED'
        else:
            return ''

    return dict(is_selected_asn1_schema=is_selected_asn1_schema)


@app.context_processor
def utility_processor_asn1_play_2():
    def is_selected_asn1_object(asn1_object, selected_asn1_object):
        if asn1_object == selected_asn1_object:
            return 'SELECTED'
        else:
            return ''

    return dict(is_selected_asn1_object=is_selected_asn1_object)


@app.route(Const.URL_SITEMAP)
def sitemap():
    return sitemapper.generate()


@sitemapper.include(lastmod=Const.DEPLOYMENT_DATE)
@app.route(Const.URL_AMENITY_PJ)
def index():
    default_data = {
        'app_title': Const.TITLE_AMENITY_PJ,
        'app_description': Const.DESCRIPTION_AMENITY_PJ,
        'app_version': Const.VERSION_AMENITY_PJ,
        'app_github_url': Const.GITHUB_URL_AMENITY_PJ,
    }
    return render_template(Const.TEMPLATE_AMENITY_PJ, **default_data)


@sitemapper.include(lastmod=Const.DEPLOYMENT_DATE)
@app.route(Const.URL_ASN1_PLAY, methods=('GET', 'POST'))
def asn1_play():
    return app_asn1_play.handle_requests()


@app.route(Const.URL_ASN1_PLAY_ASN1_OBJECTS)
def asn1_play_asn1_objects():
    return app_asn1_play.handle_asn1_objects()


@sitemapper.include(lastmod=Const.DEPLOYMENT_DATE)
@app.route(Const.URL_TLV_PLAY, methods=('GET', 'POST'))
def tlv_play():
    return app_tlv_play.handle_requests()


@sitemapper.include(lastmod=Const.DEPLOYMENT_DATE)
@app.route(Const.URL_QR_PLAY, methods=('GET', 'POST'))
def qr_play():
    return app_qr_play.handle_requests()


@sitemapper.include(lastmod=Const.DEPLOYMENT_DATE)
@app.route(Const.URL_EXCEL_PLAY, methods=('GET', 'POST'))
def excel_play():
    default_data = {
        'app_title': Const.TITLE_EXCEL_PLAY,
        'app_description': Const.DESCRIPTION_EXCEL_PLAY,
        'app_version': Const.VERSION_EXCEL_PLAY,
        'app_github_url': Const.GITHUB_URL_EXCEL_PLAY,
    }
    return render_template(Const.TEMPLATE_EXCEL_PLAY, **default_data)


@sitemapper.include(lastmod=Const.DEPLOYMENT_DATE)
@app.route(Const.URL_SPONSORSHIP, methods=('GET', 'POST'))
def sponsorship():
    default_data = {
        'app_title': Const.TITLE_SPONSORSHIP,
        'app_description': Const.DESCRIPTION_SPONSORSHIP,
        'app_version': Const.VERSION_SPONSORSHIP,
        'app_github_url': Const.GITHUB_URL_SPONSORSHIP,
    }
    return render_template(Const.TEMPLATE_SPONSORSHIP, **default_data)


@sitemapper.include(lastmod=Const.DEPLOYMENT_DATE)
@app.route(Const.URL_ABOUT_US, methods=('GET', 'POST'))
def about_us():
    default_data = {
        'app_title': Const.TITLE_ABOUT_US,
        'app_description': Const.DESCRIPTION_ABOUT_US,
        'app_version': Const.VERSION_ABOUT_US,
        'app_github_url': Const.GITHUB_URL_ABOUT_US,
    }
    return render_template(Const.TEMPLATE_ABOUT_US, **default_data)


@sitemapper.include(lastmod=Const.DEPLOYMENT_DATE)
@app.route(Const.URL_TESTIMONIALS, methods=('GET', 'POST'))
def testimonials():
    default_data = {
        'app_title': Const.TITLE_TESTIMONIALS,
        'app_description': Const.DESCRIPTION_TESTIMONIALS,
        'app_version': Const.VERSION_TESTIMONIALS,
        'app_github_url': Const.GITHUB_URL_TESTIMONIALS,
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


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template(Const.TEMPLATE_POST, post=post)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')
