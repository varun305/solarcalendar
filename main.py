from solarcalendar import GregorianDate, MarsDate

if __name__ == "__main__":
    date = GregorianDate(-1000000, 7, 31)
    offset = date.to_solar_offset()

    print(offset)
    print(GregorianDate.from_solar_offset(offset))

