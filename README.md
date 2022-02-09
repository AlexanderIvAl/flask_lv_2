# Развертывание на локальной машине
1. Создаем виртуальное окружение: python3 -m venv flask_venv
1. Активируем venv: source flask_venv/bin/activate
1. Устанавливаем зависимости: pip install -r requirements.txt
1. Создаем локальную БД: flask db upgrade


# Работа с GitHub
Копирование с удаленного репозитория: 

git clone https://github.com/AlexanderIvAl/flask_lv_2

Настройка Git:

    *   git init  (Если не установлен то ставим)
    ls -a (Проверяем установку: должна появиться папка .git [флаг -a показывает скрытые файлы и папки])

    *   git config --global user.name "..." (Вводим имя пользователя)

    *   git config --global user.email "..." (Вводим email пользователя)

    *   создаем текстовый файл  .gitignore (В нем прописываем все игнорируемые  файлы и папки *.db, __pycache__/)

    *   git add . (Формируем изменения)

    *   git status (Проверяем что внесется в изменения)

    *   git commit -m "..." (Создаем коммит с изменениями)


Выгрузка в удаленный депозиторий

    *   Формируем изменения: 

        git add .

    *   Формируем комит с изменениями:

        git commit -m "..."

    *   Загружаем изменения на удаленный репозиторий: 

        git push origin master