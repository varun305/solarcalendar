from solarcalendar import MarsDate

def test_solar_offset_start():
    date1 = MarsDate(1, 1)
    assert date1.to_solar_offset() == 0
    date2 = MarsDate.from_solar_offset(0)
    assert (date2.year, date2.day) == (1, 1)

def test_solar_offset_far_past():
    for offset in range(-100_000_000, -99_999_000):
        date1 = MarsDate.from_solar_offset(offset - 1)
        date2 = MarsDate.from_solar_offset(offset)

        assert date1.to_solar_offset() + 1 == date2.to_solar_offset()
        assert date2.to_solar_offset() == offset

def test_solar_offset_ancient():
    for offset in range(-100_000, -99_000):
        date1 = MarsDate.from_solar_offset(offset - 1)
        date2 = MarsDate.from_solar_offset(offset)

        assert date1.to_solar_offset() + 1 == date2.to_solar_offset()
        assert date2.to_solar_offset() == offset

def test_solar_offset_turning():
    for offset in range(-1000, 1000):
        date1 = MarsDate.from_solar_offset(offset - 1)
        date2 = MarsDate.from_solar_offset(offset)

        assert date1.to_solar_offset() + 1 == date2.to_solar_offset()
        assert date2.to_solar_offset() == offset

def test_solar_offset_future():
    for offset in range(99_000, 100_000):
        date1 = MarsDate.from_solar_offset(offset - 1)
        date2 = MarsDate.from_solar_offset(offset)

        assert date1.to_solar_offset() + 1 == date2.to_solar_offset()
        assert date2.to_solar_offset() == offset
