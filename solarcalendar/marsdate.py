def is_leap_year(year: int) -> bool:
    return year % 10 == 0 or year % 2 == 1


def is_valid_date(year: int, day: int) -> bool:
    return 1 <= day <= 669 if is_leap_year(year) else 668


def count_leap_years(year: int):
    if year < 1:
        return -count_leap_years(abs(year) + 1) - 1
    return (year - 1) // 10 + year // 2


class MarsDate:
    def __init__(self, year: int, day: int):
        if not is_valid_date(year, day):
            raise ValueError(f"invalid mars date {year}-{day}")
        self.year = year
        self.day = day

    def to_solar_offset(self) -> int:
        offset = 0
        offset += (self.year - 1) * 668
        offset += count_leap_years(self.year)

        offset += self.day
        offset -= 1

        return offset

    @staticmethod
    def from_solar_offset(offset: int) -> 'MarsDate':
        low = int(offset / 669) - 1
        high = int(offset / 668) + 1

        while low <= high:
            mid = (low + high) // 2
            mid_offset = MarsDate(mid, 1).to_solar_offset()
            if mid_offset <= offset:
                low = mid + 1
            else:
                high = mid - 1

        year = high
        year_offset = MarsDate(year, 1).to_solar_offset()

        return MarsDate(year, offset - year_offset + 1)

    def __repr__(self):
        return f"{self.year:d}-{self.day:02d}"
