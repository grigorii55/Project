from docx import Document

title = input("Введите заголовок статьи: ")
filename = input("Введите имя Word-файла (например, Статья 1.docx): ")

# Открываем Word документ
doc = Document(filename)

# Читаем весь текст
content = ""
for para in doc.paragraphs:
    content += para.text + "<br>\n"

# Генерируем HTML
html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header>
    <h1>{title}</h1>
    <nav>
      <a href="index.html">Главная</a>
      <a href="recommendations.html">Рекомендации</a>
      <a href="news.html" class="active">Новости</a>
      <a href="contacts.html">Контакты</a>
    </nav>
  </header>

  <section class="section">
    <h2>{title}</h2>
    <p>
    {content}
    </p>
  </section>

  <footer>
    <p>&copy; 2025 Koki. Все права защищены.</p>
  </footer>
</body>
</html>
"""

# Сохраняем в HTML
output_filename = filename.replace('.docx', '.html')
with open(output_filename, 'w', encoding='utf-8') as output:
    output.write(html)

print(f"HTML-файл '{output_filename}' успешно создан!")
