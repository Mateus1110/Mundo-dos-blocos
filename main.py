from Mundo_blocos.processamento import MundoBlocos


def main():
    esq, cent, dir = [], [], []
    MundoBlocos.cria_blocos(cent)

    MundoBlocos.ordena(esq, cent, dir)
    MundoBlocos.print_blocos(cent, esq, dir, 1)


if __name__ == '__main__':
    main()
