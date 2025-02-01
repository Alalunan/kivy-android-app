[app]

# Название приложения
title = My Kivy App

# Уникальное имя пакета
package.name = mykivyapp

# Доменное имя пакета
package.domain = org.example

# Директория с исходным кодом
source.dir = .

# Включаемые файлы исходного кода
source.include_exts = py,png,jpg,kv,atlas

# Основной файл приложения (ОСТАВИЛ ОДНУ СТРОКУ)
source.include_patterns = assets/*,images/*,*.kv,main.py

# Версия приложения
version = 1.0

# Требования (зависимости)
requirements = python3,kivy,kivymd

# Разрешения Android
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Минимальная версия Android
android.minapi = 21

# Целевая версия Android
android.targetapi = 31

# Архитектура
android.arch = armeabi-v7a,arm64-v8a

# Графический движок
android.presplash_color = #000000
android.meta_data = android.permission.QUERY_ALL_PACKAGES

# Оптимизация
android.allow_cleartext_default = True
android.release = False
