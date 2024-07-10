# routes/image_processing.py
from flask import Blueprint, request, jsonify
from ..services.image_processing_service import ImageProcessingService

image_processing_bp = Blueprint("image_processing", __name__)
image_processing_service = ImageProcessingService()


@image_processing_bp.route("/process_video", methods=["POST"])
def process_video():
    response = image_processing_service.process_video()
    return jsonify(response)


@image_processing_bp.route("/integrate_stream", methods=["POST"])
def integrate_stream():
    data = request.json
    stream_url = data.get("stream_url")
    response = image_processing_service.integrate_stream(stream_url)
    return jsonify(response)


@image_processing_bp.route("/store_results", methods=["POST"])
def store_results():
    data = request.json
    processing_results = data.get("processing_results")
    response = image_processing_service.store_processing_results(processing_results)
    return jsonify(response)
