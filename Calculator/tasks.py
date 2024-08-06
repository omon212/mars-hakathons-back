def calculate_money(kw_all):
    rate1 = 200   # Rate for consumption up to 200 kWh
    rate2 = 450   # Rate for consumption between 201-1000 kWh
    rate3 = 900   # Rate for consumption between 1001-5000 kWh
    rate4 = 1350  # Rate for consumption between 5001-10000 kWh
    rate5 = 1575  # Rate for consumption above 10000 kWh
    if kw_all <= 200:
        return kw_all * rate1
    elif kw_all <= 1000:
        return (200 * rate1) + ((kw_all - 200) * rate2)
    elif kw_all <= 5000:
        return (200 * rate1) + (800 * rate2) + ((kw_all - 1000) * rate3)
    elif kw_all <= 10000:
        return (200 * rate1) + (800 * rate2) + (4000 * rate3) + ((kw_all - 5000) * rate4)
    else:
        return (200 * rate1) + (800 * rate2) + (4000 * rate3) + (5000 * rate4) + ((kw_all - 10000) * rate5)
