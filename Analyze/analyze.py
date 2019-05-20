try:
    from konlpy.tag import Kkma
except ImportError:
    print("Please install konlpy\n=> pip install konlpy")
    import sys
    sys.exit()

class Analyze:
    def __init__(self, string):
        self.string = u"%s" %string
        self.kkma = Kkma()

    def parse_phrase_to_morphemes(self):
        return self.kkma.morphs(self.string)
    
    def noun_extractor(self):
        return self.kkma.nouns(self.string)
