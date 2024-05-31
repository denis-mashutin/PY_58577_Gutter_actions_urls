from flask import Blueprint, request

# create the blueprint
router = Blueprint('myrouter', __name__)





@router.route('prefix2/', methods=['GET', 'POST'])
def hello_world():
    return 'Hello, World!'
