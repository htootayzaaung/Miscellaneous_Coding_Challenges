from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.pdfgen import canvas
import datetime

def generate_coupon(c, x, y, width, height, company, coupon_id, date_str):
    # Draw rectangle
    c.setStrokeColor(colors.black)
    c.rect(x, y, width, height)

    # Use default font
    c.setFont("Helvetica-Bold", 16)
    
    # Draw texts on the coupon
    c.drawString(x + 10, y + height - 20, company)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(x + 10, y + (height // 2), f"{coupon_id}")
    c.setFont("Helvetica", 12)
    c.drawString(x + width - 80, y + 10, date_str)

def generate_pdf(start_id, end_id, filename):
    width, height = 175, 100  # Adjusted dimensions for no spacing
    company = "YD Trading"
    date_str = datetime.datetime.now().strftime('%Y-%m-%d')

    c = canvas.Canvas(filename, pagesize=landscape(letter))
    
    x_offset, y_offset = 50, 450  # starting position

    for i in range(start_id, end_id + 1):
        generate_coupon(c, x_offset, y_offset, width, height, company, i, date_str)
        
        x_offset += width
        if (i - start_id + 1) % 4 == 0:  # Move to the next row after 4 coupons
            x_offset = 50
            y_offset -= height
        
        if (i - start_id + 1) % 20 == 0:  # New page after 16 coupons
            c.showPage()
            x_offset, y_offset = 50, 450

    c.save()

if __name__ == "__main__":
    start_id = int(input("Enter the starting ID: "))
    end_id = int(input("Enter the ending ID: "))

    filename = f"coupons_{datetime.datetime.now().strftime('%Y-%m-%d')}.pdf"
    generate_pdf(start_id, end_id, filename)
    
    print(f"Coupons compiled into '{filename}' for printing!")
