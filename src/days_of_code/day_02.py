"""Day 2: Restaurant Bill Calculator"""


def total_plus_tip(total_int, tip_int):
    return float(total_int) + (float(total_int) * (tip_int / 100))


def split_total_plus_tip(total_int, tip_int, guests_int):
    tpp = total_plus_tip(total_int, tip_int)
    return tpp / float(guests_int)


def main():
    total_int = float(input("What was the total bill? $"))
    tip_int = float(input("What percentage tip would you like to give? "))
    guests_int = float(input("How many people should split the bill? "))
    split_pay = round(split_total_plus_tip(total_int, tip_int, guests_int), 2)
    guest_pay_str = "{:.2f}".format(split_pay)
    return f"Each person should pay ${guest_pay_str}"


if __name__ == "__main__":
    print(main())
