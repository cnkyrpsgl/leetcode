# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        host = startUrl[:(startUrl + '/').find('/', startUrl.find('//') + 2)]
        q, seen = [startUrl], {startUrl}
        for url in q:
            for nex in htmlParser.getUrls(url):
                if nex[:(nex + '/').find('/', nex.find('//') + 2)] == host and nex not in seen:
                    q.append(nex)
                    seen.add(nex)
        return q