def send_email(message, recipient, *, sender="university.help@gmail.com"):
    # Проверка на корректность e-mail адресов
    def is_valid_email(email):
        return ("@" in email) and (email.endswith(".com") or email.endswith(".ru") or email.endswith(".net"))

    # Проверка корректности адресов
    if not is_valid_email(sender) or not is_valid_email(recipient):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
        return

    # Проверка на отправку самому себе
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return

    # Проверка на стандартного отправителя
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

# Примеры вызовов функции
send_email("Привет, как дела?", "student@example.com")  # Стандартный отправитель
send_email("Привет, как дела?", "student@example.com", sender="custom.sender@gmail.com")  # Нестандартный отправитель
send_email("Привет, как дела?", "student@example.com", sender="university.help@gmail.com")  # Стандартный отправитель
send_email("Привет, как дела?", "student@example.com", sender="student@example.com")  # Письмо самому себе
send_email("Привет, как дела?", "invalid-email", sender="custom.sender@gmail.com")  # Неверный ema 
