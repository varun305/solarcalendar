from solarcalendar import GregorianDate

def test_solar_offset_start():
    date1 = GregorianDate(1, 1, 1)
    assert date1.to_solar_offset() == 0
    date2 = GregorianDate.from_solar_offset(0)
    assert (date2.year, date2.month, date2.day) == (1, 1, 1)

def test_solar_offset_far_past():
    for offset in range(-100_000_000, -99_999_000):
        date1 = GregorianDate.from_solar_offset(offset - 1)
        date2 = GregorianDate.from_solar_offset(offset)

        assert date1.to_solar_offset() + 1 == date2.to_solar_offset()
        assert date2.to_solar_offset() == offset

def test_solar_offset_past():
    for offset in range(-100_000, -99_000):
        date1 = GregorianDate.from_solar_offset(offset - 1)
        date2 = GregorianDate.from_solar_offset(offset)

        assert date1.to_solar_offset() + 1 == date2.to_solar_offset()
        assert date2.to_solar_offset() == offset

def test_solar_offset_zero():
    for offset in range(-1000, 1000):
        date1 = GregorianDate.from_solar_offset(offset - 1)
        date2 = GregorianDate.from_solar_offset(offset)

        assert date1.to_solar_offset() + 1 == date2.to_solar_offset()
        assert date2.to_solar_offset() == offset

def test_solar_offset_future():
    for offset in range(99_000, 100_000):
        date1 = GregorianDate.from_solar_offset(offset - 1)
        date2 = GregorianDate.from_solar_offset(offset)

        assert date1.to_solar_offset() + 1 == date2.to_solar_offset()
        assert date2.to_solar_offset() == offset
