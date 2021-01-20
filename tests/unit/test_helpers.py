from datetime import datetime, timedelta

from app.helpers import pretty_date

def test_seconds_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(seconds = 43))) == "43 seconds ago" 

def test_minute_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(minutes = 1))) == "a minute ago"

def test_minutes_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(minutes = 2))) == "2 minutes ago"

def test_hour_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(hours = 1))) == "an hour ago"

def test_hours_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(hours = 5))) == "5 hours ago"

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