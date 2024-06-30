from ..extensions import db


class ButtonPress(db.Model):
    __tablename__ = "button_presses"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    pet_id = db.Column(db.Integer, db.ForeignKey("pets.id"), nullable=False)
    button_id = db.Column(db.Integer, db.ForeignKey("buttons.id"), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    confidence = db.Column(db.Float)
