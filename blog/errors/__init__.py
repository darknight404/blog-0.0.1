from flask import Blueprint

# Blueprint Configuration
bp = Blueprint("errors", __name__)

from blog.errors import handlers
