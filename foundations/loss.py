import numpy as np
from numpy.typing import NDArray
import math


class Solution:

    def binary_cross_entropy(self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> float:
        i=0
        j=0
        ans=[]
        while i<len(y_true) and j<len(y_pred):
            if y_true[i]==1:
                ans.append(math.log(y_pred[j]))
            else:
                result=1-y_pred[j]
                ans.append(math.log(result))
            i=i+1
            j=j+1
        prefix_sum=0
        for k in range(len(ans)):
            prefix_sum=prefix_sum+ans[k]
        answer=-prefix_sum/len(ans)
        return round(answer,4)


        

    def categorical_cross_entropy(self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> float:
        ans=[]
        for i in range(len(y_true)):
            for j in range(len(y_true[i])):
                if y_true[i][j]==1:
                    ans.append(math.log(y_pred[i][j]))
        prefix_sum=0
        for k in range(len(ans)):
            prefix_sum=prefix_sum+ans[k]
        answer=-prefix_sum/len(ans)
        return round(answer,4)
                

        
       
