import re
from sklearn.feature_extraction.text import CountVectorizer
from syllable import sylco


def calculate_features(para):
    vectorizer = CountVectorizer()
    analyzer = vectorizer.build_analyzer()
    sentences = re.split(r"(?<=\.)\s+", para.strip())
    all_words = re.split(r'\s+', para.strip())
    words = analyzer(para)
    total_words = len(words)
    total_characters = reduce(lambda t, w: t + len(w), words, 0)
    total_syllables = reduce(lambda t, w: t + sylco(w), all_words, 0)
    avg_word_length = total_characters / total_words
    avg_syllable_per_word = total_syllables * 1.0 / total_words
    avg_sentence_length = reduce(lambda t, s: t + len(analyzer(s)), sentences, 0) / len(sentences)

    return [avg_word_length, len(all_words), avg_syllable_per_word, total_syllables, avg_sentence_length, len(sentences)]
