# src/routes/notification.py
from flask import Blueprint
from ..services.notification_service import NotificationHandler

notification_bp = Blueprint("notification", __name__)
notification_handler = NotificationHandler()


@notification_bp.route(
    "/notification/<int:notification_id>/stream/<int:stream_id>", methods=["GET"]
)
def notification_get_notification_history(notification_id, stream_id):
    return notification_handler.get_notification_history(notification_id, stream_id)
