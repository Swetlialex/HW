import json

# Зареждане на данните от файл
with open("pythonbooks.revolunet.com.issues.json", "r", encoding="utf-8") as f:
    data_f = json.load(f)

# Създаване на нова структура по категории
filtered_books = {
    "Advanced": [],
    "Beginner": [],
    "Intermediate": []
}

# Филтриране на книгите по ниво
for book in data_f["books"]:
    level = book.get("level")
    if level in filtered_books:
        filtered_books[level].append({
            "title": book["title"],
            "author": book["author"],
            "url": book["url"]
        })

# Записване в нов JSON файл
with open("rearanged_books_by_category.json", "w", encoding="utf-8") as output_file:
    json.dump(filtered_books, output_file, ensure_ascii=False, indent=4)

print(" Файлът 'rearanged_books_by_category.json' е създаден успешно.")


