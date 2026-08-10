class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        x=init
        if iterations==0:
            return round(init,5)
        for _ in range(iterations):
            gradiant=2*x
            x=x-(learning_rate*gradiant)
        return round(x,5)