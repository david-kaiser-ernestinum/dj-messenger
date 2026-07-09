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
git clone https://github.com/david-kaiser-ernestinum/dj-messenger.git
cd dj-messenger
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


## Umgebungsvariablen einrichten

Das Projekt benötigt einen Django `SECRET_KEY`.

Erstelle eine Umgebungsvariable mit einem eigenen Schlüssel.

In den Projektordner wechseln:
```bash
cd dj_chat
```

Einen neuen Schlüssel generieren:

Linux/macOS:

```bash
export SECRET_KEY="temp-key"
python manage.py shell
```

Windows:

```powershell
$env:SECRET_KEY="temp-key"
python manage.py shell
```

```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

Den ausgegebenen Wert als `SECRET_KEY` setzen.

Linux/macOS:

```bash
export SECRET_KEY="dein-generierter-key"
```

Windows PowerShell:

```powershell
$env:SECRET_KEY="dein-generierter-key"
```



## Datenbank vorbereiten


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



## Anwendung starten (DEBUG)

Zum Testen:

```bash
python manage.py runserver
```


## Anwendung starten (Deployment)

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
