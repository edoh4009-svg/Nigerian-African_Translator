# Igbo Dictionary
# Team Member: [Kamsioyochukwuechezona]
# Assigned Language: Igbo
# Word Count: 20 exactly

igbo_dict = {
    # ========== GREETINGS & BASICS (6 words) ==========
    "hello": "ndewo",
    "goodbye": "ka ọ dị",
    "thank you": "daalụ",
    "please": "biko",
    "yes": "ee",
    "no": "mba",

    # ========== FAMILY (4 words) ==========
    "mother": "nne",
    "father": "nna",
    "child": "nwa",
    "friend": "enyi",

    # ========== COMMON OBJECTS (4 words) ==========
    "water": "mmiri",
    "food": "nri",
    "house": "ụlọ",
    "book": "akwụkwọ",

    # ========== NATURE (4 words) ==========
    "sun": "anyanwụ",
    "moon": "ọnwa",
    "tree": "osisi",
    "river": "osimiri",

    # ========== TIME (2 words) ==========
    "day": "ụbọchị",
    "night": "abali"
}

# Verification - ensures exactly 20 words
if __name__ == "__main__":
    print(f"✅ Igbo dictionary created!")
    print(f"📊 Total words: {len(igbo_dict)}")

    if len(igbo_dict) == 20:
        print("✅ Perfect! Exactly 20 words.")
        print("\n🔤 Sample translations:")
        samples = list(igbo_dict.items())[:5]
        for eng, igbo in samples:
            print(f"  {eng:10} → {igbo}")
    else:
        print(f"❌ ERROR: Expected 20 words, got {len(igbo_dict)}")
        print("   Please check your word count.")
