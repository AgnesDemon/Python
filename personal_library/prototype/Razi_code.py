import pandas as pd
import matplotlib.pyplot as plt

# Add a category for each book: Canonical OT, Apocrypha, NT, Gnostic OT-like, Gnostic NT-like
categorized_books = []

# Helper sets for classification
old_testament_books = {
"Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy", "Joshua", "Judges",
"1 Samuel", "2 Samuel", "1 Kings", "2 Kings", "Isaiah", "Jeremiah", "Ezekiel",
"Hosea", "Joel", "Amos", "Obadiah", "Jonah", "Micah", "Nahum", "Habakkuk", "Zephaniah",
"Haggai", "Zechariah", "Malachi", "Psalms", "Proverbs", "Job", "Song of Songs",
"Ruth", "Lamentations", "Ecclesiastes", "Esther", "Daniel", "Ezra", "Nehemiah",
"1 Chronicles", "2 Chronicles"
}
apocrypha_books = {
"Tobit", "Judith", "Wisdom of Solomon", "Sirach (Ecclesiasticus)", "Baruch",
"1 Maccabees", "2 Maccabees", "Additions to Daniel", "Prayer of Manasseh",
"Additions to Esther", "Susanna", "Bel and the Dragon"
}
new_testament_books = {
"Matthew", "Mark", "Luke", "John", "Acts", "Romans", "1 Corinthians", "2 Corinthians",
"Galatians", "Ephesians", "Philippians", "Colossians", "1 Thessalonians", "2 Thessalonians",
"1 Timothy", "2 Timothy", "Titus", "Philemon", "Hebrews", "James", "1 Peter", "2 Peter",
"1 John", "2 John", "3 John", "Jude", "Revelation"
}
gnostic_ot_like = {
"1 Enoch", "2 Enoch (Slavonic)", "3 Enoch (Hebrew)", "Book of Jubilees", "Book of Giants"
}
gnostic_nt_like = {
"Gospel of Thomas", "Gospel of Mary", "Gospel of Judas", "Gospel of Philip",
"Apocalypse of Peter (Gnostic)", "Acts of Thomas", "Pistis Sophia"
}

# Classify each book
for book, date in categorized_books:
    if book in old_testament_books:
        category = "Canonical OT"
    elif book in apocrypha_books:
        category = "Apocrypha"
    elif book in new_testament_books:
        category = "Canonical NT"
    elif book in gnostic_ot_like:
        category = "Gnostic (OT-like)"
    elif book in gnostic_nt_like:
        category = "Gnostic (NT-like)"
    else:
        category = "Unclassified"
    categorized_books.append((book, date, category))

# Convert to DataFrame
df_categorized = pd.DataFrame(categorized_books, columns=["Book", "Date", "Category"])

# Sort by date
df_categorized = df_categorized.sort_values(by="Date")

# Assign colors for each category
color_map = {
"Canonical OT": "saddlebrown",
"Apocrypha": "goldenrod",
"Canonical NT": "darkred",
"Gnostic (OT-like)": "green",
"Gnostic (NT-like)": "purple",
"Unclassified": "gray"
}
df_categorized["Color"] = df_categorized["Category"].map(color_map)

# Plot
plt.figure(figsize=(16, 26))
plt.hlines(y=df_categorized["Book"], xmin=-1000, xmax=550, color="lightgray", linewidth=0.5)
plt.scatter(df_categorized["Date"], df_categorized["Book"], c=df_categorized["Color"])

plt.axvline(x=0, color="blue", linestyle="--", label="0 AD (Common Era)")
plt.title("Timeline of Biblical, Apocryphal, and Gnostic Books\nBy Date and Theological Placement", fontsize=16)
plt.xlabel("Date (BCE/CE)")
plt.ylabel("Books (Sorted by Date and Placement)")
plt.grid(True, axis='x', linestyle='--', alpha=0.7)

# Create custom legend
from matplotlib.patches import Patch
legend_elements = [
Patch(facecolor=color, label=label)
for label, color in color_map.items()
]
legend_elements.append(Patch(facecolor="blue", label="0 AD Marker"))
plt.legend(handles=legend_elements, loc='upper right')

plt.tight_layout()
plt.gca().invert_yaxis()
plt.show()
