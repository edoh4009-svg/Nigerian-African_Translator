hausa_dict = {
    # ========== GREETINGS & BASICS (6 words) ==========
    "hello": "sannu",
    "goodbye": "sai anjima",
    "thank you": "na gode",
    "please": "don Allah",
    "yes": "i",
    "no": "a'a",

    # ========== FAMILY (4 words) ==========
    "mother": "uwa",
    "father": "uba",
    "child": "yaro",
    "friend": "aboki",

    # ========== COMMON OBJECTS (4 words) ==========
    "water": "ruwa",
    "food": "abinci",
    "house": "gida",
    "book": "littafi",

    # ========== NATURE (4 words) ==========
    "sun": "rana",
    "moon": "wata",
    "tree": "itace",
    "river": "kogi",

    # ========== TIME (2 words) ==========
    "day": "rana",
    "night": "dare"
}

# Verification - This ensures exactly 20 words
if __name__ == "__main__":
    print(f"Hausa dictionary created!")
    print(f"Total words: {len(hausa_dict)}")
    if len(hausa_dict) == 20:
        print("✅ Perfect! Exactly 20 words.")
    else:
        print(f"❌ ERROR: Expected 20 words, got {len(hausa_dict)}")
