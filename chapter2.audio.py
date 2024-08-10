from pydub import AudioSegment

# Memuat file audio
audio = AudioSegment.from_file('Audio.mp3')

# Memotong 10 detik pertama dari audio
clipped_audio = audio[:10000]

# Menggabungkan audio asli dengan hasil potongan
combined_audio = audio + clipped_audio

# Menyimpan hasil penggabungan dalam format WAV
combined_audio.export('combined_result.wav', format='wav')

# Meningkatkan volume audio hasil penggabungan sebesar 10dB
louder_audio = combined_audio + 10

# Menyimpan hasil akhir dengan volume yang telah diatur dalam format MP3
louder_audio.export('final_result.mp3', format='mp3')
