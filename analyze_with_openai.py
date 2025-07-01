import os
from openai import OpenAI
import re
from datetime import datetime

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Keyword definitions
DIRECT_DOG_KEYWORDS = [
    "dog", "dog-friendly", "doggie", "doggy", "puppy", "pup", "fur baby", "pooch", "canine",
    "pet", "pet-friendly", "leash", "dog treat", "water bowl", "dog menu", "poop bags"
]

INDIRECT_KEYWORDS = [
    "patio", "outdoor", "outside", "terrace", "garden", "open space", "seating area",
    "friendly", "welcoming", "accommodating", "relaxed", "allowed", "great with pets", "great environment", "team", "great customer service"
]

def find_matching_reviews(reviews, keywords):
    keyword_set = set(keywords)
    matches = []

    for review in reviews:
        text = review.get("text", "").lower()
        found = [kw for kw in keyword_set if re.search(r"\b" + re.escape(kw) + r"\b", text)]
        if found:
            matches.append((review, found))

    return matches

def format_date(date_str):
        try:
            return datetime.fromisoformat(date_str.replace("Z", "")).strftime("%B %d, %Y")
        except:
            return date_str or "No date"

def format_matched_reviews(matches):
    formatted = []
    for review, keywords in matches:
        author = review.get("author", "Anonymous")
        rating = review.get("rating", "No rating")
        date = format_date(review.get("date"))
        text = review.get("text", "(No text)")
        formatted.append(f"• {author} ({rating}⭐) on {date}:\n  {text}")
    return "\n\n".join(formatted) or "None"

def generate_dog_friendliness_prompt(reviews):
    direct_matches = find_matching_reviews(reviews, DIRECT_DOG_KEYWORDS)
    indirect_matches = find_matching_reviews(reviews, INDIRECT_KEYWORDS)

    # all_reviews_text = ""
    # for review in reviews:
    #     author = review.get("author", "Unknown")
    #     rating = review.get("rating", "No rating")
    #     date = format_date(review.get("date"))
    #     text = review.get("text", "")

    #     all_reviews_text += f"{author} ({rating}⭐) on {date}:\n{text}\n\n"
    
    direct_summary = format_matched_reviews(direct_matches)
    indirect_summary = format_matched_reviews(indirect_matches)




    prompt = f"""
You're an expert at evaluating how dog-friendly a location is based on Google Maps reviews.

Your task is to:
- Give a **dog-friendliness score** (0 to 10)
- Write a one to two paragraphs justifying your score
- List a few specific reviews that influenced your decision

Use this scoring guidance:
- Reviews that directly mention dogs, dog amenities (like water bowls or leashes), or being "pet-friendly" suggest strong dog-friendliness.
- Indirect clues like patios, outdoor seating, welcoming/friendly staff, or relaxed vibes can *indicate* dog-friendliness — especially if mentioned often.
- If **no direct dog keywords** are found, the score should **not exceed 5**.
- However, if **many indirect signs** exist, you may still assign a score like 4–5, showing some openness to dogs.
- Be thoughtful — some places may feel welcoming to pets even if dogs aren’t explicitly mentioned.

Examples:
- ✅ "There was a water bowl outside for dogs" → strong sign → higher score
- ✅ "Friendly outdoor patio " → good indirect signal


Now assign your score and explanation below.


🔽 Reviews with direct dog-related keywords:
{direct_summary}

🔽 Reviews with indirect or contextual keywords:
{indirect_summary}
"""

    return [{"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}]

def rate_dog_friendliness_with_openai(reviews):
    messages = generate_dog_friendliness_prompt(reviews)

    # DEBUG_MODE = False

    # if DEBUG_MODE:
    #     print("\n===== 📤 Full Prompt to OpenAI =====")
    #     print(messages[1]['content'])
    # 🔽 All Reviews:
# {all_reviews_text}

    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        temperature=0.4
    )

    return response.choices[0].message.content

