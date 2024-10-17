"""
Date: 10.16.2024
Author: KL
Description: Calculate expected shortfall
"""
import numpy as np


def ES(losses, alpha=None, VaR=None):
    """
    Calculate the Expected Shortfall (ES) of losses.
    
    :param losses: array of positively stated loss values
    :param alpha: risk level (e.g., 0.99 for 99%)
    :param VaR: dollar value or percentage specifying the VaR threshold
    :return: Expected Shortfall as the average of losses exceeding VaR
    """
    # If neither alpha nor VaR is provided
    if alpha and VaR is None:
        raise ValueError("Either VaR or alpha must be provided.")
    elif VaR is None:
        # Calculate VaR if not provided
        VaR = np.percentile(losses, 100 * (1-alpha))

    # Get losses that exceed the VaR threshold
    tail_losses = losses[losses > VaR]

    # Calculate expected shortfall
    if len(tail_losses) == 0:
        return 0
    else:
        es_value = np.mean(tail_losses)
        
    return es_value
