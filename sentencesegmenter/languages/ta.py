from sentencesegmenter.base import Language

from .en import English

vowel_signs = {"ா", "ி", "ீ", "ு", "ூ", "ெ", "ே", "ை", "ொ", "ோ", "ௌ"}
vowels = {"அ", "ஆ", "இ", "ஈ", "உ", "ஊ", "எ", "ஏ", "ஐ", "ஒ", "ஓ", "ஔ"}
consonants = {
    "க",
    "ங",
    "ச",
    "ஞ",
    "ட",
    "ண",
    "த",
    "ந",
    "ப",
    "ம",
    "ய",
    "ர",
    "ல",
    "வ",
    "ழ",
    "ள",
    "ற",
    "ன",
}
consonant_vowels = set()

for consonant in consonants:
    for vowel_sign in vowel_signs:
        consonant_vowels.add(consonant + vowel_sign)


class Tamil(Language):
    language = "ta"

    # Writing English abbreviation like Dr as such inside Tamil is common
    abbreviations = (
        English.abbreviations.union(vowels)
        .union(consonants)
        .union(consonant_vowels)
        .union({"பி" "எச்", "ஐ", "வி" "ஐ", "எசு", "ஓ"})
    )
