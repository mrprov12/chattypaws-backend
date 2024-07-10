from ..extensions import db


class ProcessingResult(db.Model):
    __tablename__ = "processing_results"
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    button_press = db.Column(db.Boolean, nullable=False)
    additional_data = db.Column(db.JSON, nullable=True)
