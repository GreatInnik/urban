def send_mail(message, recipient, sender='university.help@gmail.com'):
    if '@' not in recipient or (".com" not in recipient and ".ru" not in recipient and ".net" not in recipient):
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient, ".")
        return

    if '@' not in sender or (".com" not in sender and ".ru" not in sender and ".net" not in sender):
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient, ".")
        return

    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return

    if sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)


send_mail("Здравствуйте", 'pochtagmail.com')
send_mail("Здравствуйте", 'university.help@gmail.com')
send_mail("Здравствуйте", 'pochta@gmail.com', "university@gmail.com")