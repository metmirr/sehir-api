from . import auth
from app.models import City

@auth.route('/', methods=['GET'])
def index():
    return 'Hello World'
