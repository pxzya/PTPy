# PTPy 2.0 - Persian Text Tokenizer

PTPy is a fast, easy-to-use, open-source Persian text tokenizer for Python. It cleans, normalizes, and tokenizes Persian-language texts, making them ready for further processing in machine learning, information retrieval, and natural language processing tasks.

## ✨ Features

- **Multi-Stage Tokenization:** Cleans and processes Persian text through 15 distinct phases.
- **Stop Words Removal:** Extensive built-in list of Persian stop words (500+ items) for flexible text filtering.
- **Character & Number Normalization:** Corrects common character issues and converts numbers to a uniform format.
- **Handles Arabic & Persian Variants:** Replaces Arabic characters with their Persian equivalents.
- **Built for CMD:** Simple command-line operation and drag-and-drop support.
- **Highly Readable Code:** Each step is well-commented for easy understanding and modification.

## ⚙️ How It Works

PTPy processes your Persian text file through the following main steps:

1. **Input Reading:** Reads the text file specified by the user.
2. **Punctuation Removal:** Strips out punctuation symbols.
3. **Whitespace Normalization:** Cleans up extra spaces and duplicate whitespace.
4. **Character Replacement:** Normalizes common Persian/Arabic character issues and fixes numerals.
5. **Suffix/Prefix Fixing:** Attaches frequent suffixes and prefixes correctly to words.
6. **Stop Word Filtering:** Removes stop words from the text.
7. **Token Output:** Produces a numbered list of tokens, saved as a new file.

The tokenizer is modular and easily extensible. Each processing phase is defined as a clean, separate function in the code.

## 🖥️ Requirements

| Requirement        | Version   |
|--------------------|-----------|
| Python             | 3.11+     |

No external libraries are required—standard Python only.

## 🚀 Usage

### 1. Prepare Your Input File

- Make sure your input text file is encoded as UTF-8.
- The file path **must not contain spaces** (move to desktop if needed, or rename path/folders).

### 2. Run the Tokenizer

From the command line (CMD):

```sh
python PTPy.py
```

When prompted, **type or drag-and-drop your file path** into the terminal and press `Enter`.

### 3. Get Results

- The tokenized output will be saved in the same location as your input file, with `_Result.txt` appended to the filename. 
- Terminal will notify you once tokenization is complete.

## 📝 Example

Suppose you have a file named `mytext.txt` on your Desktop.

To tokenize:

```sh
python PTPy.py
```

When asked:

```
What is your input path? You can also drag and drop here!
@v@?
```

Enter:

```
C:\Users\YourName\Desktop\mytext.txt
```

Your result will appear as:

```
mytext_Result.txt
```

with tokens enumerated line by line.

## 📁 Repository Structure

```
PTPy/
├── PTPy.py             # Main tokenizer script
├── stopWordList.py     # Extensive Persian stop word list
```

## 📂 Customization

- **Stop Word List:** To use a larger stop word list, edit the relevant section in `PTPy.py` (phase 15) to use `fullStopList` from `stopWordList.py`.
- **Processing Phases:** Each phase is a separate, well-named function for easy editing.

## 🛡️ License

This project is copyrighted (c) 2023 Pouya Abbasi.

## 🤝 Contributing

Pull requests and issues are welcome! Please read and follow the code comments and structure for smooth collaboration.
