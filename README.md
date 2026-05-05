# 🐍 Python Core Concepts — Tema 2

Proiect realizat în cadrul cursului **DevOps Online — IT School**.
Conține 7 exerciții practice avansate de Python orientate spre DevOps real — logging, hashing, backup, monitorizare și automatizare.

---

## 📁 Structura proiectului

| Fișier | Descriere |
|--------|-----------|
| `log_fake_generator.py` | Generator de log-uri fake cu UUID-uri, niveluri random și timestamps |
| `sha256.py` | Modul utils — hash sha256 pentru string și fișier + encode/decode base64 |
| `test_utils.py` | Testare modul sha256 |
| `backup_file.py` | Backup automat cu detecție modificări prin sha256 hash |
| `disk_monitor.py` | Monitor ocupare disc cu alertă configurabilă prin variabilă de mediu |
| `move_files.py` | Mutare fișiere între directoare cu lock pentru rulare concurentă |
| `ex7.py` | Decodare string base64 și salvare în fișier |

---

## 🚀 Cum rulezi

### Instalare dependențe
```bash
pip install requests
```

### Exercițiul 1 — Generator log-uri fake
```bash
# Generează 20 de linii de log
python3 log_fake_generator.py 20

# Output exemplu:
# 2026-04-19 20:49:59,182 - ERROR - 7dad3e5a-... - Database connection failed
# 2026-04-19 20:49:59,183 - INFO - 3f2c1a8b-... - User authenticated
```

### Exercițiul 2 — Hash sha256
```bash
python3 test_utils.py

# Output:
# Hash of 'Hello, World!': dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f
# Hash of 'test_file.txt': b57906b899834891510c77b2d406cb1274a750646dcdd51551b6003e59724960
```

### Verificare cu comanda Linux
```bash
sha256sum test_file.txt
# Rezultat identic cu Python! ✅
```

### Exercițiul 3 — Backup automat
```bash
# Prima rulare — face backup
python3 backup_file.py test_file.txt
# Backup created: 'backup/test_file.txt_20260419213018'

# A doua rulare fără modificări — skip
python3 backup_file.py test_file.txt
# Fisierul nu a fost modificat, skip backup

# Adaugare in crontab — rulare automată la fiecare minut
# * * * * * python3 /cale/backup_file.py /cale/fisier.txt
```

### Exercițiul 4 — Monitor disc
```bash
# Cu prag default 90%
python3 disk_monitor.py

# Cu prag custom prin variabilă de mediu
export DISK_THRESHOLD=10
python3 disk_monitor.py
# ALERTA: Disc la 40.94%, prag: 10%
```

### Exercițiul 5 — Mutare fișiere
```bash
# Creare fișiere de test
mkdir folder_sursa
for i in {1..10}; do echo "fisier $i" > folder_sursa/fisier$i.txt; done

# Rulare
python3 move_files.py folder_sursa folder_destinatie

# Testare cu 2 instanțe simultan
python3 move_files.py folder_sursa folder_destinatie &
python3 move_files.py folder_sursa folder_destinatie &
```

### Exercițiul 6 — Encode/Decode base64
```bash
python3 test_utils.py

# Output:
# Encoded: SGVsbG8sIFdvcmxkIQ==
# Decoded: Hello, World!
```

### Exercițiul 7 — Decodare base64 în fișier
```bash
python3 ex7.py SGVsbG8sIFdvcmxkIQ== output.txt
cat output.txt
# Hello, World!
```

---

## 🛠️ Tehnologii folosite

- **Python 3**
- `hashlib` — sha256 hashing
- `base64` — encoding/decoding
- `logging` — logging profesional cu niveluri
- `uuid` — generare ID-uri unice
- `shutil` — operații pe fișiere și disc
- `subprocess` — comenzi sistem
- `os`, `sys` — sistem de fișiere
- `random` — valori aleatoare
- `datetime` — timestamps

---

## 📚 Concepte acoperite

- Logging profesional cu `logging` library
- UUID-uri pentru identificatori unici
- Hashing sha256 pentru integritate fișiere
- Module Python reutilizabile
- Backup inteligent cu detecție modificări
- Variabile de mediu pentru configurare
- Race conditions și mecanisme de lock
- Encode/decode base64
- Crontab pentru automatizare

---

## 🔒 Concepte de securitate acoperite

- **sha256 hashing** — stocarea securizată a datelor
- **base64** — encoding pentru transmitere date
- **variabile de mediu** — configurare fără hardcoding credențiale
- **file locking** — prevenirea race conditions

---

## 👤 Autor

**Gheorghe Ștefăniță Cosmin**  
Junior DevOps Engineer  
[GitHub](https://github.com/stefcosmin09-glitch)
