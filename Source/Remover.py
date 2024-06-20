import csv
import os
import shutil

removed_lines = []
with open('Lines to Remove.txt') as file:
    for line in file:
        line = line.rstrip('\n')
        removed_lines.append(line)

character = ''
with open('Selected Character.txt') as file:
    character = file.readline()


dest_dir = 'Output/zYOURMODNAME_P/Phoenix/Content/WwiseAudio/windows/'
with open('Hogwarts Legacy Audio Files - Voiceover.csv', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if character not in row['Character']:
            continue

        if row['Script Text'] in removed_lines or row['adtl labl'] in removed_lines:
            dest_subdir = dest_dir + row['Directory/Soundbank']
            dest = dest_subdir + '/' + row['WEM File'] + '.wem'
            os.makedirs(dest_subdir, exist_ok=True)
            shutil.copy('00000000.wem', dest)
