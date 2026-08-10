import numpy as np
from numpy.typing import NDArray


class Solution:
    def forward(self, x: NDArray[np.float64], w: NDArray[np.float64], b: float, activation: str) -> float:
        i=0
        j=0
        ans=0
        while i<len(x) and j<len(w):
            ans=ans+(x[i]*w[j])
            i=i+1
            j=j+1
        ans=ans+b
        if activation=="relu":
            ans=max(0,ans)
        elif activation=='sigmoid':
            ans = 1 / (1 + np.exp(-ans))

        return float(round(ans,5))
