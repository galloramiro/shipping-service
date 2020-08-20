from freezegun import freeze_time

from services.time_service import TimeService


@freeze_time('2020-08-04')
def test_time_service_from_days_to_iso():
    time_serive = TimeService()
    days = time_serive.from_days_to_iso(5)

    assert days == '2020-08-11 00:00:00'

@freeze_time('2020-08-03')
def test_time_service_from_days_to_iso_in_weekend():
    time_serive = TimeService()
    days = time_serive.from_days_to_iso(5)

    assert days == '2020-08-10 00:00:00'
