import random

lenght = int(input('Password lenght, max 74: '))
elements = 'abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'

password = "".join(random.sample(elements, lenght))
print(password)

