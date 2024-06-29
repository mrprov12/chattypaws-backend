import unittest
import os
from dotenv import load_dotenv

from ..app import process_rtsp_video_stream

# Load environment variables from .env file
load_dotenv()


class TestApp(unittest.TestCase):

    def setUp(self):
        self.rtsp_url = os.getenv("RTSP_URL")
        self.username = os.getenv("STREAM_USERNAME")
        self.password = os.getenv("STREAM_PASSWORD")

    def test_process_video_stream(self):
        try:
            process_rtsp_video_stream(self.rtsp_url, self.username, self.password)
        except Exception as e:
            self.fail(f"process_video_stream() raised {e} unexpectedly!")

if __name__ == "__main__":
    unittest.main()
