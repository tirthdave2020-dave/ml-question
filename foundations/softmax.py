import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        z=z-np.max(z)
        result=[]
        ans=[]
        prefix_sum=0
        for i in range(len(z)):
            result.append(np.exp(z[i]))

        for i in range(len(result)):
            prefix_sum=prefix_sum+result[i]
        for i in range(len(result)):
            ans.append(round(result[i]/prefix_sum,4))
            
        return ans

        

        