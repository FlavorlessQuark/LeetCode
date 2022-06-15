def longestStrChain(self, words: List[str]) -> int:
        if (len(words) == 1):
            return 1
        
        chains = {}
        
        words.sort(key=len)
        for word in words:
            chains[word] = 1
            for  i in range(len(word)):
                children = word[0:i] + word[i + 1:]
                if (children in chains):
                    chains[word] = max(chains[children] + 1, chains[word])
        return(max(chains.values()))
