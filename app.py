from webapp import create_app, db
from webapp.models import User

# env = os.environ.get('WEBAPP_ENV', 'dev')
# app = create_app('config.%sConfig' % env.capitalize())
app = create_app()


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)


"""
    set debug=False in production mode
"""
if __name__ == '__main__':
    app.run(debug=True)
