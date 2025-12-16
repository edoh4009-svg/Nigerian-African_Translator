# Swahili Dictionary
# Team Member: [Your Name]
# Assigned Language: Swahili
# Word Count: 20 exactly

swahili_dict = {
    # ========== GREETINGS & BASICS (6 words) ==========
    "hello": "hujambo",
    "goodbye": "kwaheri",
    "thank you": "asante",
    "please": "tafadhali",
    "yes": "ndiyo",
    "no": "hapana",

    # ========== FAMILY (4 words) ==========
    "mother": "mama",
    "father": "baba",
    "child": "mtoto",
    "friend": "rafiki",

    # ========== COMMON OBJECTS (4 words) ==========
    "water": "maji",
    "food": "chakula",
    "house": "nyumba",
    "book": "kitabu",

    # ========== NATURE (4 words) ==========
    "sun": "jua",
    "moon": "mwezi",
    "tree": "mti",
    "river": "mto",

    # ========== TIME (2 words) ==========
    "day": "siku",
    "night": "usiku"
}

# Verification - This ensures exactly 20 words
if __name__ == "__main__":
    print(f"Swahili dictionary created!")
    print(f"Total words: {len(swahili_dict)}")
    if len(swahili_dict) == 20:
        print("✅ Perfect! Exactly 20 words.")
    else:
        print(f"❌ ERROR: Expected 20 words, got {len(swahili_dict)}")
