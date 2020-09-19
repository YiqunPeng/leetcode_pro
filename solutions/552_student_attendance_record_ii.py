class Solution:
    def checkRecord(self, n: int) -> int:
        """DP.

        Running time: O(n).
        """
        if n == 1:
            return 3
        
        mod = 10 ** 9 + 7
        
        no_a_p = 2
        no_a_l = 1
        no_a_ll = 1
        a_a = 2
        a_p = 1
        a_l = 1
        a_ll = 0
        
        for i in range(3, n + 1):
            n_no_a_p = no_a_p + no_a_l + no_a_ll
            n_no_a_l = no_a_p
            n_no_a_ll = no_a_l
            
            n_a_a = no_a_p + no_a_l + no_a_ll
            n_a_p = a_a + a_p + a_l + a_ll
            n_a_l = a_a + a_p
            n_a_ll = a_l
            
            no_a_p = n_no_a_p % mod
            no_a_l = n_no_a_l % mod
            no_a_ll = n_no_a_ll % mod
            a_a = n_a_a % mod
            a_p = n_a_p % mod
            a_l = n_a_l % mod
            a_ll = n_a_ll % mod
            
        return (no_a_p + no_a_l + no_a_ll + a_a + a_p + a_l + a_ll) % mod