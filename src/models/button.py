from ..extensions import db


class Button(db.Model):
    __tablename__ = "buttons"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    pet_id = db.Column(db.Integer, db.ForeignKey("pets.id"))
    tile_id = db.Column(db.Integer, db.ForeignKey("tiles.id"), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    position_x = db.Column(db.Integer)
    position_y = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp(),
    )
