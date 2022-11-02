import animeworld as aw

anime = aw.Anime(link="https://www.animeworld.tv/play/yama-no-susume-4.ZwJbq/pHS-XC")
episodenumber = "0000"

for episodio in anime.getEpisodes():
    print("Episodio Numero: ", episodio.number)
    if int(episodio.number) < 10:
        episodenumber = "000"
    if int(episodio.number) >= 10 and episodio.number < 100:
        episodenumber = "00"
    if int(episodio.number) >= 100 and episodio.number < 1000:
        episodenumber = "0"
    if int(episodio.number) >= 1000:
        episodenumber = ""
    
    if (episodio.download(title="Yama no Susume 4_Ep_"+episodenumber+str(episodio.number)+"_SUB_ITA")):
        print("scaricato")
    else:
        print("errore")
