"""
stopwords.py  (no external libraries)

A tiny "stop word remover" module you can import into your main program,
but you can ALSO run this file directly to test it.

How to use in another file:
    from stopwords import remove_stopwords

    cleaned_tokens = remove_stopwords(tokens)
    # or: cleaned_text = remove_stopwords(text, return_type="text")

Design:
- No libraries needed (only basic Python)
- Works on either:
    (A) a list of tokens: ["this","is","a","test"]
    (B) a string: "this is a test"
- You can control:
    - keep_negations=True  (keeps "not", "no", "never" etc. for sentiment!)
    - keep_pronouns=True   (optional, sometimes useful)
"""

# ------------------------------------------------------------
# A simple, editable stopword list.
# You can add/remove words depending on your project.
# ------------------------------------------------------------
DEFAULT_STOPWORDS = set([
    # articles
    "a", "an", "the",

    # basic helpers / common function words
    "and", "or", "but", "so", "because", "as", "if", "than", "then", "that", "this", "these", "those",

    # prepositions
    "in", "on", "at", "to", "from", "of", "for", "with", "about", "into", "over", "under", "between",
    "after", "before", "during", "through", "against", "without", "within",

    # common verbs (often not useful for sentiment by themselves)
    "is", "am", "are", "was", "were", "be", "been", "being",
    "do", "does", "did",
    "have", "has", "had",

    # modal verbs
    "can", "could", "may", "might", "must", "shall", "should", "will", "would",

    # adverbs that are usually low-value alone
    "very", "really", "just", "also", "too", "quite", "rather",

    # misc
    "it", "its", "it's", "im", "i'm", "youre", "you're", "theyre", "they're",
])


# ------------------------------------------------------------
# Words we often want to KEEP for sentiment / meaning.
# Negations are super important for sentiment!
# ------------------------------------------------------------
NEGATIONS = set([
    "no", "not", "never", "none", "nothing", "nowhere",
    "can't", "cannot", "dont", "don't", "doesn't", "didn't",
    "won't", "wouldn't", "shouldn't", "isn't", "aren't", "wasn't", "weren't",
])


# Optional: sometimes you might want to keep pronouns
PRONOUNS = set([
    "i", "me", "my", "mine",
    "we", "us", "our", "ours",
    "you", "your", "yours",
    "he", "him", "his",
    "she", "her", "hers",
    "they", "them", "their", "theirs"
])


# ------------------------------------------------------------
# Tiny helper: normalize a token (simple beginner style)
# ------------------------------------------------------------
def _normalize_token(token: str) -> str:
    """
    Lowercase and strip punctuation at the ends.
    This is intentionally simple.
    """
    token = token.lower()

    punct = ".,!?;:\"'()[]{}<>"
    while len(token) > 0 and token[0] in punct:
        token = token[1:]
    while len(token) > 0 and token[-1] in punct:
        token = token[:-1]

    return token


# ------------------------------------------------------------
# Main function: remove_stopwords
# ------------------------------------------------------------
def remove_stopwords(
    text_or_tokens,
    stopwords: set | None = None,
    keep_negations: bool = True,
    keep_pronouns: bool = False,
    return_type: str = "tokens",
):
    """
    Remove stopwords from a string or a list of tokens.

    Parameters
    ----------
    text_or_tokens:
        - string: "This is a test"
        - OR list of tokens: ["This","is","a","test"]

    stopwords:
        - set of stopwords to use
        - if None, uses DEFAULT_STOPWORDS

    keep_negations:
        - if True, words like "not", "never", "don't" will NOT be removed

    keep_pronouns:
        - if True, pronouns like "i", "you", "they" will NOT be removed

    return_type:
        - "tokens" -> returns list[str]
        - "text"   -> returns a string joined by spaces

    Returns
    -------
    list[str] OR str
    """

    # Use default stopwords if none given
    if stopwords is None:
        stopwords = DEFAULT_STOPWORDS

    # If input is a string, split by spaces (simple tokenization)
    if isinstance(text_or_tokens, str):
        raw_tokens = text_or_tokens.split()
    else:
        # Assume it's already a list of tokens
        raw_tokens = text_or_tokens

    cleaned = []

    for tok in raw_tokens:
        norm = _normalize_token(tok)

        # skip empty tokens after normalization
        if norm == "":
            continue

        # Decide what words we want to keep even if they're in stopwords
        if keep_negations and norm in NEGATIONS:
            cleaned.append(norm)
            continue

        if keep_pronouns and norm in PRONOUNS:
            cleaned.append(norm)
            continue

        # If it's in stopwords, we remove it
        if norm in stopwords:
            continue

        # Otherwise keep it
        cleaned.append(norm)

    if return_type == "text":
        return " ".join(cleaned)

    # default: return tokens
    return cleaned


# ------------------------------------------------------------
# Quick test runner (so you can run stopwords.py directly)
# ------------------------------------------------------------
if __name__ == "__main__":
    test_text = "I am not happy with the battery life, but it is not terrible."

    print("Original text:")
    print(test_text)

    print("\nTokens after stopword removal (keep_negations=True):")
    print(remove_stopwords(test_text, keep_negations=True, return_type="tokens"))

    print("\nText after stopword removal (keep_negations=True):")
    print(remove_stopwords(test_text, keep_negations=True, return_type="text"))

    print("\nTokens after stopword removal (keep_negations=False):")
    print(remove_stopwords(test_text, keep_negations=False, return_type="tokens"))