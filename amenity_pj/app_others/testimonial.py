import os
import sqlite3

from flask import abort, flash, request
from python_helpers.ph_constants import PhConstants
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_util import PhUtil

from amenity_pj.helper.constants import Const
from amenity_pj.helper.defaults import Defaults
from amenity_pj.helper.util import Util


def handle_requests(apj_id, default_data, **kwargs):
    """

    :return:
    """
    # Handle kwargs
    api = kwargs.get(PhKeys.API, Defaults.API)
    log = kwargs.get(PhKeys.LOG, Defaults.LOG)
    #
    default_data_app = {
        PhKeys.TESTIMONIAL_POSTS: PhConstants.STR_EMPTY,
    }
    app_data = PhUtil.dict_merge(default_data, default_data_app)
    Util.request_pre(request=request, apj_id=apj_id, api=api, log=log)
    if request.method == PhKeys.GET:
        conn = get_db_connection()
        posts = conn.execute('SELECT * FROM posts').fetchall()
        conn.close()
        app_data.update({PhKeys.TESTIMONIAL_POSTS: posts})
        return Util.request_post(request=request, apj_id=apj_id, api=api, log=log, output_data=app_data)
    elif request.method == PhKeys.POST:
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
            posts = conn.execute('SELECT * FROM posts').fetchall()
            conn.close()
            app_data.update({PhKeys.TESTIMONIAL_POSTS: posts})
        return Util.request_post(request=request, apj_id=Const.APJ_ID_TESTIMONIALS, api=api, log=log,
                                 output_data=app_data)


def handle_posts(apj_id, default_data, **kwargs):
    """

    :param apj_id:
    :param api:
    :param log:
    :param default_data:
    :param kwargs:
    :return:
    """
    # Handle kwargs
    api = kwargs.get(PhKeys.API, Defaults.API)
    log = kwargs.get(PhKeys.LOG, Defaults.LOG)
    #
    default_data_app = {
        PhKeys.TESTIMONIAL_POSTS: PhConstants.STR_EMPTY,
    }
    app_data = PhUtil.dict_merge(default_data, default_data_app)
    # Handle kwargs
    testimonial_post_id = kwargs.get(PhKeys.TESTIMONIAL_POST_ID, -1)
    post = get_post(testimonial_post_id)
    app_data.update({PhKeys.TESTIMONIAL_POST: post})
    return Util.request_post(request=request, apj_id=apj_id, api=api, log=log, output_data=app_data)


def get_db_connection():
    # conn = sqlite3.connect(r'database.db')
    path = os.sep.join([os.path.dirname(os.path.realpath(__file__)), os.pardir, 'db', 'database.db'])
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def get_post(testimonial_post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (testimonial_post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post
