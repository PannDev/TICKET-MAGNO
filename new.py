import os
import random
import qrcode
from PIL import Image, ImageDraw, ImageFont
import string

# Set konfigurasi di sini agar mudah diubah
template_folder = "/Users/Evan/Desktop/ticket/assets/"  # DESIGN
qrcode_folder = "/Users/Evan/Desktop/ticket/qrcode/"  # QR CODE
output_folder = "/Users/Evan/Desktop/ticket/output/"  # OUTPUT
nama_file_path = "/Users/Evan/Desktop/ticket/nama/nama.txt"  # DATA NAMA
font_regular_path = "/Users/Evan/Desktop/ticket/font/Poppins Regular 400.ttf"  # FONT Regular
font_bold_path = "/Users/Evan/Desktop/ticket/font/Poppins Bold 700.ttf"  # FONT Bold

# Konfigurasi
import os
import random
import string
from PIL import Image, ImageDraw, ImageFont
import qrcode

# Konfigurasi folder
qrcode_folder = "qrcodes"
template_folder = "templates"
output_folder = "output"
nama_file_path = "names.txt"

# Konfigurasi font
font_bold_path = "path_to_bold_font.ttf"
font_regular_path = "path_to_regular_font.ttf"

# Konfigurasi pengaturan
show_names = False  # Tampilkan nama? True|False
use_random_code = False  # Kode acak? True|False
lower_bound = 1  # Index awal
upper_bound = 10  # Index akhir (default 10)

use_wordlist = False  # Gunakan wordlist dari nama_file_path? True|False
use_random_word = True  # Gunakan random word? True|False

# Konfigurasi font dan tampilan
font_config = {
    "nama": {
        "size": 40,
        "color": "black",
        "bold": True,
        "display_font": True  # Mau ditampilin? True|False
    },
    "code": {
        "size": 45,
        "color": "black",
        "bold": False,
        "display_font": True  # Mau ditampilin? True|False
    }
}

# Koordinat
coords = {
    "qr": (155, 250),
    "code": (260, 25),
    "nama": (150, 20)
}

# Cek jika menggunakan kedua opsi (nama file dan random word) secara bersamaan
if use_wordlist and use_random_word:
    raise ValueError("Error: Jangan aktifkan kedua opsi (use_wordlist dan use_random_word) secara bersamaan!")

# Fungsi untuk menghasilkan random word
def generate_random_word(min_length=3, max_length=7):
    length = random.randint(min_length, max_length)
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

# Fungsi untuk menambah elemen pada template
def add_elements_to_template(template_path, qrcode_path, output_path, nama_text, code_text):
    print(f"Loading template from: {template_path}")  # Debug print
    template = Image.open(template_path).convert("RGBA")
    qrcode_img = Image.open(qrcode_path).convert("RGBA")
    
    # Menempelkan QR CODE
    print(f"Paste QR code at {coords['qr']}")  # Debug print koordinat QR
    template.paste(qrcode_img, coords["qr"], qrcode_img.convert("RGBA").getchannel("A"))
    
    draw = ImageDraw.Draw(template)

    # Menambahkan teks Nama jika show_names aktif
    if show_names and font_config["nama"]["display_font"]:
        nama_font_path = font_bold_path if font_config["nama"]["bold"] else font_regular_path
        try:
            nama_font = ImageFont.truetype(nama_font_path, font_config["nama"]["size"])
            draw.text(coords["nama"], nama_text, font=nama_font, fill=font_config["nama"]["color"])
            print(f"Added name text: {nama_text}")  # Debug print nama
        except IOError:
            raise ValueError(f"Font untuk nama tidak ditemukan: {nama_font_path}")

    # Menambahkan teks Code
    if font_config["code"]["display_font"]:
        code_font_path = font_bold_path if font_config["code"]["bold"] else font_regular_path
        try:
            code_font = ImageFont.truetype(code_font_path, font_config["code"]["size"])
            draw.text(coords["code"], code_text, font=code_font, fill=font_config["code"]["color"])
            print(f"Added code text: {code_text}")  # Debug print code
        except IOError:
            raise ValueError(f"Font untuk kode tidak ditemukan: {code_font_path}")

    print(f"Saving output to: {output_path}")  # Debug print
    template.save(output_path, "PNG")

