"""
AFRICAN LANGUAGE TRANSLATOR - DICTIONARIES PACKAGE
Team Project: African Language Translator

This package contains translation dictionaries for 5 African languages:
1. Swahili  - Spoken in East Africa
2. Yoruba   - Spoken in Nigeria and Benin
3. Hausa    - Spoken in West Africa
4. Zulu     - Spoken in South Africa
5. Igbo     - Spoken in Nigeria

Team Members:
- [Name 1] - Swahili
- [Name 2] - Yoruba
- [Name 3] - Hausa
- [Name 4] - Zulu
- [Name 5] - Igbo
"""

# ========== IMPORT ALL 5 LANGUAGE DICTIONARIES ==========

# Swahili Dictionary - East Africa
from .swahili import swahili_dict

# Yoruba Dictionary - Nigeria/Benin
from .yoruba import yoruba_dict

# Hausa Dictionary - West Africa
from .hausa import hausa_dict

# Zulu Dictionary - South Africa
from .zulu import zulu_dict

# Igbo Dictionary - Nigeria
from .igbo import igbo_dict

# ========== MAIN LANGUAGE DICTIONARY ==========
# Maps language names to their dictionaries
LANGUAGES = {
    "Swahili": swahili_dict,
    "Yoruba": yoruba_dict,
    "Hausa": hausa_dict,
    "Zulu": zulu_dict,
    "Igbo": igbo_dict,
}

# ========== HELPER VARIABLES ==========
AVAILABLE_LANGUAGES = list(LANGUAGES.keys())
TOTAL_LANGUAGES = len(LANGUAGES)

# Count total words across all dictionaries
TOTAL_WORDS = 0
for lang_name, dictionary in LANGUAGES.items():
    if dictionary and len(dictionary) > 0:
        TOTAL_WORDS += len(dictionary)


# ========== HELPER FUNCTIONS ==========
def get_language_info():
    """Return information about all loaded languages"""
    info = []
    for lang_name, dictionary in LANGUAGES.items():
        word_count = len(dictionary) if dictionary else 0
        status = "✅ Loaded" if word_count >= 20 else "⚠️ Incomplete" if word_count > 0 else "❌ Missing"
        info.append({
            'language': lang_name,
            'word_count': word_count,
            'status': status
        })
    return info


def translate_word(english_word, target_language):
    """Translate an English word to target language"""
    english_word = english_word.lower().strip()
    target_language = target_language.title()  # Capitalize first letter

    if target_language in LANGUAGES:
        dictionary = LANGUAGES[target_language]
        if dictionary and english_word in dictionary:
            return dictionary[english_word]

    return None


def list_words_in_language(language_name):
    """List all words available in a specific language"""
    language_name = language_name.title()
    if language_name in LANGUAGES:
        dictionary = LANGUAGES[language_name]
        if dictionary:
            return sorted(dictionary.keys())
    return []


def get_language_statistics():
    """Get statistics about all languages"""
    stats = {
        'total_languages': TOTAL_LANGUAGES,
        'total_words': TOTAL_WORDS,
        'languages': AVAILABLE_LANGUAGES,
        'words_per_language': {},
        'completion_status': {}
    }

    for lang_name, dictionary in LANGUAGES.items():
        word_count = len(dictionary) if dictionary else 0
        stats['words_per_language'][lang_name] = word_count

        if word_count >= 20:
            stats['completion_status'][lang_name] = "✅ Complete"
        elif word_count > 0:
            stats['completion_status'][lang_name] = f"⚠️ {word_count}/20 words"
        else:
            stats['completion_status'][lang_name] = "❌ Not started"

    return stats


# ========== STARTUP MESSAGE ==========
print("\n" + "=" * 50)
print("🌍 AFRICAN LANGUAGE TRANSLATOR PACKAGE")
print("=" * 50)
print(f"📚 Total languages: {TOTAL_LANGUAGES}")
print(f"📝 Total words loaded: {TOTAL_WORDS}")

# Show status of each language
print("\n📊 LANGUAGE STATUS:")
for lang in AVAILABLE_LANGUAGES:
    word_count = len(LANGUAGES[lang]) if LANGUAGES[lang] else 0
    if word_count >= 20:
        status = "✅"
    elif word_count > 0:
        status = "⚠️"
    else:
        status = "❌"
    print(f"{status} {lang:10} - {word_count:3} words")

print("=" * 50)

# ========== EXPORT THESE VARIABLES/FUNCTIONS ==========
# What gets imported when someone does: from languages import *
__all__ = [
    'LANGUAGES',
    'AVAILABLE_LANGUAGES',
    'TOTAL_LANGUAGES',
    'TOTAL_WORDS',
    'get_language_info',
    'translate_word',
    'list_words_in_language',
    'get_language_statistics'
]

# ========== TEST WHEN RUN DIRECTLY ==========
if __name__ == "__main__":
    print("\n🧪 RUNNING PACKAGE SELF-TEST...")

    # Test 1: Check all imports worked
    print("1. Checking imports...")
    for lang in AVAILABLE_LANGUAGES:
        if lang in LANGUAGES and LANGUAGES[lang]:
            print(f"   ✅ {lang}: {len(LANGUAGES[lang])} words loaded")
        else:
            print(f"   ❌ {lang}: Import failed or empty")

    # Test 2: Test translation function
    print("\n2. Testing translations...")
    test_cases = [
        ("hello", "Swahili"),
        ("thank you", "Yoruba"),
        ("water", "Hausa"),
        ("mother", "Zulu"),
        ("sun", "Igbo")
    ]

    for english, language in test_cases:
        translation = translate_word(english, language)
        if translation:
            print(f"   ✅ {english:10} → {translation:15} ({language})")
        else:
            print(f"   ❌ {english:10} not found in {language}")

    print("\n" + "=" * 50)
    print("✅ Package loaded successfully!")
    print("=" * 50)
