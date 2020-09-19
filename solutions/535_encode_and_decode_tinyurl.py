class Codec:
    
    def __init__(self):
        self.urls = {}
    
    def gen_url(self):
        """Running time: O(1)
        """
        char = string.digits + string.ascii_lowercase
        s = ''
        for i in range(6):
            s += random.choice(char)
        return s

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        Running time: O(1)
        """
        url = self.gen_url()
        while url in self.urls:
            url = gen_url()
        self.urls[url] = longUrl
        return url
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        Running time: O(1)
        """
        return self.urls[shortUrl]
        