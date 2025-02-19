from returns import invalid_information

while True:
    try:
        download_size = float(input("Tamanho do arquivo (em MB): "))
        break
    except ValueError:
        print(invalid_information())

while True:
    try:
        internet_speed = float(input("Tamanho da banda larga de internet (em Mbps): "))
        break
    except ValueError:
        print(invalid_information())

download_time_seconds = (download_size * 8 ) / internet_speed
download_time = download_time_seconds / 60

print(f"Tempo estimado para donwnload = {download_time:.2f}")