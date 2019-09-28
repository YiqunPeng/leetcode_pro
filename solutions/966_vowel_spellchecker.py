class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        """Hash table.

        Running time: O(n + m) where n is the length of queries and m is the length of wordlist.
        """
        def get_wild(word):
            wild = ''
            for c in word:
                if c in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                    wild += '*'
                else:
                    wild += c 
            return wild.lower()
        
        worddict = set()
        wordcapdict = {}
        wordvoweldict = {}
        
        for word in wordlist:
            worddict.add(word)
            
            if word.lower() not in wordcapdict:
                wordcapdict[word.lower()] = word

            wild = get_wild(word)
            if wild not in wordvoweldict:
                wordvoweldict[wild] = word
        
        for i in range(len(queries)):
            wild = get_wild(queries[i])
                        
            if queries[i] in worddict:
                continue
            elif queries[i].lower() in wordcapdict:
                queries[i] = wordcapdict[queries[i].lower()]
            elif wild in wordvoweldict:
                queries[i] = wordvoweldict[wild]
            else:
                queries[i] = ''
        
        return queries