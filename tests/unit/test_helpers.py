from datetime import datetime, timedelta

from app.helpers import pretty_date

def test_yesterday():
    assert (pretty_date(datetime.utcnow() - timedelta(days = 1))) == "Yesterday"

def test_days_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(days = 6))) == "6 days ago"
