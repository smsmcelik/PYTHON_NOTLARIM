isLogin = True
if isLogin:#== bu doğru mu diye sormaktır#
    print('Sema nın dünyasına hoş geldin!')

#username = 'Semacelik'
#password = 'ananzaaxd123'
#isslogin = (username == 'Semacelik') and (password == 'ananzaaxd123'  )
#isslogin: bool
#if isslogin:
   # print('Sema nın dünyasına hoş geldin!')#

# Girilen kullanıcı adı ve şifreyi kontrol eden basit bir program
#username = input('Kullanıcı adını giriniz: ')
#password = input('Şifrenizi giriniz: ')
#if (username == 'Semacelik') and (password == 'ananzaaxd123'):
 #   print('Sema nın dünyasına hoş geldin!')
#else:
 #   print('Kullanıcı adı veya şifre yanlış!')   # girilen kullanıcı adı veya şifre yanlışsa bu mesajı verir.

username = input('Kullanıcı adını giriniz: ')
password = input('Şifrenizi giriniz: ')
if username == 'Semacelik':
    if password == 'ananzaaxd123':
        print('Sema nın dünyasına hoş geldin!')
    else:
        print('Şifre yanlış!')
else:
    print('Kullanıcı adı yanlış!')
# Bu kod, kullanıcı adı ve şifre kontrolü yapar.
# Eğer kullanıcı adı 'Semacelik' ise, şifre kontrol edilir.
# Eğer şifre 'ananzaaxd123' ise, kullanıcıya hoş geldin mesajı gösterilir.
# Eğer şifre yanlışsa, "Şifre yanlış!" mesajı gösterilir.
# Eğer kullanıcı adı yanlışsa, "Kullanıcı adı yanlış!" mesajı gösterilir.
    