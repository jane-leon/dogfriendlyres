from apify_client import ApifyClient
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()
APIFY_API_TOKEN = os.getenv("APIFY_API_TOKEN")

if not APIFY_API_TOKEN:
    raise ValueError("Missing APIFY_API_TOKEN in .env file!")

# Initialize Apify client
client = ApifyClient(APIFY_API_TOKEN)

def scrape_reviews_from_url(maps_url: str, max_reviews: int = 100):


    run_input={
    "startUrls": [{"url": maps_url}],
    "includeReviews": True,
    "maxReviews": 100,
    "reviewsSort": "mostRelevant",
    "language": "en",
    "reviewsOrigin": "all",
    "personalData": True
    }

    # Run the actor
    run = client.actor("Xb8osYTtOjlsgI6k9").call(run_input=run_input)
    items = client.dataset(run["defaultDatasetId"]).list_items().items

    reviews = []
    for item in items:
        text = item.get("text")
        name = item.get("name", "Anonymous")
        stars = item.get("stars", None)
        date = item.get("publishedAtDate", "Unknown")

        if text:  # Only keep reviews with non-empty text
            reviews.append({
                "author": name,
                "rating": stars,
                "text": text,
                "date": date
            })

    return reviews



