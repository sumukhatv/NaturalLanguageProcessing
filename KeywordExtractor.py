'''
Created on 26-Nov-2013

@author: Sumukha TV
'''
import warnings
warnings.filterwarnings("ignore")
from topia.termextract import extract
import re

def getKeyTerms(text):
    
    extractor = extract.TermExtractor()
    text = re.sub(r"[^\w'. ,]", " ", text)
    keyTerms = sorted(extractor(text), key=lambda tup: tup[1], reverse = True)
    kTerms = []
    for kt in keyTerms:
        try:
            unicode(kt[0])            
            kTerms.append(kt[0])
        except:
            pass
    return kTerms

if __name__ == "__main__":
    text = open("text.txt", "r").read()
    kTerms = getKeyTerms(text)
    print kTerms