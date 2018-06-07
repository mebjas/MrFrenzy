import hashlib

class Deduplication:
    '''
    Class to perform deduplication task
    '''

    def __init__(self):
        self.__hashes = {}

    def transform(self, texts):
        _texts = []
        for text in texts:
            digest = self.__hash(text)
            if not digest in self.__hashes:
                _texts.append(text)
                self.__hashes[digest] = True

        return _texts

    def __hash(self, text):
        h = hashlib.md5(text.encode("utf-8"))
        return h.hexdigest()