
from ranking import rank_bm25

index = {
    "quantum": {"0": 2, "1": 1},
    "computing": {"0": 1, "1": 1, "2": 1},
    "classical": {"1": 2}
}

doc_length = {
    "0": 3,
    "1": 4,
    "2": 2
}

query_tokens = ["quantum", "computing"]

results = rank_bm25(
    query_tokens,
    index,
    doc_length,
    k=3
)

for doc_id, score in results:
    print(f"Document {doc_id}: {score:.4f}")