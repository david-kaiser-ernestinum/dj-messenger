# Django Messenger

Ein Messenger, entwickelt mit Django.

## Voraussetzungen

- Python 3.12+
- Git
- Nginx

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

### Einen neuen Schlüssel generieren:

Um einen sicheren Schlüssel zu erstellen braucht es zuerst einen temporären Schlüssel:

Linux/macOS:

```bash
export SECRET_KEY="temp-key"
python manage.py shell
```

Nun kann der sichere Schlüssel generiert werden:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

Den ausgegebenen Wert als `SECRET_KEY` setzen.

Linux/macOS:

```bash
export SECRET_KEY="dein-generierter-key"
```

Windows Command Line:

```powershell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
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

### Django Einstellungen

In `settings.py`:

```python
DEBUG = False

ALLOWED_HOSTS = [
    "deine-domain.de",
    "www.deine-domain.de",
]
```

Ersetze `deine-domain.de` durch deine tatsächliche Domain.

### Gunicorn einrichten

Gunicorn starten:

```bash
gunicorn dj_chat.wsgi:application --bind 127.0.0.1:8000
```
### Nginx konfigurieren

Neue Konfiguration erstellen:

```bash
sudo nano /etc/nginx/sites-available/dj-messenger
```

Beispiel:

```nginx
server {
    listen 80;

    server_name deine-domain.de www.deine-domain.de;

    location /static/ {
        alias /pfad/zu/dj-messenger/dj_chat/staticfiles/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;

        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```
Ersetze `deine-domain.de` durch deine tatsächliche Domain.
Ersetze `/pfad/zu/dj-messenger/dj_chat/staticfiles/` durch den tatsächlichen Pfad.

Aktivieren:

```bash
sudo ln -s /etc/nginx/sites-available/dj-messenger /etc/nginx/sites-enabled/
```

Konfiguration testen:

```bash
sudo nginx -t
```

Nginx neu starten:

```bash
sudo systemctl restart nginx
```

## Verwendete Technologien

- Django
- SQLite
- Gunicorn
- Nginx
- HTML
- CSS
