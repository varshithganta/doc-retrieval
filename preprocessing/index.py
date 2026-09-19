class Index:
    def __init__(self, docs: dict):
        """
        So your input docs is a dict which has doc_id,filename, tokens as int, string, list, types. This should take care of indexing
        basically and also dont think about tokens, they are normalised, stop words removed and shit so you have docs and tokens
        list basically.    

        index={word1: {docid1:frequency, docid2:frequency....}}   

        doc_length={0:len of tokens, 1:len of tokens....}  
        

    """

        self.index={}
        self.doc_length={}
        self.docs=docs
        self.filenames={}
        self.index=self.make_index()


    def make_index(self):
        index={}
        for doc in self.docs:
            doc_id=doc["doc_id"]
            tokens=doc["tokens"]
            
            self.filenames[doc_id]=doc["filename"]
            self.doc_length[doc_id]=len(tokens)

            for token in tokens:
                if(token not in index):
                    index[token]={}

                if doc_id not in index[token]:
                    index[token][doc_id]=0

                index[token][doc_id]+=1
        return index

### Testing purposes
if __name__ == "__main__":
    docs = {
        "doc1": ["quantum", "computing", "quantum"],
        "doc2": ["classical", "computing"],
    }
    idx = Index(docs)
    print(idx.index)
    print(idx.doc_length)