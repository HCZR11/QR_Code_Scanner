# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import qrcode

# qr = qrcode.QRCode(version=1,
#                    error_correction=qrcode.constants.ERROR_CORRECT_L,
#                    box_size=50,
#                    border=1)
#
# qr.add_data("https://github.com/HCZR11")
# qr.make(fit=True)
#
# img = qr.make_image(fill_color="black", back_color="white")
# img.save("git.png")

coffe_menu = """
Meniu Cafea:

1.Espresso - 10 lei 
2.Cappuccino - 12 lei
3. Flath White - 15 lei 
4. Latte - 14 lei 
5. Long black - 8 lei 
6. Cold Brew - 18 lei 

Cafeaua zile Brasil Cerado dolce


"""

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=50,
                   border=1)

qr.add_data(coffe_menu)
qr.make(fit=True)

img = qr.make_image(fill_color=

                    "black", back_color="white")
img.save("coffee_menu_qr.png")
