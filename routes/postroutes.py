from flask import Blueprint
from controllers import postcontroller

Post_bp = Blueprint("PostBP", __name__, url_prefix="/Posts")
@Post_bp.route("/add", methods=["POST"])
def createPost():
    return postcontroller.createPost()

@Post_bp.route("/view", methods=["GET"])
def viewall():
    return postcontroller.viewAllPosts()