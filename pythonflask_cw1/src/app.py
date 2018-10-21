from flask import Flask, render_template



app = Flask(__name__)
app.config.from_object('config')



@app.route('/')
def home():
    return render_template('pages/home.html')


@app.route('/users')
def users():
    return render_template('pages/users.html')


@app.route('/users/<name>')
def user_detail(name):
    return render_template('pages/user_detail.html', name=name)


@app.route('/repositories')
def repositories():
    return render_template('pages/repositories.html')


@app.route('/repositories/<owner>/<repo>')
def repo_detail(owner, repo):
    return render_template('pages/repo_detail.html', owner=owner, repo=repo)


@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


if __name__ == '__main__':
    app.run()
