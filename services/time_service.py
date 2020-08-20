from datetime import datetime, timedelta


class TimeService:

    def get_available_days(self):
        pass

    def from_days_to_iso(self, days: int) -> datetime:
        today = datetime.now()
        delivery_date = today + timedelta(days=days)
        day_of_the_week = delivery_date.weekday()

        if day_of_the_week == 5 or day_of_the_week == 6:
            delivery_date = delivery_date + timedelta(days=2)

        return delivery_date.strftime("%Y-%m-%d %H:%M:%S")


    def from_iso_to_days(self, days: datetime) -> int:
        pass
