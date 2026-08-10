import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        ans=[-1]*len(z)
        for i in range(len(z)):
           ans[i]=round(float(1/(1+np.exp(-z[i]))),5)
        return (np.array(ans, dtype=np.float64))
    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        ans=[-1]*len(z)
        for i in range(len(z)):
            ans[i]=round(float(max(0,z[i])),5)
        return np.array(ans, dtype=np.float64)