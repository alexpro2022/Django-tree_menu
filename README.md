# Проект tree-menu: 
[![Tree-menu CI/CD](https://github.com/alexpro2022/menu-tree/actions/workflows/main.yml/badge.svg)](https://github.com/alexpro2022/menu-tree/actions/workflows/main.yml)
[![codecov](https://codecov.io/gh/alexpro2022/<REPOSITIRY_NAME>/branch/master/graph/badge.svg?token=1ETL9DOJEB)](https://codecov.io/gh/alexpro2022/<REPOSITIRY_NAME>)



## Оглавление:
- [Технологии](#технологии)
- [Описание работы](#описание-работы)
- [Установка и запуск](#установка-и-запуск)
- [Автор](#автор)



## Технологии:

<details><summary>Развернуть</summary>

**Языки программирования, библиотеки и модули:**

[![Python](https://img.shields.io/badge/Python-v3.10-blue?logo=python)](https://www.python.org/)

**Фреймворк, расширения и библиотеки:**

[![Django](https://img.shields.io/badge/Django-v4.2.1-blue?logo=Django)](https://www.djangoproject.com/)


**Базы данных и инструменты работы с БД:**

[![SQLite3](https://img.shields.io/badge/-SQLite3-464646?logo=SQLite)](https://www.sqlite.com/version3.html)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?logo=PostgreSQL)](https://www.postgresql.org/)


<!--**Тестирование:**

[![Pytest](https://img.shields.io/badge/-Pytest-464646?logo=Pytest)](https://docs.pytest.org/en/latest/)
[![Pytest-cov](https://img.shields.io/badge/-Pytest--cov-464646?logo=Pytest)](https://pytest-cov.readthedocs.io/en/latest/)
[![Coverage](https://img.shields.io/badge/-Coverage-464646?logo=Python)](https://coverage.readthedocs.io/en/latest/)
-->

**CI/CD:**

[![GitHub_Actions](https://img.shields.io/badge/-GitHub_Actions-464646?logo=GitHub)](https://docs.github.com/en/actions)
[![docker_hub](https://img.shields.io/badge/-Docker_Hub-464646?logo=docker)](https://hub.docker.com/)
[![docker_compose](https://img.shields.io/badge/-Docker%20Compose-464646?logo=docker)](https://docs.docker.com/compose/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?logo=gunicorn)](https://gunicorn.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?logo=NGINX)](https://nginx.org/ru/)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?logo=Yandex)](https://cloud.yandex.ru/)
[![Telegram](https://img.shields.io/badge/-Telegram-464646?logo=Telegram)](https://core.telegram.org/api)

[⬆️Оглавление](#оглавление)
</details>



## Описание работы:
Add your description here

[⬆️Оглавление](#оглавление)



## Установка и запуск:
Удобно использовать принцип copy-paste - копировать команды из GitHub Readme и вставлять в командную строку Git Bash или IDE (например VSCode).
### Предварительные условия для Docker Compose:
<details><summary>Развернуть</summary>

Предполагается, что пользователь:
 - создал аккаунт [DockerHub](https://hub.docker.com/), если запуск будет производиться на удаленном сервере.
 - установил [Docker](https://docs.docker.com/engine/install/) и [Docker Compose](https://docs.docker.com/compose/install/) на локальной машине или на удаленном сервере, где проект будет запускаться в контейнерах. Проверить наличие можно выполнив команды:
    ```
    docker --version && docker-compose --version
    ```
</details>
<hr>
<details><summary>Локальный запуск</summary> 

**!!! Для пользователей Windows обязательно выполнить команду:** 
```
git config --global core.autocrlf false
```
иначе файл start.sh при клонировании будет бракован.

1. Клонируйте репозиторий с GitHub и введите данные для переменных окружения (значения даны для примера, но их можно оставить):
```
git clone git@github.com:alexpro2022/tree-menu.git && \
cd tree-menu && \
cp env_example .env && \
nano .env
```
<details><summary>Локальный запуск: Django/SQLite3</summary>

2. Создайте и активируйте виртуальное окружение:
   * Если у вас Linux/macOS
   ```
    python -m venv venv && source venv/bin/activate
   ```
   * Если у вас Windows
   ```
    python -m venv venv && source venv/Scripts/activate
   ```

3. Установите в виртуальное окружение все необходимые зависимости из файла **requirements.txt**:
```
python -m pip install --upgrade pip && pip install -r requirements.txt
```

4. Выполните миграции, загрузку данных, создание суперюзера и запустите приложение:
```
python tree_menu/manage.py makemigrations && \
python tree_menu/manage.py migrate && \
python tree_menu/manage.py load_data && \
python tree_menu/manage.py create_superuser && \
python tree_menu/manage.py runserver
```
Сервер запустится локально по адресу http://127.0.0.1:8000/

5. Остановить приложение можно комбинацией клавиш Ctl-C.
</details>

<details><summary>Локальный запуск: Docker Compose/PostgreSQL</summary>

2. Из корневой директории проекта выполните команду:
```
docker compose -f infra/local/docker-compose.yml up -d --build
```
Проект будет развернут в трех docker-контейнерах (db, web, nginx) по адресу http://localhost.

3. Остановить docker и удалить контейнеры можно командой из корневой директории проекта:
```
docker compose -f infra/local/docker-compose.yml down
```
Если также необходимо удалить тома базы данных, статики и медиа:
```
docker compose -f infra/local/docker-compose.yml down -v
```
</details><hr></details>

<details><summary>Запуск на удаленном сервере</summary>

1. Сделайте [форк](https://docs.github.com/en/get-started/quickstart/fork-a-repo) в свой репозиторий.

2. Создайте Actions.Secrets согласно списку ниже (значения указаны для примера) + переменные окружения из env_example файла:
```
PROJECT_NAME
SECRET_KEY

POSTGRES_PASSWORD
DATABASE_URL

CODECOV_TOKEN

DOCKERHUB_USERNAME
DOCKERHUB_PASSWORD

# Данные удаленного сервера и ssh-подключения:
HOST  # публичный IP-адрес вашего удаленного сервера
USERNAME
SSH_KEY  
PASSPHRASE

# Учетные данные Телеграм-бота для получения сообщения о успешном завершении workflow:
TELEGRAM_USER_ID
TELEGRAM_BOT_TOKEN
```

3. Запустите вручную workflow, чтобы автоматически развернуть проект в трех docker-контейнерах (db, web, nginx) на удаленном сервере.
</details><hr>

При первом запуске будут автоматически произведены следующие действия:
  - выполнены миграции БД
  - БД заполнена начальными данными
  - собрана статика
  - создан суперюзер (пользователь с правами админа) с учетными данными:
      - Django: username = 'adm', password = 'adm' - значения можно изменить в `tree_menu\app\management\commands\create_superuser.py`
      - Docker Compose - из переменных окружения ADMIN_USERNAME, ADMIN_EMAIL, ADMIN_PASSWORD
      
 

Меню представлены по адресу (в зависимости от способа запуска):
  - http://127.0.0.1:8000/menu/
  - http://localhost/menu/
  - http://<IP-адрес удаленного сервера>/menu/main/

Вход в админ-зону осуществляется по адресу (в зависимости от способа запуска):
  - http://127.0.0.1:8000/admin/
  - http://localhost/admin/
  - http://<IP-адрес удаленного сервера>/admin/



[⬆️Оглавление](#оглавление)



## Автор:
[Aleksei Proskuriakov](https://github.com/alexpro2022)

[⬆️В начало](#Проект)