import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    bond_price = 0
    coupon_payment = face * couponRate / ppy

    # array of periods
    periods = np.arange(1, m * ppy + 1)
    pv_factor = 1/(1 + y / ppy) ** periods

    # sum of pv coupon payments, pv of face value when mature
    bond_price = np.sum(coupon_payment * pv_factor)
    bond_price += face / (1 + y / ppy) ** (m * ppy)

    return bond_price
