# PTpy! 1.0 (Pee-Tee-Py) - Perisan Tokenizer for Python - Developed in Python 3.11 as exercise 2.5 for Information retrieval
# Copyright 2023, Pouya Abbasi, All rights reserved.

import re
import time  # Just for the "sleep" function, nothing to do with the tokenizing procces.

# The full stop words are saved as a seperate list as fullStopList,
# change the #15 function if you want the +550 stop list to be applied.
from stopWordList import fullStopList


# The whole "Tokenization" function, that passes your text through 15 phases!!!
def tokenize_text(input_file_path):
    # Phase One, get the text from the file provided by the user.
    input_text = get_text_from_file(input_file_path)

    # Phase Two, remove the punctuation characters.
    puncList = [
        "!",
        ".",
        "؟",
        "،",
        "؛",
        ")",
        ",",
        "!",
        "?",
        "(",
        "'",
        '"',
        "{",
        "}",
        "[",
        "]",
        "-",
    ]

    input_text = remove_punctuation(input_text, puncList)

    # Phase Three, remove the redundant spaces.
    input_text = remove_extra_spaces(input_text)

    # Phase Four, replace "ک" and "ی" to "که" and "یه", respectively and so on.
    input_text = replace_chars(input_text)

    # Phase Five, removes the "Hamzeh" character.
    input_text = remove_hamzeh(input_text)

    # Phase Six, removes the "Hamzeh" character from the end of a word
    input_text = remove_hamzeh_end(input_text)

    # Phase Seven, converts "آ" to "ا".
    input_text = replace_a(input_text)

    # Phase Eight, removes "Tashdid".
    input_text = remove_tashdid(input_text)

    # Phase Nine, replaces English numbers with persian ones.
    input_text = replace_numbers(input_text)

    # Phase Ten, fixes the "&nbps", a.k.a non-breaking space, a.k.a "nim-faseleh" issue.
    # EDIT: I THINK THE 13TH PHASE DOES THE JOB BETTER, DIDN'T REMOVE IT SO THE PHASE NUMBERING WOULD STAY THE SAME.
    #    input_text = fix_nbsp(input_text)

    # Phase Eleven, replaces Arabic characters to their respective Persian variants.
    input_text = fix_arabic(input_text)

    # Phase Twelve, removes duplicate spaces. (Kind of phase 3, rewrote it in another way.)
    input_text = remove_duplicate_spaces(input_text)

    # Phase Thirteen, fixes the separate suffix issue. It is customizable, see the related function definition.
    input_text = attach_suffixes(input_text)

    # Phase Fourteen, fixes the separate prefix issue. It is customizable, see the "prefixes" list in the related function definition.
    input_text = fix_prefix_spacing(input_text)

    # Phase Fifteen, removes the stop words.
    stopList = [
        "انگار",
        "حتما",
        "زود",
        "حتی",
        "هست",
        "که",
        "خصوصا",
        "با",
        "بله",
        "حالا",
        "باشد",
        "از",
        "حدودا",
        "بدون",
        "اینقدر",
        "باید",
        "کرد",
        "اما",
        "بعدا",
        "اینطور",
        "بلاخره",
        "چون",
        "شد",
        "البته",
        "اگر",
        "اینک",
        "برای",
        "اکنون",
        "است",
        "زیرا",
        " یک",
        " یه ",
        "به",
        "بر",
        "را",
        "در",
        "هر",
        "و",
        "تا",
        "یا",
        "با",
        "هم",
    ]
    input_text = remove_stop_words(input_text, stopList)

    # Tokenize and save result
    words = input_text.split()
    result = "\n".join([f"{i + 1}. {word}" for i, word in enumerate(words)])

    result_file_path = input_file_path.replace(".txt", "_Result.txt")
    with open(result_file_path, "w", encoding="utf-8") as result_file:
        result_file.write(result)

    print(
        """
     ____                       _
    |  _ \   ___   _ __    ___ | |
    | | | | / _ \ | '_ \  / _ \| |
    | |_| || (_) || | | ||  __/|_|
    |____/  \___/ |_| |_| \___|(_)
          """
    )
    print(f"Tokenization completed! Result saved in {result_file_path}")
    time.sleep(10)


# 1
def get_text_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


# 2
def remove_punctuation(text, punc_list):
    for punc in punc_list:
        text = text.replace(punc, "")
    return text


# 3
def remove_extra_spaces(text):
    text = text.strip()
    return text


# 4
def replace_chars(text):
    text = text.replace(" ک ", " که ").replace(" ی ", " یه ").replace(" چ ", " چه ")
    return text


# 5 ---NEEDS A CHECK---
# def remove_hamzeh(text):
#    hamzeh_list = ["ؤ", "ئ", "أ", "إ"]
#    for hamzeh in hamzeh_list:
#        text = text.replace(hamzeh, "")
#    return text


# Another and maybe better approach?
def remove_hamzeh(text):
    text = text.replace("ؤ", "و").replace("ئ", "ی").replace("أ", "ا").replace("إ", "ا")
    text = re.sub("[َُِّْ]", "", text)
    return text


# 6
def remove_hamzeh_end(text):
    text = re.sub(r"([^\W\d_])\sء\b", r"\1", text)
    return text


# 7
def replace_a(text):
    text = text.replace("آ", "ا")
    return text


# 8
def remove_tashdid(text):
    text = re.sub(r"(\w)\1+", r"\1", text)
    return text


# 9
def replace_numbers(text):
    persian_numbers = {
        "۰": "0",
        "۱": "1",
        "۲": "2",
        "۳": "3",
        "۴": "4",
        "۵": "5",
        "۶": "6",
        "۷": "7",
        "۸": "8",
        "۹": "9",
    }

    for persian, latin in persian_numbers.items():
        text = text.replace(persian, latin)

    return text


# 10
# def fix_nbsp(text):
#    text = text.replace("‌", "")
#    return text


# 11
def fix_arabic(text):
    text = text.replace("ة", "ه").replace("٤", "۴").replace("٥", "۵").replace("٦", "۶")
    text = text.replace("ك", "ک").replace("ي", "ی").replace("ـ", "")
    return text


# 12
def remove_duplicate_spaces(text):
    text = re.sub(r"\s+", " ", text)
    return text


# 13
def attach_suffixes(text):
    text = re.sub(
        r"\b(ترین|تر|ها|های|هایی|هایم|هایت|هایش|هایمان|هایتان|هایشان|ات|اتی|اتان|اتانی|اتانیم|ان)\b",
        r"\1",
        text,
    )
    return text


# 14
def fix_prefix_spacing(text):
    prefixes = ["بی", "برمی", "درمی", "نمی", "می"]
    for prefix in prefixes:
        text = text.replace(f" {prefix} ", f"{prefix} ")
    return text


# 15
def remove_stop_words(text, stop_list):
    for stop_word in stop_list:
        text = re.sub(r"\b" + stop_word + r"\b", "", text)
    return text


# ------------------The code structure is a bit complex, yet clean.-----------------------

# Here we go!
print(
    """
 ______   ______   ______   __  __ 
/\  == \ /\__  _\ /\  == \ /\ \_\ \\
\ \  _-/ \/_/\ \/ \ \  _-/ \ \____ \\
 \ \_\      \ \_\  \ \_\    \/\_____\\    ▄█ ░ █▀█  
  \/_/       \/_/   \/_/     \/_____/    ░█ ▄ █▄█
      """
)
input_file_path = input(
    "What is your input path? You can also drag and drop here!\n@v@?"
)
tokenize_text(input_file_path)
