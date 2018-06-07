class FastClustering:
    '''
    Class to perform level 1 fast clustering
    '''
    def __init__(self, threshold=0.3):
        self.threshold = threshold
        self.clusters = []
        self.clusterIndex = 0
    
    def transform(self, X):
        clusterLabels = []

        for x in X:
            minDistance = self.threshold
            clusterIndex = -1
            for i, clusterCenter in enumerate(self.clusters):
                d = self.__distance(x, clusterCenter)
                if d < minDistance:
                    minDistance = d
                    clusterIndex = i
            
            if clusterIndex == -1:
                self.clusters.append(x)
                clusterIndex = self.clusterIndex
                self.clusterIndex+= 1
                
            clusterLabels.append(clusterIndex)
            
        return clusterLabels
    
    def getLabelCount(self):
        return self.clusterIndex + 1
    
    def __distance(self, x, y):
        xl = len(x)
        yl = len(y)
        d = xl if xl > yl else yl
        m = xl if xl < yl else yl
        n = 0
        for i in range(0, m):
            if x[i] == y[i]:
                n += 1

        return 1 - (n/d)


class Tokenizer:
    '''
    Class to tokenize strings to array of tokens
    '''
    def __init__(self):
        pass

    def transform(self, texts):
        response = []
        for i, t in enumerate(texts):
            response.append(t.split(" "))
        
        return response