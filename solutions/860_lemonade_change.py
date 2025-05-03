class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fiver, tenner, twenty = 0, 0, 0
        for b in bills:
            if b == 5:
                fiver += 1
            elif b == 10:
                if fiver == 0:
                    return False
                tenner += 1
                fiver -= 1
            else:
                if tenner >= 1 and fiver >= 1:
                    tenner -= 1
                    fiver -= 1
                elif fiver >= 3:
                    fiver -= 3
                else:
                    return False
        return True
