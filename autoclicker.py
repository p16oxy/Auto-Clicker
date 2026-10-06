import time
import threading
import pyautogui
import keyboard  # Klavye tuşlarını dinlemek için gerekli kütüphane

# Güvenli çıkış aktif (Mouse'u sol üst köşeye götürürseniz acil durur)
pyautogui.FAILSAFE = True

# Varsayılan Ayarlar
TIKLAMA_ARALIGI = 0.1  # Saniye cinsinden tıklama sıklığı
KONTROL_TUSU = 'f6'    # Başlatma/Durdurma tuşu
calisiyor = False

def tiklama_islem_dongusu():
    global calisiyor
    while calisiyor:
        pyautogui.click()
        time.sleep(TIKLAMA_ARALIGI)

def tus_dinleyici():
    global calisiyor
    print(f"\n[Durum] Auto Clicker hazır! Açmak/Kapatmak için **{KONTROL_TUSU.upper()}** tuşuna basın.")
    print("[Bilgi] Çıkış yapmak için menüden 3'ü seçebilirsiniz.\n")
    
    while True:
        # Belirlenen tuşa basıldığını algıla
        if keyboard.is_pressed(KONTROL_TUSU):
            calisiyor = not calisiyor
            if calisiyor:
                print(">> Auto Clicker BAŞLATILDI (Durdurmak için F6'ya basın)")
                # Tıklama döngüsünü ayrı bir iş parçacığında başlat
                t = threading.Thread(target=tiklama_islem_dongusu)
                t.daemon = True
                t.start()
            else:
                print(">> Auto Clicker DURDURULDU")
            
            # Tuşa basılı kalma durumunu önlemek için kısa bir bekleme
            time.sleep(0.3)
        time.sleep(0.05)

def main():
    global TIKLAMA_ARALIGI, KONTROL_TUSU
    
    # Klavye kütüphanesinin yüklü olup olmadığını kontrol edelim
    try:
        import keyboard
    except ImportError:
        print("Hata: 'keyboard' kütüphanesi eksik!")
        print("Lütfen terminale şu komutu yazarak yükleyin: pip install keyboard")
        return

    while True:
        print("\n--- AUTO CLICKER MENÜSÜ ---")
        print(f"1. Tıklama Aralığını Değiştir (Şu an: {TIKLAMA_ARALIGI} saniye)")
        print(f"2. Kontrol Tuşunu Değiştir (Şu an: {KONTROL_TUSU.upper()})")
        print("3. Programı Başlat ve Menüyü Gizle")
        print("4. Çıkış")
        
        secim = input("Seçiminiz (1-4): ")
        
        if secim == '1':
            try:
                yeni_aralik = float(input("Yeni tıklama aralığını saniye cinsinden girin (Örn: 0.05 veya 0.1): "))
                if yeni_aralik > 0:
                    TIKLAMA_ARALIGI = yeni_aralik
                    print(f"Tıklama aralığı {TIKLAMA_ARALIGI} saniye olarak güncellendi.")
                else:
                    print("Aralık 0'dan büyük olmalıdır!")
            except ValueError:
                print("Geçersiz bir sayı girdiniz.")
                
        elif secim == '2':
            yeni_tus = input("Atamak istediğiniz tuşu yazın (Örn: f1, f6, space, a): ").strip().lower()
            if yeni_tus:
                KONTROL_TUSU = yeni_tus
                print(f"Kontrol tuşu **{KONTROL_TUSU.upper()}** olarak değiştirildi.")
                
        elif secim == '3':
            # Tuş dinleme modunu başlat
            print("\nProgram çalışıyor! Konsolu kapatmadan oyununuza veya uygulamanıza dönebilirsiniz.")
            tus_dinleyici()
            break
            
        elif secim == '4':
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, lütfen 1-4 arasında bir sayı girin.")

if __name__ == "__main__":
    main()