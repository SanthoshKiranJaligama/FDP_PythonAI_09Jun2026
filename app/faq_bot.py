import os
import sys
import math
import re

class NumPyLikeArray:
    def __init__(self, data):
        self.data = data

    def flatten(self):
        if len(self.data) > 0 and isinstance(self.data[0], list):
            flat_data = [item for sublist in self.data for item in sublist]
            return NumPyLikeArray(flat_data)
        return NumPyLikeArray(self.data)

    def argmax(self):
        if not self.data:
            return 0
        return self.data.index(max(self.data))

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return repr(self.data)

class TfidfVectorizer:
    def __init__(self):
        self.vocabulary_ = {}
        self.idf_ = {}
        self.feature_names_ = []

    def _tokenize(self, text):
        return re.findall(r'\b\w\w+\b', text.lower())

    def fit_transform(self, raw_documents):
        tokenized_docs = [self._tokenize(doc) for doc in raw_documents]
        
        vocab = set()
        for tokens in tokenized_docs:
            vocab.update(tokens)
        self.feature_names_ = sorted(list(vocab))
        self.vocabulary_ = {word: i for i, word in enumerate(self.feature_names_)}
        
        df = {word: 0 for word in self.feature_names_}
        for tokens in tokenized_docs:
            unique_tokens = set(tokens)
            for token in unique_tokens:
                if token in df:
                    df[token] += 1
                    
        n = len(raw_documents)
        for word in self.feature_names_:
            self.idf_[word] = math.log((1 + n) / (1 + df[word])) + 1
            
        return self.transform(raw_documents)

    def transform(self, raw_documents):
        vectors = []
        for doc in raw_documents:
            tokens = self._tokenize(doc)
            tf = {}
            for token in tokens:
                if token in self.vocabulary_:
                    tf[token] = tf.get(token, 0) + 1
            
            tfidf_vec = [0.0] * len(self.vocabulary_)
            for token, count in tf.items():
                idx = self.vocabulary_[token]
                tfidf_vec[idx] = count * self.idf_[token]
                
            sq_sum = sum(x**2 for x in tfidf_vec)
            if sq_sum > 0:
                l2_norm = math.sqrt(sq_sum)
                tfidf_vec = [x / l2_norm for x in tfidf_vec]
                
            vectors.append(tfidf_vec)
        return vectors

def cosine_similarity(query_vector, tfidf_matrix):
    q = query_vector[0]
    similarities = []
    for doc_vec in tfidf_matrix:
        dot_product = sum(qi * di for qi, di in zip(q, doc_vec))
        similarities.append(dot_product)
    return NumPyLikeArray([similarities])

# Knowledge base of Question-Answer pairs
FAQ_KB = {
    "What is the Faculty Development Programme?": 
        "The Faculty Development Programme (FDP) is designed to enhance the teaching and research skills of faculty members.",
    "How do I install Python for the hands-on session?": 
        "You can install Python 3.11 or newer from python.org and ensure you check 'Add Python to PATH' during installation.",
    "What is the purpose of virtual environments?": 
        "Virtual environments allow you to isolate project-specific dependencies to prevent conflicts between different projects.",
    "How does the Student Risk Predictor work?": 
        "It computes a weighted normalized score from attendance, internal marks, and assignment marks, then classifies the student based on an environment-specific threshold.",
    "What is the role of CI/CD in AI engineering?": 
        "CI/CD automates the testing, integration, and deployment of code and models, ensuring reliable and repeatable releases."
}

def get_answer(query, confidence_threshold):
    """
    Finds the best matching FAQ question using TF-IDF vectorization and cosine similarity.
    Returns the answer if the similarity score is >= confidence_threshold, otherwise a fallback.
    """
    questions = list(FAQ_KB.keys())
    
    # Initialize TF-IDF Vectorizer
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(questions)
    
    # Vectorize the user query
    query_vector = vectorizer.transform([query])
    
    # Compute Cosine Similarity between the query and all KB questions
    similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()
    
    # Identify the best matching question
    best_match_idx = similarities.argmax()
    best_similarity = similarities[best_match_idx]
    
    if best_similarity >= confidence_threshold:
        return FAQ_KB[questions[best_match_idx]], best_similarity, questions[best_match_idx]
    else:
        return "I'm sorry, I cannot answer this question with high confidence.", best_similarity, None

def main():
    # Retrieve configuration from environment variables
    app_env = os.environ.get("APP_ENV", "dev")
    app_env_lower = app_env.lower()
    
    # Pick default confidence based on selected environment
    if app_env_lower == "test":
        default_confidence = 0.60
    elif app_env_lower == "dev":
        default_confidence = 0.20
    else:
        default_confidence = 0.40

    confidence_str = os.environ.get("FAQ_CONFIDENCE")
    if confidence_str is not None:
        try:
            confidence_threshold = float(confidence_str)
        except ValueError:
            confidence_threshold = default_confidence
    else:
        confidence_threshold = default_confidence

    print(f"Environment: {app_env}")
    print(f"FAQ Confidence Threshold: {confidence_threshold}")

    # Determine user query
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        print(f"Query provided via CLI: '{query}'")
    else:
        # Check if interactive
        is_interactive = sys.stdin.isatty() and not os.environ.get("CI")
        if is_interactive:
            print("\n--- FAQ Bot Interactive Mode ---")
            print("Frequently Asked Questions Topics:")
            for idx, q in enumerate(FAQ_KB.keys(), 1):
                print(f"  {idx}. {q}")
            query = input("\nEnter your question: ").strip()
            if not query:
                query = "how to install python for hands-on?"
                print(f"No text entered. Using default query: '{query}'")
        else:
            # Default query for demonstration
            query = "how to install python for hands-on?"
            print(f"No query provided via arguments in non-interactive environment. Using default query: '{query}'")

    answer, similarity, matched_question = get_answer(query, confidence_threshold)
    
    print("\n--- FAQ Bot Response ---")
    print(f"User Query   : '{query}'")
    print(f"Similarity   : {similarity:.4f}")
    if matched_question:
        print(f"Matched Qn   : '{matched_question}'")
    print(f"Response     : {answer}")
    print("------------------------\n")

if __name__ == "__main__":
    main()
