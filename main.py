from solarcalendar import GregorianDate, MarsDate

if __name__ == "__main__":
    date = GregorianDate(-43, 3, 15)
    offset = date.to_solar_offset()

    mars_solar_offset = (offset - 570930) / 1.027491
    mars_date = MarsDate.from_solar_offset(int(mars_solar_offset))
    print(mars_date)
