from FastClustering import Tokenizer

class Generator:
    '''
    Class to generate patterns
    '''
    def __init__(self):
        self.wildcard = '*'

    def generate(self, X):
        tokenizer = Tokenizer()
        tokens = tokenizer.transform(X)
        pattern = tokens[0]
        for i in range(1, len(X)):
            len_p = len(pattern)
            len_t = len(tokens[i])
            if len_p < len_t:
                for j in range(0, len_t - len_p):
                    pattern.append(self.wildcard)
                
                len_p = len_t
            
            for j in range(0, len_t):
                if pattern[j] == self.wildcard:
                    continue
                    
                if pattern[j] == tokens[i][j]:
                    continue
                    
                pattern[j] = self.wildcard
        
        return " ".join(pattern)