class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        res = [startUrl]
        seen = set(res)
        q = deque([startUrl])
        while q:
            url = q.popleft()
            host = self._get_host(url)
            nxt_urls = htmlParser.getUrls(url)
            for u in nxt_urls:
                if u not in seen and self._get_host(u) == host:
                    seen.add(u)
                    res.append(u)
                    q.append(u)
        return res
    
    def _get_host(self, url):
        return url[7:].split('/')[0]
