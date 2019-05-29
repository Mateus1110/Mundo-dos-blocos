from random import shuffle


class MundoBlocos(object):
    num_blocos = 0

    @staticmethod
    def cria_blocos(cent):
        MundoBlocos.num_blocos = int(input('entre com o numero de blocos...'))
        id = 0
        for i in range(MundoBlocos.num_blocos):
            id += 1
            cent.append(i)
        shuffle(cent)

    @staticmethod
    def print_blocos(cent, esq, dir, flag=0):
        if flag == 0:
            print('esq: {}'.format(esq))
            print('cent: {}'.format(cent))
            print('dir: {}'.format(dir))
            print('\n')
        else:
            print('\033[33m esq: {}\033[m'.format(esq))
            print('\033[33m cent: {}\033[m'.format(cent))
            print('\033[33m dir: {}\033[m'.format(dir))

    @staticmethod
    def verifica_ordem(lista):
        if all(lista[i] > lista[i + 1] for i in range(len(lista) - 1)):
            return True
        else:
            return False

    @staticmethod
    def meio_para_direita(cent, dir):
        dir.append(cent.pop())

    @staticmethod
    def meio_para_esquerda(cent, esq):
        esq.append(cent.pop())

    @staticmethod
    def direita_para_meio(cent, dir):
        cent.append(dir.pop())

    @staticmethod
    def direita_para_esquerda(esq, dir):
        esq.append(dir.pop())

    @staticmethod
    def ordena(esq, cent, dir):
        if MundoBlocos.verifica_ordem(cent) is True:
            pass
        else:
            e = MundoBlocos.num_blocos - 1
            while True:
                MundoBlocos.print_blocos(cent, esq, dir)
                if e in cent:
                    ind_next = cent.index(e)
                    for i in range(len(cent) - 1 - ind_next):
                        MundoBlocos.meio_para_direita(cent, dir)
                    MundoBlocos.meio_para_esquerda(cent, esq)
                else:
                    ind_next = dir.index(e)
                    for i in range(len(dir) - 1 - ind_next):
                        MundoBlocos.direita_para_meio(cent, dir)
                    MundoBlocos.direita_para_esquerda(esq, dir)
                e -= 1
                if e < 0:
                    break
                input()
