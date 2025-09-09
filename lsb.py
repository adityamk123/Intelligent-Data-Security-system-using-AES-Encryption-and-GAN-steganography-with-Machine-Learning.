from PIL import Image
import numpy as np

def encode_image(image: Image.Image, secret_data: bytes, output_path="encoded.png"):
    data_bits = ''.join(format(byte, '08b') for byte in secret_data)
    img = np.array(image).astype(np.uint8)   # ✅ ensure uint8
    h, w, _ = img.shape

    idx = 0
    for row in range(h):
        for col in range(w):
            for channel in range(3):  # RGB
                if idx < len(data_bits):
                    pixel_val = int(img[row][col][channel])  # force int
                    bit = int(data_bits[idx])
                    # Clear LSB then set new bit safely
                    pixel_val = (pixel_val & 0b11111110) | bit
                    img[row][col][channel] = np.uint8(pixel_val)
                    idx += 1

    encoded_img = Image.fromarray(img)
    encoded_img.save(output_path)


def decode_image(image_path: str, length: int) -> bytes:
    img = np.array(Image.open(image_path)).astype(np.uint8)
    bits = ""
    for row in img:
        for pixel in row:
            for channel in pixel:
                bits += str(int(channel) & 1)
                if len(bits) >= length * 8:
                    return bytes(int(bits[i:i+8], 2) for i in range(0, len(bits), 8))
