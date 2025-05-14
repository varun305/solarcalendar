def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def get_days_in_month(year: int, month: int) -> int:
    days = [31, 29 if is_leap_year(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days[month - 1]


def is_valid_date(year: int, month: int, day: int) -> bool:
    return 1 <= month <= 12 and 1 <= day <= get_days_in_month(year, month)


def count_leap_years(year: int) -> int:
    if year < 1:
        return -count_leap_years(abs(year) + 1) - 1
    last_year = year - 1
    return (last_year // 4) - (last_year // 100) + (last_year // 400)


def get_month_and_day(year: int, day_of_year: int) -> tuple[int, int]:
    days = [31, 29 if is_leap_year(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    month = 1
    for days_in_month in days:
        if day_of_year <= days_in_month:
            break
        day_of_year -= days_in_month
        month += 1
    return month, day_of_year


class GregorianDate:
    def __init__(self, year: int, month: int, day: int):
        if not is_valid_date(year, month, day):
            raise ValueError(f"invalid gregorian date {year}-{month}-{day}")
        self.year = year
        self.month = month
        self.day = day

    def to_solar_offset(self) -> int:
        offset = 0
        offset += (self.year - 1) * 365
        offset += count_leap_years(self.year)

        for m in range(1, self.month):
            offset += get_days_in_month(self.year, m)

        offset += self.day
        offset -= 1

        return offset

    @staticmethod
    def from_solar_offset(offset: int) -> 'GregorianDate':
        low = int(offset / 366) - 1
        high = int(offset / 365) + 1

        if low > high:
            low, high = high, low

        while low <= high:
            mid = (low + high) // 2
            mid_offset = GregorianDate(mid, 1, 1).to_solar_offset()
            if mid_offset <= offset:
                low = mid + 1
            else:
                high = mid - 1

        year = high
        year_offset = GregorianDate(year, 1, 1).to_solar_offset()

        month, day = get_month_and_day(year, offset - year_offset + 1)
        return GregorianDate(year, month, day)

    def __repr__(self):
        return f"{self.year:d}-{self.month:02d}-{self.day:02d}"
