# Create virtual environment and install dependencies

```bash
$ virtualenv venv -p $(which python3)
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```

# Execution

```bash
(venv) $ python main.py  # English
(venv) $ LOCALE=de python main.py  # German
(venv) $ LOCALE=jp python main.py  # Japanese
```
