# Проект tree-menu: 
[![Tree-menu CI/CD](https://github.com/alexpro2022/Django-tree_menu/actions/workflows/main.yml/badge.svg)](https://github.com/alexpro2022/Django-tree_menu/actions/workflows/main.yml)

### Древовидное меню на Django, испоьзуя custom template tag.

[Тестовое задание](https://docs.google.com/document/d/1XTnbcXhejyGB-I2cHRiiSZqI3ElHzqDJeetwHkJbTa8/edit?usp=sharing)

<br>

## Оглавление:
- [Технологии](#технологии)
- [Установка и запуск](#установка-и-запуск)
- [Описание работы](#описание-работы)
- [Удаление](#удаление)
- [Автор](#автор)

<br>

## Технологии:

<details><summary>Подробнее</summary>

**Языки программирования, библиотеки и модули:**

[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11-blue?logo=python)](https://www.python.org/)

**Фреймворк, расширения и библиотеки:**

[![Django](https://img.shields.io/badge/Django-v4.2.1-blue?logo=Django)](https://www.djangoproject.com/)


**Базы данных и инструменты работы с БД:**

[![SQLite3](https://img.shields.io/badge/-SQLite3-464646?logo=SQLite)](https://www.sqlite.com/version3.html)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?logo=PostgreSQL)](https://www.postgresql.org/)



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

<br>

## Установка и запуск:
Удобно использовать принцип copy-paste - копировать команды из GitHub Readme и вставлять в командную строку Git Bash или IDE (например VSCode).

<details><summary>Предварительные условия</summary>

Предполагается, что пользователь:
 - создал аккаунт [DockerHub](https://hub.docker.com/), если запуск будет производиться на удаленном сервере.
 - установил [Docker](https://docs.docker.com/engine/install/) и [Docker Compose](https://docs.docker.com/compose/install/) на локальной машине или на удаленном сервере, где проект будет запускаться в контейнерах. Проверить наличие можно выполнив команды:
    ```bash
    docker --version && docker-compose --version
    ```
<h1></h1>
</details>

<details><summary>Локальный запуск</summary> 

**!!! Для пользователей Windows обязательно выполнить команду:** 
```bash
git config --global core.autocrlf false
```
иначе файл start.sh при клонировании будет бракован.

1. Клонируйте репозиторий с GitHub и введите данные для переменных окружения (значения даны для примера, но их можно оставить):
```bash
git clone https://github.com/alexpro2022/Django-tree_menu.git && \
cd Django-tree_menu && \
cp env_example .env && \
nano .env
```
<details><summary>Локальный запуск: Django/SQLite3</summary>

2. Создайте и активируйте виртуальное окружение:
   * Если у вас Linux/macOS
   ```bash
    python -m venv venv && source venv/bin/activate
   ```
   * Если у вас Windows
   ```bash
    python -m venv venv && source venv/Scripts/activate
   ```

3. Установите в виртуальное окружение все необходимые зависимости из файла **requirements.txt**:
```bash
python -m pip install --upgrade pip && pip install -r requirements.txt
```

4. Выполните миграции, загрузку данных, создание суперюзера и запустите приложение:
```bash
python tree_menu/manage.py makemigrations && \
python tree_menu/manage.py migrate && \
python tree_menu/manage.py load_data && \
python tree_menu/manage.py create_superuser && \
python tree_menu/manage.py runserver
```
Сервер запустится локально по адресу `http://127.0.0.1:8000/`

5. Остановить приложение можно комбинацией клавиш Ctl-C.
<h1></h1>
 </details>

<details><summary>Локальный запуск: Docker Compose/PostgreSQL</summary>

2. Из корневой директории проекта выполните команду:
```bash
docker compose -f infra/local/docker-compose.yml up -d --build
```
Проект будет развернут в трех docker-контейнерах (db, web, nginx) по адресу `http://localhost`.

3. Остановить docker и удалить контейнеры можно командой из корневой директории проекта:
```bash
docker compose -f infra/local/docker-compose.yml down
```
Если также необходимо удалить тома базы данных, статики и медиа:
```bash
docker compose -f infra/local/docker-compose.yml down -v
```
</details><h1></h1></details>

<details><summary>Запуск на удаленном сервере</summary>

1. Сделайте [форк](https://docs.github.com/en/get-started/quickstart/fork-a-repo) в свой репозиторий.

2. Создайте `Actions.Secrets` согласно списку ниже (значения указаны для примера) + переменные окружения из env_example файла:
```py
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

3. Запустите вручную `workflow`, чтобы автоматически развернуть проект в трех docker-контейнерах (db, web, nginx) на удаленном сервере.
</details><h1></h1>

При первом запуске будут автоматически произведены следующие действия:
  - выполнены миграции БД
  - БД заполнена начальными данными
  - собрана статика
  - создан суперюзер (пользователь с правами админа) с учетными данными:
      - для Django: username = 'adm', password = 'adm' - значения можно изменить в `tree_menu\app\management\commands\create_superuser.py`
      - для Docker Compose - из переменных окружения `ADMIN_USERNAME`, `ADMIN_EMAIL`, `ADMIN_PASSWORD`
      
 

Меню представлены по адресу (в зависимости от способа запуска):
  - http://127.0.0.1:8000/menu/
  - http://localhost/menu/
  - `http://<IP-адрес удаленного сервера>/menu/`

Вход в админ-зону осуществляется по адресу (в зависимости от способа запуска):
  - http://127.0.0.1:8000/admin/
  - http://localhost/admin/
  - `http://<IP-адрес удаленного сервера>/admin/`

[⬆️Оглавление](#оглавление)

<br>

## Описание работы:

На странице `http://<hostname>/menu/` представлены четыре тестовых меню, при клике на название которых происходит переход на страницу данного меню. Возврат в главное меню происходит при клике `В главное меню`.
Принцип работы приложения основан на выборке из БД всех пунктов меню, которые имеют в поле `menu` название выбранного меню. Название выбранного меню извлекается из url. Далее происходит отображение этого меню. При клике на пункт меню происходит рекурсивный поиск по извлеченным данным, чтобы построить список пунктов которые должны быть открыты на пути к этому пункту меню. Далее данный список передается в шаблон который выводит пункты меню, рекурсивно вызывая себя при выводе развернутых пунктов меню. Такой алгоритм позволяет обратиться к любому пункту меню указав в url только имя меню и его пункт. Например, при вводе url (в зависимости от типа локального запуска)

  - http://127.0.0.1:8000/menu/first%20menu/Menu%20item/
  - http://localhost/menu/first%20menu/Menu%20item/


произойдет переход на пункт меню `Menu item` с отрисовкой всех уровней вложенности меню `first menu` на пути к этому пункту меню.


[⬆️Оглавление](#оглавление)

<br>

## Удаление:
Для удаления проекта выполните следующие действия:
```bash
cd .. && rm -fr Django-tree_menu && deactivate
```
  
[⬆️Оглавление](#оглавление)

<br>

## Автор:
[Aleksei Proskuriakov](https://github.com/alexpro2022)

[⬆️В начало](#Проект)
