import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 897901830

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    x_max = np.max(x)
    return x_max, ( ( x_max - 0.038 ) / ( alpha ) ** ( 1 / len(x) ) ) + 0.038
