# Django Messenger

Ein Messenger, entwickelt mit Django.

## Voraussetzungen

- Python 3.12+
- Git
- Nginx
- Gunicorn

## Installation

Repository klonen:

```bash
git clone https://github.com/<dein-name>/django-messenger.git
cd django-messenger
```

Virtuelle Umgebung erstellen:

```bash
python -m venv venv
```

Linux/macOS:

```bash
source venv/bin/activate
```

Windows:

```powershell
venv\Scripts\activate
```

Abhängigkeiten installieren:

```bash
pip install -r requirements.txt
```

Migrationen ausführen:

```bash
python manage.py migrate
```

(Optional) Admin-Benutzer erstellen:

```bash
python manage.py createsuperuser
```

Statische Dateien sammeln:

```bash
python manage.py collectstatic
```

## Anwendung starten

Zum Testen:

```bash
python manage.py runserver
```

Für den Produktivbetrieb mit Gunicorn:

```bash
gunicorn messenger.wsgi:application
```

Die Anwendung wird anschließend über Nginx bereitgestellt.

## Verwendete Technologien

- Django
- SQLite
- Gunicorn
- Nginx
- HTML
- CSS
