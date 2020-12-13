class Solution:
    def validIPAddress(self, IP: str) -> str:
        if self._is_ipv4(IP):
            return "IPv4"
        elif self._is_ipv6(IP):
            return "IPv6"
        else:
            return "Neither"
        
    def _is_ipv4(self, s):
        p = s.split('.')
        if len(p) != 4:
            return False
        for i in p:
            if not i:
                return False
            for c in i:
                if not c.isdecimal():
                    return False
            if i[0] == '0' and int(i) != 0:
                return False
            if int(i) == 0 and len(i) != 1:
                return False
            if int(i) > 255 or int(i) < 0:
                return False
        return True
    
    def _is_ipv6(self, s):
        p = s.split(':')
        if len(p) != 8:
            return False
        for i in p:
            if not (1 <= len(i) <= 4):
                return False
            for c in i:
                if not ('A' <= c <= 'F' or 'a' <= c <= 'f' or '0' <= c <= '9'):
                    return False
        return True
