import smtplib

sunucu=smtplib.SMTP('smtp.gmail.com', 587)
sunucu.ehlo()
sunucu.starttls()
sunucu.login("google hesap adı", "şifre")
to=["gönderilecek mail"]
mesaj="Deneme"
try:
    sunucu.sendmail('google hesap adı',to,mesaj)
    print ('Mail gönderimi başarılı')
except:
    print ('Mail gönderimi başarısız')

sunucu.quit()


#gmail olmaz ise 
#mail = SMTP_SSL("smtp.yandex.com", 465) # yandex için
#SMTP("smtp-mail.outlook.com",587) # outlook için