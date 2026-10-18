from PIL import Image, ImageFilter

filename = input("Enter image filename: ")

try:
    img = Image.open(filename)

    print("Image opened successfully.")
    print("Size:", img.size)

    # Grayscale
    gray = img.convert("L")
    gray.save("grayscale.png")

    # Black and white threshold
    bw = gray.point(lambda x: 255 if x > 128 else 0)
    bw.save("black_white.png")

    # Blur
    blur = img.filter(ImageFilter.BLUR)
    blur.save("blurred.png")

    print("Processed images saved successfully.")

except FileNotFoundError:
    print("Image file not found.")

except Exception as e:
    print("Error:", e)