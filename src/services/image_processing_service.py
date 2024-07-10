# services/image_processing_service.py
import cv2
from onvif import ONVIFCamera
from ..models import db, ProcessingResult
from ..utils.image_processing_utils import detect_button_press


class ImageProcessingService:
    def process_video(self):
        # Implement the logic to process video feed and store interactions
        return {"message": "Video processed successfully"}, 200

    def integrate_stream(self, stream_url):
        # Implement the logic to integrate a new camera feed stream
        return {"message": "Stream integrated successfully"}, 201

    def store_processing_results(self, results):
        try:
            new_result = ProcessingResult(**results)
            db.session.add(new_result)
            db.session.commit()
            return {
                "message": "Results stored successfully",
                "result_id": new_result.id,
            }, 201
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 400

    def get_rtsp_stream_url(self, onvif_camera):
        media_service = onvif_camera.create_media_service()
        profiles = media_service.GetProfiles()
        token = profiles[0].token
        stream_uri = media_service.GetStreamUri(
            {
                "StreamSetup": {"Stream": "RTP-Unicast", "Transport": "RTSP"},
                "ProfileToken": token,
            }
        )
        return stream_uri.Uri

    def process_rtsp_stream(self, rtsp_url, username, password):
        rtsp_url_with_credentials = f"rtsp://{username}:{password}@{rtsp_url}"
        cap = cv2.VideoCapture(rtsp_url_with_credentials)

        if not cap.isOpened():
            print("Error: Unable to open RTSP stream")
            return

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Unable to read frame from RTSP stream")
                break

            button_press = detect_button_press(frame)
            cv2.imshow("RTSP Stream", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()

    def process_onvif_stream(self, ip, port, username, password):
        camera = ONVIFCamera(ip, port, username, password)
        rtsp_url = self.get_rtsp_stream_url(camera)

        cap = cv2.VideoCapture(rtsp_url)

        if not cap.isOpened():
            print("Error: Unable to open ONVIF stream")
            return

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Unable to read frame from ONVIF stream")
                break

            button_press = detect_button_press(frame)
            cv2.imshow("ONVIF Stream", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()
