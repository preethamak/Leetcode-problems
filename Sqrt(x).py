class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:  # Handle edge case where x = 0
            return 0
        
        L, R = 1, x

        while L <= R:
            M = (L + R) // 2
            M_sq = M * M

            if M_sq == x:
                return M
            elif M_sq < x:
                L = M + 1
            else:
                R = M - 1

        return R  # The integer square root
