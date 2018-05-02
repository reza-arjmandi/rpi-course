import sys
class Calculator:
    def power(self, n, p):
        if p < 0 or n < 0:
            raise ValueError('n and p should be non-negative')
        return n**p;