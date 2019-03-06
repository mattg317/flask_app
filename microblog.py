from app import app, db
from app.models import User, Post


# create shell context that adds the database instance and modesl to the session
# This decorator registers the function as a shell context
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
