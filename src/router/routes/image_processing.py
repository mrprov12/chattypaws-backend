from flask import Blueprint
from ..route_handlers.image_processing_handler import ImageProcessingHandler

image_processing_bp = Blueprint('image_processing', __name__)
image_processing_handler = ImageProcessingHandler()

@image_processing_bp.route('/image_processing/process', methods=['POST'])
def image_process():
    return image_processing_handler.process_video()

@image_processing_bp.route('/image_processing/stream_integration', methods=['POST'])
def image_processing_integrate_stream():
    return image_processing_handler.integrate_stream()
