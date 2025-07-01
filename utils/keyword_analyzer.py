# utils/keyword_analyzer.py
from collections import Counter
import re

DOG_KEYWORDS = [
    "dog", "dog-friendly", "doggie", "doggy", "puppy", "pup", "fur baby", "pooch", "canine", "pet", "pet-friendly",
    "water bowl", "dog treat", "poop bags", "leash",
    "patio", "outdoor", "outside", "terrace", "garden", "open space", "seating area",
    "welcoming", "friendly", "accommodating", "allowed", "relaxed", "great environment", "team", "great customer sevice"
]

def count_keyword_frequency(reviews, keywords=DOG_KEYWORDS):
    keyword_counts = Counter()
    lowercase_keywords = set(keyword.lower() for keyword in keywords)

    for review in reviews:
        review_text = review.get("text", "").lower()
        for keyword in lowercase_keywords:
            if re.search(r"\b" + re.escape(keyword) + r"\b", review_text):  
                keyword_counts[keyword] += 1

    return dict(keyword_counts)

def extract_reviews_with_keywords(reviews, keywords=DOG_KEYWORDS):
    matching_reviews = []
    lowercase_keywords = set(keyword.lower() for keyword in keywords)

    for review in reviews:
        review_text = review.get("text", "").lower()
        for keyword in lowercase_keywords:
            if re.search(r"\b" + re.escape(keyword) + r"\b", review_text): 
                matching_reviews.append(review)
                break  # Stop after finding the first match


    return matching_reviews
