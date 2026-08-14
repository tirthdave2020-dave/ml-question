import numpy as np
from numpy.typing import NDArray

class Solution:

    def get_model_prediction(self, X: NDArray[np.float64], weights: NDArray[np.float64]) -> NDArray[np.float64]:
        ans=[]
        for i in range(len(X)):
            total=0
            for j in range(len(weights)):
                total=total+X[i][j]*weights[j]
            ans.append(round(total,5))
        return ans
        

    def get_error(self, model_prediction: NDArray[np.float64], ground_truth: NDArray[np.float64]) -> float:
        i=0
        j=0
        ans=[]
        answer=[]
        prefix_sum=0
        mse=0
        while i<len(model_prediction) and j<len(ground_truth):
            mse=mse+(model_prediction[i][0]-ground_truth[j][0])**2
            i=i+1
            j=j+1
        return round(mse/len(model_prediction),5)