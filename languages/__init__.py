"""
AFRICAN LANGUAGE DICTIONARIES
Team Project - African Language Translator
Team Lead: [Edoh Godwin]
"""

# ========== IMPORT ALL DICTIONARIES ==========
from .swahili import swahili_dict    # Member 1 _ Momodu Daniel
from .yoruba import yoruba_dict      # Member 2 - John Bright
from .hausa import hausa_dict        # Member 3 - Simpa Ibrahim
from .zulu import zulu_dict          # Team Lead - Edoh Godwin ZULU ADDED HERE
from .igbo import igbo_dict          # Member 4 - Kamsi

# ========== MAIN LANGUAGE DICTIONARY ==========
LANGUAGES = {
    "Swahili": swahili_dict,
    "Yoruba": yoruba_dict,
    "Hausa": hausa_dict,
    "Zulu": zulu_dict,               # ZULU ADDED HERE
    "Igbo": igbo_dict,
}

# ========== STATISTICS ==========
AVAILABLE_LANGUAGES = sorted(LANGUAGES.keys())
TOTAL_LANGUAGES = len(LANGUAGES)
TOTAL_WORDS = sum(len(dict_obj) for dict_obj in LANGUAGES.values())

# ========== HELPER FUNCTIONS ==========
def get_project_stats():
    """Get project statistics"""
    return {
        "total_languages": TOTAL_LANGUAGES,
        "total_words": TOTAL_WORDS,
        "languages": AVAILABLE_LANGUAGES,
        "words_per_language": {lang: len(LANGUAGES[lang]) for lang in LANGUAGES}
    }

def translate(english_word, target_language):
    """Translate English word to target language"""
    english_word = english_word.lower().strip()
    target_language = target_language.title()
    
    if target_language in LANGUAGES and english_word in LANGUAGES[target_language]:
        return LANGUAGES[target_language][english_word]
    return f"Word '{english_word}' not found in {target_language}"

# ========== STARTUP MESSAGE ==========
print("\n" + "="*50)
print("🌍 AFRICAN LANGUAGE TRANSLATOR PACKAGE")
print("="*50)
print(f"📚 Languages: {', '.join(AVAILABLE_LANGUAGES)}")
print(f"📊 Total words: {TOTAL_WORDS}")
print("="*50)

# Export these
__all__ = [
    'LANGUAGES',
    'AVAILABLE_LANGUAGES',
    'TOTAL_LANGUAGES',
    'TOTAL_WORDS',
    'get_project_stats',
    'translate'
]
    'TOTAL_WORDS',
    'get_language_info',
    'translate_word',
    'list_words_in_language'
]
