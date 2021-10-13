from captcha.image import ImageCaptcha

image = ImageCaptcha(width=340, height=90)
captcha_text = 'Oh the mighty'
data = image.generate(captcha_text)
image.write(captcha_text, "CAPTCHA.png")