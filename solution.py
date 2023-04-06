import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 897901830

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    x_max = numpy.max(x)
    return ( x_max / ( 1 - alpha / 2 ) ** ( 1 / len(x) ) ), \
           ( x_max / ( alpha / 2 ) ** ( 1 / len(x) ) )
