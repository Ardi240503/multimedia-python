import pygame

# Inisialisasi Pygame
pygame.init()

try:
    # Inisialisasi mixer
    pygame.mixer.init()
except pygame.error:
    print("Audio tidak tersedia, melanjutkan tanpa suara.")

# Mengatur tampilan
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Game")

# Memuat gambar
image = pygame.image.load('ImageChapter4.jpg')

# Memuat suara jika tersedia
sound = None
if pygame.mixer.get_init():
    sound = pygame.mixer.Sound('Audio.mp3')
    sound.play()

# Variabel untuk animasi
x = 0

# Pengaturan FPS
clock = pygame.time.Clock()

# Loop utama permainan
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Memperbarui posisi gambar
    x += 5
    if x > 800:
        x = 0

    # Menghapus layar sebelum menggambar ulang
    screen.fill((0, 0, 0))

    # Menggambar gambar di posisi baru
    screen.blit(image, (x, 100))

    # Memperbarui tampilan
    pygame.display.flip()

    # Menjaga kecepatan animasi tetap konsisten
    clock.tick(60)

# Keluar dari Pygame
pygame.quit()
