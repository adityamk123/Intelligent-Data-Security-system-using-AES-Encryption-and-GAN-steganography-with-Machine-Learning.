from security.aes_crypto import AESCipher
from models.gan_model import generate_image
from steganography.lsb import encode_image, decode_image

if __name__ == "__main__":
    # 1. User input
    message = "Abufrubnunf"
    print("Original message:", message)

    # 2. Encrypt
    cipher = AESCipher()
    encrypted = cipher.encrypt(message)
    print("Encrypted:", encrypted)

    # 3. Generate realistic AI image with Stable Diffusion
    prompt = "A futuristic cyber cityscape, ultra detailed, 4k"
    img = generate_image(prompt)

    # 4. Hide encrypted message
    encode_image(img, encrypted, "encoded.png")
    print("Message hidden inside encoded.png")

    # 5. Decode & Decrypt
    extracted = decode_image("encoded.png", len(encrypted))
    decrypted = cipher.decrypt(extracted)
    print("Decrypted message:", decrypted)
