from ..extensions import db


class StreamCredential(db.Model):
    __tablename__ = "stream_credentials"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    stream_type = db.Column(db.String(50), nullable=False)  # 'rtsp' or 'onvif'
    url = db.Column(db.String(255))
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
