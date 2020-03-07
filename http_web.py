from flask import Flask, session,render_template,send_file
from mysql_getdata import BD, get_date

app = Flask(__name__)


@app.route('/')
def hello():
    bd = BD("visitors")
    if session == {}:
        session['id'] = bd.get_next_id()
    bd.set_visit(session['id'], get_date())
    count = bd.get_all(session['id'])
    print(count)
    return "Your visits is {}.\n".format(count)


@app.route('/D/')
def hello_d():
    bd = BD("visitors")
    if session == {}:
        session['id'] = bd.get_next_id()
    bd.set_visit(session['id'], get_date())
    count = bd.get_day(session['id'], get_date())
    return "Your visits is {}.\n".format(count)


@app.route('/M/')
def hello_m():
    bd = BD("visitors")
    if session == {}:
        session['id'] = bd.get_next_id()
    bd.set_visit(session['id'], get_date())
    count = bd.get_month(session['id'], get_date())
    return "Your visits is {}.\n".format(count)


@app.route('/Y/')
def hello_y():
    bd = BD("visitors")
    if session == {}:
        session['id'] = bd.get_next_id()
    bd.set_visit(session['id'], get_date())
    count = bd.get_year(session['id'], get_date())
    return "Your visits is {}.\n".format(count)


@app.route('/img/')
def hello_I():
    bd = BD("visitors")
    if session == {}:
        session['id'] = bd.get_next_id()
    bd.set_visit(session['id'], get_date())
    return send_file('p.png')


def main():
    app.debug = False
    app.secret_key =\
        b'\xcbt\x0f\xbfAQd\x16\x91\xa4\x1f\x8b\xa2j\xc8k\x19^\xf19\xf4Bq\xe1'
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    main()
