"""
YMS 301 - Lab 01: CLI Sistem Bilgilendirici
Açıklama: Komut satırından kullanıcı adını alır ve sistem bilgilerini
formatlı bir rapor olarak ekrana basar.
"""

import os
import sys


def kullanim_mesaji_goster() -> None:
    """Argüman eksikse kullanıcıyı uyarır."""
    print("Kullanım: python main.py <Kullanici_Adi>")


def sistem_kullanicisini_bul() -> str:
    """İşletim sistemindeki oturum açmış kullanıcının adını döndürür."""
    try:
        return os.getlogin()
    except OSError:
        return os.environ.get("USERNAME") or os.environ.get("USER") or "bilinmiyor"


def rapor_yazdir(gelistirici: str) -> None:
    """Sistem analiz raporunu formatlı biçimde yazdırır."""
    cizgi = "=" * 41
    print(cizgi)
    print("YMS 301 - SISTEM ANALIZ RAPORU")
    print(cizgi)
    print(f"Geliştirici       : {gelistirici}")
    print(f"Sistem Kullanıcısı: {sistem_kullanicisini_bul()}")
    print(f"Çalışma Dizini    : {os.getcwd()}")
    print(f"İşlemci Çekirdeği : {os.cpu_count()} Çekirdek")
    print("Durum             : Sistem Hazır.")
    print(cizgi)


def main() -> None:
    """Programın giriş noktası."""
    if len(sys.argv) < 2:
        kullanim_mesaji_goster()
        return
    rapor_yazdir(sys.argv[1])


if __name__ == "__main__":
    main()
