Zaafiyet:

Sorguda username ve numara sorguya direkt dahil edildiği için zafiyet oluşur.
Username alanına : admin’ -- yazılırsa ,uygulama şifrenin doğruluğunu kontrol etmeden giriş sağlar.


Çözüm :
 
Parametreli sorgu kullanarak bunun önüne geçeriz çünkü parametreli sorgularda input bir nesne olarak ele alınır.
Parametreli sorgular kullanılırsa, kullanıcıdan gelen veri sorgunun bir parçası değil, sadece bir değişken olarak ele alınır.

