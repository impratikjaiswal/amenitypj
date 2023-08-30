import os
import sqlite3

from flask import Flask, render_template, request, url_for, flash, redirect
from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
from python_helpers.ph_util import PhUtil
from werkzeug.exceptions import abort

from asn1_play.main.data_type.data_type_master import DataTypeMaster
from asn1_play.main.helper.constants_config import ConfigConst
from asn1_play.main.helper.formats import Formats
from asn1_play.main.helper.formats_group import FormatsGroup

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Pj Test'


@app.route('/')
def index():
    return render_template('index.html')


def get_sample_data(key):
    sample_data = {
        'sample_1': {
            'raw_data': 'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
            'input_format': Formats.DER,
            'output_format': Formats.ASN1,
            'asn1_element': 'StoreMetadataRequest',
            'tlv_parsing_of_output': False,
            'remarks_list': 'Der to Asn1'
        },
        'sample_2': {
            'raw_data': """{
  iccid '989209012143658709F5'H,
  serviceProviderName "SP Name 1",
  profileName "Operational Profile Name 1"
}""",
            'input_format': Formats.ASN1,
            'output_format': Formats.DER,
            'asn1_element': 'StoreMetadataRequest',
            'tlv_parsing_of_output': True,
            'remarks_list': 'Asn1 to Der'
        },
        'sample_3': {
            'raw_data': 'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
            'input_format': Formats.DER,
            'output_format': Formats.DER_64,
            'asn1_element': ' ',
            'tlv_parsing_of_output': False,
            'remarks_list': 'Der(Hex) to Base 64'
        },
        'sample_4': {
            'raw_data': 'Welcome To AsnPlay !!!',
            'input_format': Formats.ASCII,
            'output_format': Formats.HEX,
            'asn1_element': ' ',
            'tlv_parsing_of_output': False,
            'remarks_list': 'Ascii to Hex'
        }
    }
    return sample_data.get(key, None)


@app.route('/asn1Play', methods=('GET', 'POST'))
def asn1Play():
    """

    :return:
    """
    input_formats = FormatsGroup.INPUT_FORMATS
    input_formats.sort()
    output_formats = FormatsGroup.ALL_FORMATS
    output_formats.sort()
    page_url = 'asn1Play.html'
    default_data = {
        'version': f'v{ConfigConst.TOOL_VERSION}',
        'input_formats': input_formats,
        'output_formats': output_formats,
        'selected_input_format': Formats.HEX,
        'selected_output_format': Formats.ASN1,
        'sample_processing': 'load_only',
        'output_data': '',
    }
    if request.method == 'GET':
        return render_template(page_url, **default_data)
    if request.method == 'POST':
        PhUtil.print_iter(request.form, header='request.form')
        sample_processing = request.form['sample_processing']
        # if not request.form['raw_data']:
        #     flash('raw_data is required!')
        sample_data_dict = None
        for key in request.form.keys():
            if not key.startswith('sample'):
                continue
            sample_data_dict = get_sample_data(key)
            if sample_data_dict:
                break
        if sample_data_dict and sample_processing == 'load_only':
            # Data Processing is not needed
            pass
        else:
            # Data Processing is needed in all other cases
            # Filter All Sample Keys
            dic_to_process = {k: v for k, v in
                              (sample_data_dict if sample_data_dict else request.form.to_dict()).items() if
                              not k.startswith('sample')}
            data_type = DataTypeMaster()
            data_type.set_data_pool(data_pool=dic_to_process)
            data_type.parse_safe(PhErrorHandlingModes.CONTINUE_ON_ERROR)
            default_data.update({'output_data': data_type.get_output_data()})
        if sample_data_dict:
            default_data.update({'raw_data': sample_data_dict.get('raw_data')})
            default_data.update({'selected_input_format': sample_data_dict.get('input_format')})
            default_data.update({'selected_output_format': sample_data_dict.get('output_format')})
            default_data.update({'asn1_element': sample_data_dict.get('asn1_element')})
            default_data.update({'remarks_list': sample_data_dict.get('remarks_list')})
            default_data.update({'tlv_parsing_of_output': sample_data_dict.get('tlv_parsing_of_output')})
            default_data.update({'sample_processing': sample_processing})
        else:
            default_data.update({'raw_data': request.form['raw_data']})
            default_data.update({'selected_input_format': request.form['input_format']})
            default_data.update({'selected_output_format': request.form['output_format']})
            default_data.update({'asn1_element': request.form['asn1_element']})
            default_data.update({'remarks_list': request.form['remarks_list']})
            default_data.update(
                {'tlv_parsing_of_output': True if 'tlv_parsing_of_output' in request.form.keys() else False})
            default_data.update({'sample_processing': sample_processing})
        return render_template(page_url, **default_data)
    return render_template(page_url, **default_data)


@app.route('/tlvPlay', methods=('GET', 'POST'))
def tlvPlay():
    return render_template('wip.html', page='tlvPlay', git_end_point='tlvPlay')


@app.route('/excelPlay', methods=('GET', 'POST'))
def excelPlay():
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
