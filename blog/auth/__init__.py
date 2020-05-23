from flask import Blueprint

# Blueprint Configuration
bp = Blueprint("auth", __name__)

from blog.auth import auth_routes
