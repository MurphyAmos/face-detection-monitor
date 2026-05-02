import mailtrap as mt
import time
api_key = "your_api_key"
def sendAlert(detectedFace = None):
    mail = mt.Mail(
                        sender=mt.Address(email="hello@demomailtrap.co", name="Mailtrap Test"),
                        to=[mt.Address(email="holderEmail@domain.com")],
                        subject="Camera Alert!",
                        text=f"{detectedFace} is at the Front Door at {time.time()}",
                        category=f"Google Nest: Front-Door",
                    )
    mt.Client(api_key="your_api_key").send(mail)
def sendAlertWithImage(detectedFace = None, imagePath = None):
    mail = mt.Mail(
                        sender=mt.Address(email="murphyamos9@gmail.com", name="Mailtrap Test"),
                        to=[mt.Address(email="holderEmail@gmail.com")],
                        subject="Camera Alert!",
                        text=f"{detectedFace} is at the Front Door at {time.time()}",
                        category=f"Google Nest: Front-Door",
                        attachments=[mt.Attachment(
                            filename="intruder.jpg",
                            content=open(imagePath, "rb").read(),
                            content_type="image/jpeg"
                        )]
                    )
    mt.Client(api_key="your_api_key").send(mail)

    