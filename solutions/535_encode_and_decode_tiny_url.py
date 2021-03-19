class Codec:
    
    def __init__(self):
        self.d = {}
        self.cs = string.ascii_letters + string.digits

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        s = ''.join([random.choice(self.cs) for i in range(8)])
        while s in self.d:
            s = ''.join([random.choice(self.cs) for i in range(8)])
        self.d[s] = longUrl
        return s
        
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.d[shortUrl]
