from flask import Blueprint

# Blueprint Configuration
bp = Blueprint("main", __name__)

from blog.main import main_routes
