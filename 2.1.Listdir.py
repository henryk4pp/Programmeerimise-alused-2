from os import listdir


# a = os.listdir(".")
# b = os.listdir("C:\\Users\Ester\Desktop")


failinimed = listdir("C:\\Users\\Aivar\\Music")

mp3_leidub = False # alustame pessimistlikult
for failinimi in failinimed:
    if failinimi.endswith(".mp3"):
        mp3_leidub = True

        # kui meile piisab ühe faili leidumisest,
        # siis rohkem pole vaja edasi vaadata
        break
