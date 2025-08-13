import json

# Зареждане на данните от файл
with open("pythonbooks.revolunet.com.issues.json", "r", encoding="utf-8") as f:
    data_f = json.load(f)

# Филтриране и отпечатване на книги с ниво "Advanced"
print("📘 Книги за напреднали:\n")
i = 0 # номериране на поредната книга
for book in data_f["books"]:
    if book.get("level") == "Advanced":
        i +=1
        print(f"№{i}")
        print(f"Заглавие : {book['title']}")
        print(f"Автор    : {book['author']}")
        print(f"Линк     : {book['url']}\n")
