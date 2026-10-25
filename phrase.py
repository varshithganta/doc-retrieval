def phrase_search(query_tokens, positions):
    if not query_tokens:
        return []

    # if any word is missing from the index, no doc can contain the phrase
    for word in query_tokens:
        if word not in positions:
            return []

    # docs that contain ALL the words
    common = set(positions[query_tokens[0]].keys())
    for word in query_tokens[1:]:
        common = common & set(positions[word].keys())

    matches = []
    for doc_id in sorted(common, key=int):          # doc_ids are strings, so sort as numbers
        for p in positions[query_tokens[0]][doc_id]:
            found = True
            for i in range(1, len(query_tokens)):
                if (p + i) not in positions[query_tokens[i]][doc_id]:
                    found = False
                    break
            if found:
                matches.append(doc_id)
                break                                # one hit is enough for this doc
    return matches