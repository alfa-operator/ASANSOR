#ASANSÖR UYGULAMASI
import time#zaman modülünü içe aktarıyoruz
kat=0# başlangıç değeri oluşturuyoruz
while True:#sürekli döngü 
    
    seçim=int(input('HANGİ KAT: '))#kullanıcıdan talep alıyoruz seçim  e int i esitliyoruz
    #ki değeri  rakam olarak yazmak için.
#---------‐-----------------------------------------------------------------------------------------------------------------------
#KAT ARALIĞI VE HATA KONTROLU 
    if seçim > 7 or seçim < -3:# burden fazla aynı sart sağlanırsa çalışır 
    #bu yöntemi de or  ile yapıyoruz.
        print('⛔️GEÇERSİZ SEÇİM LÜTFEN 7 İLE-3 ARASINDA KAT GİRİN')#uyarı ve yönlendirme ekliyoruz.
        continue# döngüye devam eriyoruz.
  #---------‐-----------------------------------------------------------------------------------------------------------------------
  #YUKARI ÇIKMA  
    if seçim > kat:# gideceğimiz kat 0 dan yüksekse misal 5
    
        print(f'{seçim}. kata çıkıyor')# o kata çıktığımızı belirtiyor.
        for i in range(kat,seçim+1):#mevcut kattan seçtiğimiz kata 1er 1er 
        #artırıyoruz 
            time.sleep(0.3)#gecikmeli yazdırıyoruz,sonraki satırı 
            #biraz gerçekçi olsun diye
            print(i)#for i in range yi yazdırıyoruz
            
            kat=seçim#kat ile seçim esitliyoruz ki her seferinde 
            #0 dan başlamasın gerçekçi olsun diye
#---------‐-----------------------------------------------------------------------------------------------------------------------  
#AŞAĞI İNME      
    #12 ile 21 arasındaki satırların aynı mantığı 
    #tek fark aşağı inmesi
    elif seçim < kat:
        print(f'{seçim}. kata iniyor')
        for i in range(kat, seçim-1,-1):
            time.sleep(0.1)
            print(i)
            kat=seçim
#---------‐-----------------------------------------------------------------------------------------------------------------------
#BİLGİLENDİRME
    elif seçim == kat:
        print('burdasiniz')
