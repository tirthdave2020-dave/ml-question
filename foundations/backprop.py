import numpy as np
from numpy.typing import NDArray
from typing import Tuple
import math


class Solution:
    def backward(self, x: NDArray[np.float64], w: NDArray[np.float64], b: float, y_true: float) -> Tuple[NDArray[np.float64], float]:
        prefix_sum=0
        for i in range(len(x)):
            prefix_sum=prefix_sum+(x[i]*w[i])
        prefix_sum=prefix_sum+b
        sigmoid=1 / (1 + math.exp(-prefix_sum))
        error=sigmoid-y_true
        dw=sigmoid*(1-sigmoid)
        dx=dw*error
        result=[]
        for i in range(len(x)):
            result.append(round(dx*x[i],5))
        return result,round(dx,5)
        
