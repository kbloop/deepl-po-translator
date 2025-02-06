# deepl-po-translator - Automated Translation for .po Files Using DeepL

deepl-po-translator is a Python-based tool that automates the translation of `.po` files using the DeepL API. It ensures placeholders, special characters (like `« »`), and formatting are preserved, making it perfect for localizing applications efficiently.

## ✨ Features
- 🌍 **Automated Translation** – Translates `.po` files from one language to another using DeepL.  
- 🔤 **Preserves Formatting** – Keeps special characters (`« »`, `{variables}`) and placeholders intact.  
- 🛠 **Handles Multi-Line Entries** – Supports complex `.po` files with multi-line `msgid` values.  
- ⚡ **Efficient API Calls** – Batches requests to minimize API usage while maximizing speed.  
- 📄 **Easy Integration** – Works with gettext `.po` files used in web and software localization.  

## 📦 Installation
### **1. Clone the Repository**
```sh
git clone https://github.com/yourusername/deepl-po-translator.git
cd deepl-po-translator
```
### **2. Create a Virtual Environment (Optional but Recommended)**
```sh
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```
### **3. Install Dependencies**
```sh
pip install -r requirements.txt
```
## 🚀 Usage

Basic Commands

```sh
python3 translate.py
```
This will translate .po files using the DeepL API.

## 🛠 Configuration
Set your DeepL API Key:
```sh
AUTH_KEY = "your-deepl-api-key"
```
Modify FILE_PATH in translate.py to point to your .po files:
```sh
FILE_PATH = "/path/to/your/po/files"
```
Change source and target languages (e.g., FR → ES → EN → DE)

## 📝 License

This project is licensed under the MIT License – feel free to modify and use it!
