import string

review = "The food was GREAT! But the service was horrible, I felt it was bad."

print("Original Review:")
print(review)

# Remove punctuation
clean_review = ""
for ch in review:
    if ch not in string.punctuation:
        clean_review += ch

# Convert to lowercase
clean_review = clean_review.lower()

# Split into words
words = clean_review.split()

print("\nCleaned Review:")
print(clean_review)

# Define sentiment words
positive_words = ["good", "great"]
negative_words = ["bad", "horrible"]

# Count frequency
positive_count = 0
negative_count = 0

for word in words:
    if word in positive_words:
        positive_count += 1
    elif word in negative_words:
        negative_count += 1

# Decide sentiment
if positive_count > negative_count:
    print("\nReview Type: Positive Review")
elif negative_count > positive_count:
    print("\nReview Type: Negative Review")
else:
    print("\nReview Type: Neutral Review")
