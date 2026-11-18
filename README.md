# YMS 301 - Lab 01: CLI Sistem Bilgilendirici

Komut satırından kullanıcı adını alıp sistem bilgilerini (sistem kullanıcısı,
çalışma dizini, işlemci çekirdek sayısı) formatlı bir rapor olarak yazdıran
basit bir Python aracı.

## Gereksinimler

- Python 3.11 veya üzeri
- Dış kütüphane gerekmez (yalnızca `sys` ve `os` kullanılır)

## Kurulum

```bash
python -m venv .venv
# Windows (PowerShell):
.venv\Scripts\Activate.ps1
# macOS / Linux:
source .venv/bin/activate
```

## Çalıştırma

```bash
python main.py <Kullanici_Adi>
```

Örnek:

```bash
python main.py Simge
```

Argüman verilmezse program çökmez, kullanım bilgisini gösterir:

```
Kullanım: python main.py <Kullanici_Adi>
```

## Örnek Çıktı

```
=========================================
YMS 301 - SISTEM ANALIZ RAPORU
=========================================
Geliştirici       : Simge
Sistem Kullanıcısı: simge
Çalışma Dizini    : C:\workspace\yms301-lab1
İşlemci Çekirdeği : 8 Çekirdek
Durum             : Sistem Hazır.
=========================================
```
