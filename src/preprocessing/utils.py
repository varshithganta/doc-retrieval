import os
from pypdf import PdfReader
from docx import Document
import re

def preprocess(text):
    tokens=tokenize(text)
    normal_tokens=normalise(tokens)
    filtered=remove_stopwords(normal_tokens)

    return filtered


def tokenize(text):
    return re.findall(r"[A-Za-z0-9]+", text)

def normalise(tokens):
    normalised=[]
    for token in tokens:
        normalised.append(token.lower())
    return normalised

def remove_stopwords(tokens):   
    output_tokens=[]

    default_stopwords={"i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him",
      "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves",
        "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being",
        "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", 
        "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
        "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further",
        "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more",
        "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too",
                "very", "s", "t", "can", "will", "just", "don", "should", "now"}

    for token in tokens:
        if token not in default_stopwords:
            output_tokens.append(token)
    return output_tokens


