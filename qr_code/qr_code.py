import qrcode


class CustomQR():
    def __init__(self, size: int = 30, padding: int = 20):
        self.qr = qrcode.QRCode(box_size=size, border=padding)

    def create_qrcode(self, file_name: str, fore: str, back: str):
        user_input: str = input("Enter text")
        try:
            self.qr.add_data(user_input)
            image = self.qr.make_image(fill_color=fore, back_color=back)
            image.save(file_name)
            print(f"File {file_name} saved")
        except Exception as e:
            print(f"Error in QR generation {e}")


if __name__ == '__main__':
    myQR = CustomQR(padding=2)
    myQR.create_qrcode("check.png", "black", "white")
