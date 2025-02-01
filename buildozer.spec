[app]

# Название приложения
title = My Kivy App

# Уникальное имя пакета (измените под себя)
package.name = mykivyapp

# Доменное имя пакета (измените под себя)
package.domain = org.example

# Директория с исходным кодом
source.dir = .

# Включаемые файлы исходного кода
source.include_exts = py,png,jpg,kv,atlas

# Основной файл приложения (если у вас main.py, измените)
source.include_patterns = assets/*,images/*,*.kv,main.py

# Версия приложения
version = 1.0

# Требования (библиотеки, добавил нужные для сборки)
requirements = python3,kivy,kivymd

# Разрешения Android (если нужен доступ к файлам, добавьте WRITE_EXTERNAL_STORAGE)
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Минимальная версия Android
android.minapi = 21

# Целевая версия Android
android.targetapi = 31

# Архитектура (добавил arm64-v8a для поддержки современных устройств)
android.arch = armeabi-v7a,arm64-v8a

# Указываем имя главного Python-файла (если у вас не main.py — измените)
source.include_patterns = main.py

# Графический движок (нужен для работы Kivy)
android.presplash_color = #000000
android.meta_data = android.permission.QUERY_ALL_PACKAGES

# Оптимизация (убирает ненужные файлы)
android.add_jars = 
android.add_src = 
android.allow_cleartext_default = True
android.release = False
