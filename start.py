from normalizer import Normalizer

counter = 1

count_files = int(input("Количество исходных файлов\n\n>>> "))

for i in range(count_files):
    Normalizer.clearing(counter=i+1)

for i in range(count_files):
    counter = Normalizer.splitting(file_counter=i+1, counter=counter)
