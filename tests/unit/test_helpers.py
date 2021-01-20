from datetime import datetime, timedelta

from app.helpers import pretty_date

def test_yesterday():
    assert (pretty_date(datetime.utcnow() - timedelta(days = 1))) == "Yesterday"

def test_days_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(days = 6))) == "6 days ago"

def test_weeks_ago():
    assert (pretty_date(datetime.utcnow()- timedelta(days = 15))) == "2 weeks ago"

def test_months_ago():
    assert (pretty_date(datetime.utcnow()- timedelta(days = 123))) == "4 months ago"

def test_years_ago():
    assert (pretty_date(datetime.utcnow()- timedelta(days = 700))) == "1 years ago"