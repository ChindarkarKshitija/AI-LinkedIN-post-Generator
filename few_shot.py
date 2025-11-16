import json
import pandas as pd
import os

class FewShotPosts:
    def __init__(self, file_path="data/processed_posts.json"):
        self.df = None
        self.unique_tags = None
        self.file_path = file_path

    def load_posts(self, file_path=None):
        """Load and process posts from a JSON file."""
        if file_path is None:
            file_path = self.file_path

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Posts file not found at: {file_path}")

        with open(file_path, encoding="utf-8") as f:
            posts = json.load(f)
            self.df = pd.json_normalize(posts)

            # Categorize length
            self.df["length"] = self.df["line_count"].apply(self.categorize_length)

            # Collect all unique tags
            all_tags = []
            for tags in self.df['tags']:
                if isinstance(tags, list):
                    all_tags.extend(tags)
                else:
                    all_tags.append(tags)
            self.unique_tags = set(all_tags)

    def categorize_length(self, line_count):
        """Categorize a post based on-line count."""
        if line_count < 5:
            return "Short"
        elif 5 <= line_count <= 10:
            return "Medium"
        else:
            return "Long"

    def get_tags(self):
        """Return a set of all available tags."""
        if self.unique_tags is None:
            # ensure posts are loaded
            self.load_posts()
        return self.unique_tags

    def get_filtered_posts(self, length, language, tag):
        """
        Filter posts by length, language, and tag.
        Returns a list of dicts with post-data.
        """
        if self.df is None:
            # ensure posts are loaded
            self.load_posts()

        # Apply filters
        df_filtered = self.df[
            (self.df['language'] == language) &
            (self.df['length'] == length) &
            (self.df['tags'].apply(lambda tags: tag in tags))
        ]

        return df_filtered.to_dict(orient="records")


# For testing this file directly
if __name__ == "__main__":
    fs = FewShotPosts()
    fs.load_posts("data/processed_posts.json")  # ensure your JSON path is correct
    posts = fs.get_filtered_posts("Short", "English", "Job Search")
    print("Filtered posts:")
    for post in posts:
        print(post)
