import numpy as np

def getBondDuration(y, face, couponRate, m, ppy = 1):
    bond_price = 0
    # remember to factor in multiple payments per year
    coupon_payment = face * couponRate / ppy
    periods = np.arange(1, m * ppy + 1)
    pv_factor = 1 / ((1 + y / ppy) ** periods)

    # calculate bond price
    bond_price = (np.sum(coupon_payment * pv_factor) 
                  + face / (1 + y / ppy) ** (m * ppy))

    # calculate weights
    cash_flows = np.full_like(periods, coupon_payment)
    # add face value to the last period's cash flow
    cash_flows[-1] += face
    weights = pv_factor * cash_flows / bond_price

    # calculate duration, scale back in year
    duration = np.sum(weights * periods)
    duration /= ppy

    return duration
