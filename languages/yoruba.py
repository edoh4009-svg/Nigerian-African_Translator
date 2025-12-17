# Yoruba Dictionary
# Team Member: [Your Name]
# Assigned Language: Yoruba
# Word Count: 20 exactly

yoruba_dict = {
    # ========== GREETINGS & BASICS (6 words) ==========
    "hello": "bawo",
    "goodbye": "o dabọ",
    "thank you": "o ṣeun",
    "please": "jọwọ",
    "yes": "bẹẹni",
    "no": "bẹẹkọ",

    # ========== FAMILY (4 words) ==========
    "mother": "iya",
    "father": "baba",
    "child": "ọmọ",
    "friend": "ọrẹ",

    # ========== COMMON OBJECTS (4 words) ==========
    "water": "omi",
    "food": "ounjẹ",
    "house": "ile",
    "book": "iwe",

    # ========== NATURE (4 words) ==========
    "sun": "oorun",
    "moon": "osupa",
    "tree": "igi",
    "river": "odò",

    # ========== TIME (2 words) ==========
    "day": "ọjọ",
    "night": "alẹ"
}

# Verification - ensures exactly 20 words
if __name__ == "__main__":
    print(f"✅ Yoruba dictionary created!")
    print(f"📊 Total words: {len(yoruba_dict)}")

    if len(yoruba_dict) == 20:
        print("✅ Perfect! Exactly 20 words.")
        print("\n🔤 Sample translations:")
        samples = list(yoruba_dict.items())[:5]
        for eng, yoruba in samples:
            print(f"  {eng:10} → {yoruba}")
    else:
        print(f"❌ ERROR: Expected 20 words, got {len(yoruba_dict)}")
        print("   Please check your word count.")
