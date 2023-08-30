from flask import render_template


def handle_requests():
    return render_template('wip.html', page='tlvPlay', git_end_point='tlvPlay')
