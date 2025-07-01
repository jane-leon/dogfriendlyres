# utils/save_to_csv.py

import pandas as pd
import os

def save_reviews_to_csv(reviews, fallback_name="place", directory="data"):
    """
    Save reviews to a CSV file named after the place (e.g., 'soul_bowls_reviews.csv').
    Creates a 'data' folder if it doesn't exist.
    """
    os.makedirs(directory, exist_ok=True)

    # Try to get the place title from the first review
    place_name = reviews[0].get("title", fallback_name).lower().replace(" ", "_")
    filename = f"{directory}/{place_name}_reviews.csv"

    df = pd.DataFrame(reviews)
    df.to_csv(filename, index=False)
    print(f"✅ Saved {len(reviews)} reviews to {filename}")
