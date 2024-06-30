# tests/test_services.py (continuation)

from src.services.image_processing_service import ImageProcessingService
from src.models import db, ProcessingResult


def test_process_video():
    service = ImageProcessingService()
    response = service.process_video()
    assert response["message"] == "Video processed successfully"


def test_integrate_stream(db):
    service = ImageProcessingService()
    stream_url = "http://example.com/stream"
    response = service.integrate_stream(stream_url)
    assert response["message"] == "Stream integrated successfully"


def test_store_processing_results(db):
    service = ImageProcessingService()
    results = {
        "timestamp": "2024-06-30T12:34:56",
        "button_press": True,
        "additional_data": {"example": "data"},
    }
    response, status_code = service.store_processing_results(results)
    assert status_code == 201
    assert response["message"] == "Results stored successfully"
    assert "result_id" in response
