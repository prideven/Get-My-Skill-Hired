from accounts import accounts as acc
from accounts.models import InitUserTable
from flask import Flask, request, jsonify

app = Flask(__name__)

#Initializing DB
InitUserTable()

app.add_url_rule("/account/signin", \
    view_func=acc.sign_in, endpoint="SignIn", methods=["GET"])

app.add_url_rule("/account/signup", \
    view_func=acc.sign_up, endpoint="SignUp", methods=["POST"])

app.add_url_rule("/account/signout", \
    view_func=acc.sign_out, endpoint="SignOut", methods=["GET"])

app.add_url_rule("/account/delete/<usertype>", \
    view_func=acc.delete_user, endpoint="DeleteUser", methods=["DELETE"])

app.add_url_rule("/account/profile/<usertype>", \
    view_func=acc.update_profile, endpoint="UpdateProfile", methods=["PUT"])


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, port=8000)

