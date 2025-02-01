[app]

# Название приложения
title = My Kivy App

# Имя пакета (должно быть уникальным)
package.name = mykivyapp

# Домен (например, com.example)
package.domain = org.example

# Директория с исходным кодом
source.dir = .

# Исходный код
source.include_exts = py,png,jpg,kv,atlas

# Основной файл приложения
source.include_patterns = assets/*,images/*,*.kv

# Версия приложения
version = 1.0

# Требования (библиотеки)
requirements = kivy

# Разрешения Android
android.permissions = INTERNET

# Минимальная версия Android
android.minapi = 21

# Целевая версия Android
android.targetapi = 31

# Архитектура
android.arch = armeabi-v7a
