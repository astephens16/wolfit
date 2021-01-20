from datetime import datetime, timedelta

from app.helpers import pretty_date


def test_yesterday():
    assert (pretty_date(datetime.utcnow() - timedelta(days=1))) == "Yesterday"
