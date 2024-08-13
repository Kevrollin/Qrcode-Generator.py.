import qrcode
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

def create_centered_qr_code(input_text):
    # Create a QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(input_text)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Create a PDF with centered QR code
    buffer = BytesIO()
    pdf_canvas = canvas.Canvas(buffer, pagesize=letter)
    img_width, img_height = img.size
    pdf_width, pdf_height = letter

    # Calculate center coordinates
    x = (pdf_width - img_width) / 2
    y = (pdf_height - img_height) / 2

    # Draw the QR code on the PDF
    pdf_canvas.drawInlineImage(img, x, y, width=img_width, height=img_height)

    pdf_canvas.save()

    # Reset buffer position to start
    buffer.seek(0)
    
    return buffer

def main():
    # Get user input for QR code text
    user_input = input("Enter the text to encode in the QR code: ")

    # Create centered QR code and save as PDF
    pdf_buffer = create_centered_qr_code(user_input)

    # Save PDF to file
    pdf_filename = "centered_qr_code.pdf"
    with open(pdf_filename, "wb") as pdf_file:
        pdf_file.write(pdf_buffer.read())

    print(f"PDF saved as {pdf_filename}")

if __name__ == "__main__":
    main()
