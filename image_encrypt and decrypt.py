from PIL import Image

def encrypt_image(image_path, output_path, key):
    # Open the image
    image = Image.open(image_path)
    pixels = image.load()  # Access pixel data
    
    # Get image dimensions
    width, height = image.size
    
    # Encrypt the image by modifying each pixel
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            # Simple operation: adding the key value (and taking modulus 256 to avoid overflow)
            pixels[x, y] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)
    
    # Save the encrypted image
    image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(image_path, output_path, key):
    # Open the encrypted image
    image = Image.open(image_path)
    pixels = image.load()  # Access pixel data
    
    # Get image dimensions
    width, height = image.size
    
    # Decrypt the image by reverting the operation
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            # Revert the operation by subtracting the key value
            pixels[x, y] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)
    
    # Save the decrypted image
    image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

# Example usage:
image_path = 'D:\Prodigy\Image\image.png'
encrypted_path = 'D:\Prodigy\Image\encrypted_image.png'
decrypted_path = 'D:\Prodigy\Image\decrypted_image.png'
key = 50  # Encryption key (can be any integer)

# Encrypt the image
encrypt_image(image_path, encrypted_path, key)

# Decrypt the image
decrypt_image(encrypted_path, decrypted_path, key)