# Baca nama dari file
def read_names_from_file(path, lower_bound, upper_bound):
    if not os.path.exists(path) or os.stat(path).st_size == 0:
        raise ValueError(f"File nama tidak ditemukan atau kosong: {path}")
    
    with open(path, "r") as file:
        names = file.readlines()
    print(f"Read names: {names}")  # Debug print
    return [name.strip() for name in names[lower_bound-1:upper_bound]]

# Fungsi kode acak
def generate_random_code():
    return str(random.randint(10000, 99999))

# Fungsi kode urut
def generate_sequential_code(i):
    return f"{i:05d}"

# Fungsi untuk membuat QR code dengan warna acak
def create_random_color_qrcode(text, width=200, height=200):
    # Generate random foreground (QR color) dan background color
    fg_color = tuple(random.randint(0, 255) for _ in range(3))  # RGB color for foreground
    bg_color = tuple(random.randint(0, 255) for _ in range(3))  # RGB color for background
    
    # Pastikan foreground dan background tidak sama
    while fg_color == bg_color:
        fg_color = tuple(random.randint(0, 255) for _ in range(3))
        bg_color = tuple(random.randint(0, 255) for _ in range(3))
    
    print(f"Foreground color: {fg_color}, Background color: {bg_color}")  # Debug print

    # Generate the QR code
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(text)
    qr.make(fit=True)
    
    # Create an image from the QR Code and color it
    img = qr.make_image(fill=fg_color, back_color=bg_color).convert("RGBA")
    
    # Resize image to desired size
    img = img.resize((width, height), Image.Resampling.LANCZOS)
    
    return img

# Ambil file QR Code dari folder
qrcode_files = [f for f in sorted(os.listdir(qrcode_folder)) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))][lower_bound-1:upper_bound]

# Jika folder QR code kosong, buat QR Code random
if not qrcode_files:
    print("Folder QR Code kosong, membuat QR Code dengan warna acak...")  # Debug print
    qrcode_files = [f"{i}.png" for i in range(lower_bound, upper_bound + 1)]
    for i, qr_file in enumerate(qrcode_files):
        print(f"Creating QR code {qr_file}...")  # Debug print
        random_qr = create_random_color_qrcode(f"QR {i+1}")
        random_qr.save(os.path.join(qrcode_folder, qr_file))

# Loop pemrosesan QR code
if use_wordlist:
    if not os.path.exists(nama_file_path) or os.stat(nama_file_path).st_size == 0:
        raise ValueError(f"Error: File wordlist nama tidak ditemukan atau kosong: {nama_file_path}")
    names = read_names_from_file(nama_file_path, lower_bound, upper_bound)
elif use_random_word:
    names = [generate_random_word() for _ in range(upper_bound - lower_bound + 1)]
else:
    names = []

# Pastikan jumlah QR Code dan nama sesuai
if len(qrcode_files) != len(names):
    raise ValueError("Error: Jumlah file QR Code dan nama tidak sesuai!")

# Ambil template dan QR Code
template_files = [f for f in sorted(os.listdir(template_folder)) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))][0:1]  # Ambil 1 template

for i, qrcode_file in enumerate(qrcode_files):
    template_path = os.path.join(template_folder, template_files[0])
    qrcode_path = os.path.join(qrcode_folder, qrcode_file)
    nama_text = names[i] if show_names else ""
    
    # Pilih kode sesuai pengaturan
    code_text = generate_random_code() if use_random_code else generate_sequential_code(i + 1)
    
    output_filename = f"{i+1}.png"  # Nama output sesuai dengan urutan angka (1.png, 2.png, dst)
    output_path = os.path.join(output_folder, output_filename)

    if os.path.exists(output_path):
        os.remove(output_path)
    
    add_elements_to_template(template_path, qrcode_path, output_path, nama_text, code_text)
    print(f"Informatics Club 81: {output_path}")  # Debug print
