import math

def rank_tfidf(query_tokens, index, doc_length,k=5):
    N=len(doc_length) #total docs
    scores={}

    for word in query_tokens:

        if word not in index:
            continue

        word_freq=len(index[word])
        idf=math.log(N/word_freq) # how relevant is this word like rare is this actually?

        for doc_id, freq in index[word].items():
            if doc_id not in scores:
                scores[doc_id]=0

            scores[doc_id]+=freq*idf

    ranked=sorted(scores.items(), key=lambda x:x[1], reverse=True)
    return ranked[:k]

            

