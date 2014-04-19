'''
Created on 01-Dec-2013

@author: Sumukha TV
'''
import nltk

def entityExtractor(text):
    stopWords = list(set(nltk.corpus.stopwords.words('english')))
    sentences = nltk.sent_tokenize(text)
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    chunked_sentences = nltk.batch_ne_chunk(tagged_sentences, binary=True)
    
    entities = []
    for tree in chunked_sentences:
        entities.extend(get_entity_names(tree))
 
    entities = list(set(entities))
    entsPerfect = []
    for e in entities:
        if e not in stopWords:
            entsPerfect.append(e)
    return entsPerfect

def get_entity_names(t):
    entities = []
    
    if hasattr(t, 'node') and t.node:
        if t.node == 'NE':
            entities.append(' '.join([childNode[0] for childNode in t]))
        else:
            for childNode in t:
                entities.extend(get_entity_names(childNode))
                
    return entities

if __name__ == '__main__':
    text = open("text.txt").read()
    print entityExtractor(text)
