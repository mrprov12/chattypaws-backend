from flask import Blueprint
from ..route_handlers.notification_handler import NotificationHandler

notification_bp = Blueprint('notification', __name__)
notification_handler = NotificationHandler()

@notification_bp.route('/notification/notification/<int:notification_id>/stream/<int:stream_id>', methods=['GET'])
def notification_get_notification_history(notification_id, stream_id):
    return notification_handler.get_notification_history(notification_id, stream_id)
