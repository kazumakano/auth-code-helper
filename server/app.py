import os.path as path
import flask
import pyotp
import qrcode
from database import Account, db


app = flask.Flask(__name__)

def init() -> None:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///account.db"
    db.init_app(app)
    with app.app_context():
        db.create_all()

@app.route("/account", methods=["POST"])
def post_account() -> tuple[str, int]:
    data = flask.request.get_json()
    db.session.add(Account(name=data["name"], seed=data["seed"]))
    db.session.commit()
    return "Created", 201

@app.route("/code/<name>")
def get_code_by_name(name: str) -> tuple[str, int]:
    return pyotp.TOTP(db.get_or_404(Account, name).seed).now(), 200

@app.route("/qr/<name>")
def save_qr_by_name(name: str) -> tuple[str, int]:
    qrcode.make(f"otpauth://totp/{name}?secret={db.get_or_404(Account, name).seed}&issuer={name}").save(path.join(path.dirname(__file__), "qr/", name + ".png"))
    return "No Content", 204

@app.after_request
def set_headers(res: flask.Response) -> flask.Response:
    res.headers.set("Access-Control-Allow-Origin", "*")
    return res

if __name__ == "__main__":
    import argparse
    import waitress

    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="0.0.0.0", help="specify server host", metavar="HOST")
    parser.add_argument("--port", default=5000, type=int, help="specify server port", metavar="PORT")
    args = parser.parse_args()

    init()
    waitress.serve(app, host=args.host, port=args.port)
    # key_dir = path.join(path.dirname(__file__), "key/")
    # app.run(host=args.host, port=args.port, ssl_context=(path.join(key_dir, "certificate.pem"), path.join(key_dir, "private.pem")))
