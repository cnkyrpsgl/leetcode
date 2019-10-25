class Solution:
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        ip4, ip6 = IP.split("."), IP.split(":")
        if len(ip4) == 4:
            for num in ip4:
                try: 
                    if not (num[0] in string.digits and int(num) < 256 and (num[0] != "0" or num == "0")): return "Neither"
                except: return "Neither"
            return "IPv4"
        elif len(ip6) == 8:
            for num in ip6:
                try: 
                    if not (num[0] in string.hexdigits and 0 <= int(num, 16) and len(num) <= 4): return "Neither"
                except: return "Neither"
            return "IPv6"
        return "Neither"