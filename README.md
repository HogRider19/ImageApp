<h2 align="center">ImageApp</h2>


### Описание проекта:
Небольшой api для обмена картинками 


**Технологии:**
- Python = 3.11
- fastapi = 0.89.1
- Postgresql = 15.1
- alembic==1.9.1

<br>

## **Запуск проекта:**
---
##### 1) Клонировать репозиторий

    git clone ссылка_сгенерированная_в_вашем_репозитории

##### 2) Создать виртуальное окружение

    python -m venv venv
    
##### 3) Активировать виртуальное окружение
    
    venv/Scripts/activate

##### 4) Устанавливить зависимости:

    pip install -r requirements.txt

##### 5) Создать .env файл:

    Пример содержания в env.example
    
##### 6) Выполнить команду для выполнения миграций

    alembic upgrade head
    
##### 7) Запустить сервер

    uvicorm main:app

<br>

## **Запуск проекта через Docker:**
---
##### 1) Запустить docker-compose

    docker-compose up
    