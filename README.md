# Развертывание на локальной машине
1. Создаем виртуальное окружение: python3 -m venv flask_venv
1. Активируем venv: source flask_venv/bin/activate
1. Устанавливаем зависимости: pip install -r requirements.txt
1. Создаем локальную БД: flask db upgrade


# Работа с GitHub
1. Копирование с удаленного репозитория: 

git clone https://github.com/AlexanderIvAl/Flask_kurs2

2. Формируем изменения: 

git add .

3. Формируем комит с изменениями:

git commit -m "..."

4. Загружаем изменения на удаленный репозиторий: 

git push origin master