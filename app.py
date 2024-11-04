import qrcode

# URL to your GitHub profile (change this if needed)
url = "https://github.com/kito15"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Customize colors and output filename
img = qr.make_image(fill_color="black", back_color="white")
img.save("/app/qr_code.png")  # Save in the Docker container's `/app` directory

print("QR code generated and saved as qr_code.png")
