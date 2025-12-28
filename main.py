import requests
from collections import Counter, defaultdict
import matplotlib.pyplot as plt

BASE_URL = "https://codeforces.com/api/problemset.problems"

# Rating buckets: (label, lower_bound_inclusive, upper_bound_exclusive)
RATING_BUCKETS = [
    ("0-1000", 0, 1000),
    ("1000-1300", 1000, 1300),
    ("1300-1600", 1300, 1600),
    ("1600-1900", 1600, 1900),
    ("1900-2100", 1900, 2101),  # 2100 inclusive
]


def get_bucket_label(rating: int):
    """
    Return the label of the rating bucket that the given rating belongs to.
    Returns None if the rating is missing or outside defined buckets.
    """
    if rating is None:
        return None

    for label, lower, upper in RATING_BUCKETS:
        if lower <= rating < upper:
            return label

    return None


def fetch_problems_0_2100():
    """
    Fetch all problems from the Codeforces problemset API.
    Only problems with ratings up to 2100 are later considered via bucketing.
    """
    response = requests.get(BASE_URL)
    response.raise_for_status()

    data = response.json()
    if data.get("status") != "OK":
        raise RuntimeError(f"Codeforces API error: {data}")

    return data["result"]["problems"]


def build_tag_frequencies_by_bucket(problems):
    """
    Build tag frequency counters for each rating bucket.

    Returns:
        dict[str, Counter]: bucket_label -> Counter(tag -> frequency)
    """
    bucket_to_tag_counter = defaultdict(Counter)

    for problem in problems:
        rating = problem.get("rating")
        tags = problem.get("tags", [])

        bucket_label = get_bucket_label(rating)
        if bucket_label is None:
            continue

        for tag in tags:
            bucket_to_tag_counter[bucket_label][tag] += 1

    return bucket_to_tag_counter


def plot_tag_barcharts(bucket_to_tag_counter, top_n=15):
    """
    Plot bar charts showing the top N most frequent tags
    for each rating bucket.
    """
    for bucket_label, counter in bucket_to_tag_counter.items():
        if not counter:
            print(f"No data for bucket {bucket_label}, skipping plot.")
            continue

        most_common = counter.most_common(top_n)
        tags = [tag for tag, _ in most_common]
        freqs = [freq for _, freq in most_common]

        plt.figure(figsize=(10, 6))
        plt.bar(tags, freqs)
        plt.xticks(rotation=45, ha="right")
        plt.xlabel("Tag")
        plt.ylabel("Frequency")
        plt.title(f"Top {top_n} Tags for Rating Bucket {bucket_label}")
        plt.tight_layout()
        plt.show()


def main():
    print("Fetching problems from Codeforces API...")
    problems = fetch_problems_0_2100()
    print(f"Fetched {len(problems)} problems")

    print("Building tag frequencies by rating bucket...")
    bucket_to_tag_counter = build_tag_frequencies_by_bucket(problems)

    for label, _, _ in RATING_BUCKETS:
        counter = bucket_to_tag_counter.get(label, Counter())
        print(
            f"\nBucket {label}: "
            f"{sum(counter.values())} tag occurrences "
            f"across {len(counter)} unique tags"
        )
        for tag, freq in counter.most_common(10):
            print(f"  {tag:<25} {freq}")

    print("\nGenerating bar charts...")
    plot_tag_barcharts(bucket_to_tag_counter, top_n=15)


if __name__ == "__main__":
    main()
