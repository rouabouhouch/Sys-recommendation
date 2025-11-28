# mood_classifier.py

from transformers import pipeline

# zero-shot classifier
classifier = pipeline("zero-shot-classification",
                      model="facebook/bart-large-mnli")

# labels
MOODS = ["happy", "chill", "energetic", "sad", "heartbreak"]

def classify_mood(text):
    """
    Classify a song title (or lyrics later) into a mood.
    """
    result = classifier(text, MOODS)
    return result["labels"][0]  # highest scoring label
