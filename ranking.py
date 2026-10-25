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


def rank_bm25(query_tokens, index, doc_length, k=5, k1=1.5, b=0.75):
    N = len(doc_length)

    if N == 0:
        return []

    avgdl = sum(doc_length.values()) / N
    scores = {}

    for word in query_tokens:
        if word not in index:
            continue

        df = len(index[word])

        idf = math.log((N - df + 0.5) / (df + 0.5) + 1)

        for doc_id, tf in index[word].items():
            dl = doc_length[doc_id]

            denominator = tf + k1 * (
                1 - b + b * dl / avgdl
            )

            term_score = idf * (
                tf * (k1 + 1)
            ) / denominator

            if doc_id not in scores:
                scores[doc_id] = 0

            scores[doc_id] += term_score

    ranked = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return ranked[:k]

            

