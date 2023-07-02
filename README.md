# Process
- Document Collection: 
Start with a collection of documents that you want to index and make searchable. These documents can be in various formats such as text files, web pages, or any other structured/unstructured data.

- Preprocessing: 
Apply text preprocessing techniques such as tokenization, lowercase conversion, stop word removal, and lemmatization to the documents and the search query. This ensures that they are represented consistently and without noise.

- Document vector representations:
Use a suitable vectorization technique, such as TF-IDF, to convert the preprocessed documents and the search query into numerical vector representations. This step transforms the text into a format that can be used for cosine similarity calculations.

- Calculate the cosine similarity between the search query and each document:
Compute the cosine similarity between the vector representation of the search query and each document using the cosine similarity formula. The higher the cosine similarity score, the more similar the document is to the search query.

- Rank the documents based on cosine similarity scores:
Sort the documents in descending order of their cosine similarity scores. The document with the highest cosine similarity score is considered the most relevant to the search query.
