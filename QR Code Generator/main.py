from colors import COLORS,BACKGROUNDS
from generator import generate_qr


print("Professional QR CODE Generator")

data = input("Enter Text or Paste the URL ")

print("QR Colors")
for number, color in COLORS.items():
    print(f"{number} . {color.title()}")


color_choice = int(input("Choose Color . (ENTER THE COLOR NUMBER ONLY )"))

print("Background Color ")
for number,color in BACKGROUNDS.items():
    print(f"{number} . {color.title()}")

background_choice = int(input("Select  the Background Color .(ENTER THE COLOR NUMBER ONLY)"))


filename = input("Enter the File name for QR Code: ")

generate_qr(
    data,
    COLORS[color_choice],
    BACKGROUNDS[background_choice],
    filename,
)

print("QR CODE Generated Successfully ")

print(f"Saved in {filename}.png")
