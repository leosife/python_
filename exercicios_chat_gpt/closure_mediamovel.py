def mediamovel(janela):
    lst = []
    def calcular_media(x):
        lst.append(x)
        if len(lst) > janela:
            lst.pop(0)
        return sum(lst) / len(lst)
    return calcular_media


media_movel = mediamovel(3)        

print(media_movel(10))
print(media_movel(20))
print(media_movel(30))
print(media_movel(40))
print(media_movel(50))
print(media_movel(50))
print(media_movel(50))


