class Solution:
    
    def __init__(self):
        self.one_to_nineteen = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        self.tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        self.thousands = ['', 'Thousand', 'Million', 'Billion']
    
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'        
        res = ''
        i = 0
        while num != 0:
            if num % 1000 != 0:
                res = self._helper(num % 1000) + self.thousands[i] + ' ' + res
            num //= 1000
            i += 1
        return res.strip()

    def _helper(self, num):
        if num == 0:
            return ''
        if num < 20:
            return self.one_to_nineteen[num-1] + ' '
        if num < 100:
            return self.tens[num // 10 - 2] + ' ' + self._helper(num % 10)
        return self.one_to_nineteen[num // 100 - 1] + ' Hundred ' + self._helper(num % 100)
