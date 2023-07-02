import pandas as pd
import json
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def tokenizer(statement):
    # Filter out stop words & special characters
    stop_words = set(stopwords.words('english'))
    special_characters = '''!()-—[]{};:'"\, <>./?@#$%^&*_~+='''
    tokens = word_tokenize(statement)
    return [token.lower() for token in tokens if token.lower() not in stop_words and token not in special_characters]

def lemmatize_stmt(statement):    
    lemmatizer = WordNetLemmatizer()
    filtered_tokens = tokenizer(statement)
    lemmatize_tokens = []
    for word in filtered_tokens:
        lemma = lemmatizer.lemmatize(word)
        lemmatize_tokens.append(lemma)
    return ' '.join(lemmatize_tokens)

def search_engine(query):
    lemmatized_query = [lemmatize_stmt(query)]
    with open('./scraped_data/rcih_research_output.json') as f:
        rcih_research = json.loads(f.read())
    df = pd.DataFrame.from_dict(rcih_research)
    documents = []
    vectorizer = TfidfVectorizer()
    document_vectors = vectorizer.fit_transform(df['imp'])
    query_vector = vectorizer.transform(lemmatized_query)
    cosine_similarities = cosine_similarity(query_vector, document_vectors).flatten()
    sorted_indices = cosine_similarities.argsort()[::-1]
    for i in range(10):
        index = sorted_indices[i]
        relevant_document = df.iloc[index].to_dict()
        documents.append(relevant_document)
    return documents
