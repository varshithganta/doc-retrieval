from preprocessing.converter import *
from preprocessing.index import Index
import argparse
import sys
import os 
import json
from ranking import *

cache_file="cache.json"
def write_cache(index, doc_length,filenames, path=cache_file):
    with open(path, "w") as f:
        json.dump({"index":index, 
                   "doc_length":doc_length,
                   "filenames":filenames},f)

def read_cache(path=cache_file):
    with open(path, "r") as f:
        data=json.load(f)
        index=data["index"]
        doc_length=data["doc_length"]
        filenames=data["filenames"]
        return index, doc_length,filenames



parser=argparse.ArgumentParser(description="Document Retreival")

parser.add_argument( "--path", type=str,default="sampledata" ,help="Path to the folder where the files are present")
parser.add_argument("--k", type=int, default=5, help="returns top k documents which are relevant")
parser.add_argument("--rebuild", action="store_true",default=False,  help="Rebuilds the whole indexing by going throuhg the document path again")
parser.add_argument("--query", type=str,required=True, help="This is the search term or phrase or whatever we are looking for in the docs")
args=parser.parse_args()



if(args.rebuild or not os.path.exists(cache_file)):

    if not os.path.exists(args.path):
        raise ValueError("Specified path doesnt exist")

    documents=file_loader(args.path)
    index1=Index(documents)

    index=index1.index
    doc_length=index1.doc_length
    filenames=index1.filenames

    write_cache(index, doc_length, filenames)

else:
    index, doc_length,filenames=read_cache(cache_file)

if(args.k>len(doc_length)):
    raise ValueError("Value of K is larger than doc length")

query_tokens=preprocess(args.query)

results=rank_tfidf(query_tokens,index, doc_length=doc_length,k=args.k)



if not results:
    print("No matching documents")
    sys.exit(0)
    
rank=1
print("Completed ranking using the TFIDF. Results: ")
print("Query: ", args.query)
for doc_id, score in results:
    print(f"{rank})  Doc_id: {doc_id}, Filename: {filenames[doc_id]}\n Score: {round(score, 3)}, ")
    print("")
    rank+=1


