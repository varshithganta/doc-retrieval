import math

class Index:
    def __init__(self, docs: dict):
        """
        So your input docs is a dict which has doc_id,filename, tokens as int, string, list, types. This should take care of indexing
        basically and also dont think about tokens, they are normalised, stop words removed and shit so you have docs and tokens
        list basically.    

        index={word1: {docid1:frequency, docid2:frequency....}}   

        doc_length={0:len of tokens, 1:len of tokens....}  
        
        positions={ word1:{docid1:[positions of where it appears]}, word2:{...} }
    """

        self.index={}
        self.positions={}
        self.doc_length={}
        self.docs=docs
        self.filenames={}
        self.index=self.make_index()
        self.doc_norms = self.make_doc_norms()

    def make_index(self):
        index={}
        positions={}
        for doc in self.docs:
            doc_id=doc["doc_id"]
            tokens=doc["tokens"]
            
            self.filenames[doc_id]=doc["filename"]
            self.doc_length[doc_id]=len(tokens)

            for position,token in enumerate(tokens):
                if(token not in index):
                    index[token]={}

                if doc_id not in index[token]:
                    index[token][doc_id]=0
                                                
                index[token][doc_id]+=1

                if token not in positions:
                    positions[token]={}
                if doc_id not in positions[token]:
                    positions[token][doc_id]=[]
                positions[token][doc_id].append(position)
        
        self.positions=positions
        return index
    
    def make_doc_norms(self):
        N = len(self.doc_length)
        sums = {}                                    # doc_id -> sum of weight²
        for word in self.index:
            idf = math.log(N / len(self.index[word]))   # len(...) = number of docs containing the word
            for doc_id, freq in self.index[word].items():
                weight = freq * idf
                if doc_id not in sums:
                    sums[doc_id] = 0
                sums[doc_id] += weight ** 2

        norms = {}
        for doc_id in sums:
            norms[doc_id] = math.sqrt(sums[doc_id])
        return norms
### Testing purposes
if __name__ == "__main__":
    docs = [
    {
        "doc_id": 0,
        "filename": "a.txt",
        "tokens": ["quantum", "computing", "quantum"]
    },
    {
        "doc_id": 1,
        "filename": "b.txt",
        "tokens": ["classical", "computing"]
    }
    ]
    idx = Index(docs)
    print(idx.index)
    print(idx.doc_length)