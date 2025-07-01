# utils/visualizer.py

import matplotlib.pyplot as plt
from collections import Counter
from utils.keyword_analyzer import count_keyword_frequency, extract_reviews_with_keywords
import re

# Keywords to scan for
DOG_KEYWORDS = [
    "dog", "dog-friendly", "doggie", "doggy", "puppy", "pup", "fur baby", "pooch", "canine", "pet", "pet-friendly",
    "water bowl", "dog treat", "poop bags", "leash",
    "patio", "outdoor", "outside", "terrace", "garden", "open space", "seating area",
    "welcoming", "friendly", "accommodating", "allowed", "relaxed", "great environment","team", "great customer service"
]


def plot_keyword_frequency_bar(reviews, top_n=15):
    freq_dict = count_keyword_frequency(reviews)
    if not freq_dict:
        print("❌ No keywords found to plot.")
        return

    sorted_keywords = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)[:top_n]
    keywords, counts = zip(*sorted_keywords)

    plt.figure(figsize=(10, 5))
    bars = plt.bar(keywords, counts, color="#c6a5e6")

     # headroom above the tallest bar
    max_count = max(counts)
    plt.ylim(0, max_count + max_count * 0.2)


    # Titles & labels
    plt.title("Top Dog-Related Keyword Frequency in Reviews", fontsize=16, fontweight='bold')
    plt.xlabel("Keywords", fontsize=12, fontweight='bold')
    plt.ylabel("Frequency", fontsize=12, fontweight='bold')
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.yticks(fontsize=10)


    # Add value labels (tickers) on top of each bar
    for bar in bars:
        height = bar.get_height()
        plt.annotate(f'{height}',
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 3),  # 3 points vertical offset
                     textcoords="offset points",
                     ha='center', va='bottom',
                     fontsize=9, fontweight='bold')

    plt.tight_layout(pad=2.0)
    plt.show()


def plot_review_keyword_coverage_pie(reviews):
    total = len(reviews)
    with_keywords = len(extract_reviews_with_keywords(reviews))
    without_keywords = total - with_keywords

    if total == 0:
        print("❌ No reviews to visualize.")
        return

    labels = ["With Dog Keywords", "Without Dog Keywords"]
    sizes = [with_keywords, without_keywords]
    colors = ["#b3d68d", "#ebd89d"]

    fig, ax = plt.subplots(figsize=(8, 6)) 
    wedges, _, autotexts = plt.pie(
        sizes,
        autopct='%1.1f%%',
        colors=colors,
        startangle=140,
        textprops={'fontsize': 11, 'fontweight': 'bold'}
    )

    # Add legend
    plt.legend(
        wedges,
        labels,
        title="Review Type",
        loc="center left",
        bbox_to_anchor=(1, 0, 0.5, 1),
        fontsize=11,
        title_fontsize=12
    )

    fig.suptitle("Review Coverage of Dog-Related Keywords", fontsize=16, fontweight='bold',y=0.88)
    plt.axis("equal")
    plt.tight_layout(pad=4.0)
    plt.show()

