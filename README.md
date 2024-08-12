# BLUM AUTO

## Persiapan

Pastikan kamu sudah install:

- [Python](https://www.python.org/downloads/release/python-31014/) **version 3.10**

## Cara Bikin API ID dan API HASH

1. Buka [my.telegram.org](https://my.telegram.org/) , login pake nomer hape akun.
2. Pilih "API development tools" dan isi form nya buat bikin applikasi baru.
3. Simpan **API_ID** dan **API_HASH** , lalu taruh di file .env.

## Request API KEY

Kamu bisa request API KEY di private channel telegram dzuhri-auto. (limited)

## Cara Install

Download [**repository**](https://github.com/HiddenCodeDevs/BlumTelegramBot) lalu git clone ke pc / vps kamu:

```shell
git clone https://github.com/dzuhri-auto/blum.git
```

Masuk ke folder nya

```shell
cd blum
```

Lalu bisa pake command dibawah untuk otomatis install:

**Windows** :

```shell
run.bat
```

**Linux** :

```shell
run.sh
```

## Linux manual installation

```shell
sudo sh install.sh
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
cp .env-example .env
nano .env  # isi API_ID, API_HASH dan API KEY
python3 main.py
```

## Windows manual installation

```shell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env-example .env
# isi API_ID, API_HASH dan API KEY
python main.py
```
