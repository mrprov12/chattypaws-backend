# tests/test_services.py (continuation)

from src.services.notification_service import NotificationService
from src.models import db, User, Notification


def test_get_notification_history(db):
    user = User(username="testuser", password_hash="hash", email="test@example.com")
    db.session.add(user)
    db.session.commit()
    notification = Notification(user_id=user.id, message="test notification")
    db.session.add(notification)
    db.session.commit()

    service = NotificationService()
    response = service.get_notification_history(notification.id, 1)
    assert "notifications" in response
