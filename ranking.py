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

def rank_cosine(query_tokens, index, doc_length, doc_norms, k=5):
    N = len(doc_length)

    # query vector: how many times each word appears in the query
    query_counts = {}
    for word in query_tokens:
        query_counts[word] = query_counts.get(word, 0) + 1

    dot = {}                 # doc_id -> sum of query_weight * doc_weight
    query_norm_sq = 0
    for word, count in query_counts.items():
        if word not in index:
            continue
        idf = math.log(N / len(index[word]))
        q_weight = count * idf
        query_norm_sq += q_weight ** 2
        for doc_id, freq in index[word].items():
            d_weight = freq * idf
            dot[doc_id] = dot.get(doc_id, 0) + q_weight * d_weight

    query_norm = math.sqrt(query_norm_sq)
    if query_norm == 0:      # no known words, or all have idf 0
        return []

    scores = {}
    for doc_id in dot:
        if doc_norms[doc_id] == 0:       # avoid division by zero
            continue
        scores[doc_id] = dot[doc_id] / (query_norm * doc_norms[doc_id])

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return ranked[:k]


            

