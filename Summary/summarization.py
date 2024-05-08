# summary/summarization.py
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

LANGUAGE = "english"
SENTENCES_COUNT = 5  # Adjust the number of sentences as needed

def generate_summary(text):
    parser = PlaintextParser.from_string(text, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    # Generate summary with specified number of sentences
    summary = summarizer(parser.document, SENTENCES_COUNT)
    
    # Join the sentences into a single string
    return ' '.join(str(sentence) for sentence in summary)
