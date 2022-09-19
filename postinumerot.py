from postikasittely import kasittely

if __name__ == '__main__':

    paikka = input('Kirjoita postitoimipaikka ')
    name = kasittely(paikka)

    if name:
        print('Postinumerot: ' + ', '.join(name) + paikka)

    else:
        print('Tuntematon postitoimipaikka')
