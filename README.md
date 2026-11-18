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

## 1. Hafta Canlı Kodlama Defteri

[`hafta1/canli_kodlama_hafta1.ipynb`](hafta1/canli_kodlama_hafta1.ipynb) dosyasında 1. haftanın
uygulama defteri ve 7 Lab Alıştırması'nın çözümleri yer alıyor. Bu hafta Python'da girintinin blok
belirlemesini, dinamik tiplemeyi, `is None` kalıbını, f-string ve slicing kullanımını, tip ipuçlu ve
docstring'li fonksiyonlar yazmayı ve mutable default argument tuzağını öğrendim. Mini proje olarak
bir parolanın istatistiklerini `dict` olarak döndüren `parola_istatistikleri()` fonksiyonunu yazdım
ve hata ayıklama görevlerinde bir `SyntaxError` ile sessiz bir mantık hatasını düzelttim.

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
