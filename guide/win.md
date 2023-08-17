# Запуск проекта на Windows

Клонируйте репозитроий и перейдите в директорию `api_final_yatube`.

```bash
git clone git@github.com:Wiz410/api_final_yatube.git
```

```bash
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```bash
python -m venv venv
```

```bash
source venv/Scripts/activate
```

Установите зависимости из файла `requirements.txt`:

```bash
python -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

Перейдите в директорию `yatube_api`.

```bash
cd yatube_api
```

Выполните миграции и запустите проект.

```bash
python manage.py migrate
```

```bash
python manage.py runserver
```