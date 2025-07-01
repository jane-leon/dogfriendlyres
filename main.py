import os
from dotenv import load_dotenv
from barkometer_scraper import scrape_reviews_from_url
from utils.save_to_csv import save_reviews_to_csv
from analyze_with_openai import (
    rate_dog_friendliness_with_openai,
    find_matching_reviews,
    format_matched_reviews,
    DIRECT_DOG_KEYWORDS,
    INDIRECT_KEYWORDS
)
from utils.visualizer import plot_keyword_frequency_bar, plot_review_keyword_coverage_pie

def run_barkometer():
    load_dotenv()

    print("🐾 Barkometer: AI-Powered Dog-Friendliness Analyzer")
    maps_url = input("📍 Paste a Google Maps URL: ").strip()

    if not maps_url.startswith("https://www.google.com/maps"):
        print("❌ Invalid URL. Please make sure it's a Google Maps link.")
        return

    print("\n🔍 Scraping Google Maps reviews...")
    reviews = scrape_reviews_from_url(maps_url, max_reviews=150)
    if not reviews:
        print("❌ No reviews found.")
        return

    print(f"✅ Retrieved {len(reviews)} reviews with text.")

    # Save to CSV
    save_reviews_to_csv(reviews)

    # Visualize keyword frequency and coverage
    plot_keyword_frequency_bar(reviews)
    plot_review_keyword_coverage_pie(reviews)

    # Analyze with OpenAI
    print("\n🤖 Analyzing dog-friendliness with OpenAI...")
    result = rate_dog_friendliness_with_openai(reviews)

    print("\n===== 🐶 Barkometer Rating =====")
    print(result)

    print("\n🔍 Matched Reviews (Direct Keywords):")
    print(format_matched_reviews(find_matching_reviews(reviews, DIRECT_DOG_KEYWORDS)))

    print("\n🔍 Matched Reviews (Indirect Keywords):")
    print(format_matched_reviews(find_matching_reviews(reviews, INDIRECT_KEYWORDS)))


if __name__ == "__main__":
    run_barkometer()




