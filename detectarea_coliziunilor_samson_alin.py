from math import pi, sqrt

class FormaGeometrica(object):
    """
    Aceasta clasa reprezinta o forma geometrica. Este conceputa pentru a fi valabila pentru orice
    tip de forme geometrice. In cadrul acestui proiect aceasta clasa parinte (FormaGeormetrica)
    va fi folosita doar pentru urmatoarele forme geometrice: Cerc, Patrat, Dreptunghi si Triunghi.
    Args:
        x (type - integer/float) : reprezinta coordonata pe axa X a centrului formei geometrice
        y (type - integer/float) : reprezinta coordonata pe axa Y a centrului formei geometrice
    Methods:
        __init__()          : este o metoda constructor in care sunt definite coordonatele x si y;
        cerc_incadrare      : reprezinta o metoda abstracta ce va genera automat o exceptie;
        arie_cerc_incadrare : reprezinta o metoda abstracta ce va genera automat o exceptie;
        distanta_puncte     : reprezinta o metoda ce calculeaza si returneaza distanta dintre
                                  centrele a doua figuri geometrice;
    """
    def __init__(self, id, x, y):
        """
        Metoda constructor necesara pentru definirea atributelor x si y care primeste pozitia
        centrului unei figuri geometrice.
        Args:
            x (type - integer/float) : reprezinta coordonata pe axa X a centrului formei geometrice
            y (type - integer/float) : reprezinta coordonata pe axa Y a centrului formei geometrice
        """
        self.id = id
        self.x = x
        self.y = y

    def cerc_incadrare(self):
        """
        Metoda abstracta ce va genera automat o exceptie in cazul in care nu este suprascrisa de
        clasele ce o mostenesc.
        Cu ajutorul "NotImplementedError" semnalam ca o metoda nu este complet implementata.
        """
        raise NotImplementedError('Nu se poate calcula raza de incadrare pentru aceasta'
                                  'forma geometrica.')
    def arie_cerc_incadrare(self):
        """
        Metoda abstracta ce va genera automat o exceptie in cazul in care nu este suprascrisa de
        clasele ce o mostenesc.
        Cu ajutorul "NotImplementedError" semnalam ca o metoda nu este complet implementata.
        """
        raise NotImplementedError('Calculul arie nu se poate efectu pentru forma geometrica.')

    def distanta_puncte(self, alt_punct):
        """
        Metoda destanta_puncte are urmatoarele doua scopuri: calculeaza si returneaza distanta
        dintre centrele a doua figuri geometrice.
        Args:
            alt_punct (class) : primeste o instanta a unei clase in care sunt generate doua
                                valori pentru x si y reprezentand centrul unei alte figuri geometrice.
        Return:
            distanta (float)  : o valoare de tip real (float) care reprezinta distanta dintre
                                centrele a doua figuri geometrice.
        """
        distanta = sqrt((self.x - alt_punct.x)**2 +(self.y - alt_punct.y)**2)
        return distanta

class Cerc(FormaGeometrica):
    """
    Clasa Cerc este o clasa copil (clasa derivata) a clasei parinte (clasa de baza) FormaGeometrica.
    Aceasta clasa mosteneste toate atributele si metodele clasei parinte si suplimentar primeste
    atribute si metode proprii.
    Tip mostenire - Mostenire Simpla (mosteneste dintr-o singura clasa).
    Args:
        raza (float) : reprezinta valoarea razei cercului ce va fi creat
    Methods:
        __init__() : este o metoda constructor in care este definita raza cercului, dar si in care
                     sunt mostenite coordonatele centrului cercului;
        arie_cerc_incadrare() : returneaza valoarea arei pentru cercul a carui raza si coordonate
                                au fost definite;
        detectie_coliziune() : afiseaza un raspuns privind coliziunea sau nu a figurilor geometrice;
        semiincluziune() : afiseaza un raspuns clar cu privire la semi-incluziunea dintre doua
                           figuri geometrice;
    """
    def __init__(self, id, x, y, raza):
        """
        Metoda constructor necesara pentru definirea atributelor x si y, mostenite din clasa parinte
        FormaGeometrica, dar si a atributului propriu raza.
        Args:
            raza (float) : reprezinta valoarea razei cercului ce va fi creat
        """
        super().__init__(id, x, y)
        self.raza = raza

    def cerc_incadrare(self):
        """
        Metoda ce returneaza raza cercului definita in metoda constructor.
        Return:
             raza (float) : valoare de tip real pentru aria cercului
        """
        return self.raza

    def arie_cerc_incadrare(self):
        """
        Metoda ce calculeaza si returneaza valoarea ariei pentru raza definita in metoda constructor.
        Return:
            valoare (float) : rezultatul de tip real pentru aria cercului.
        """
        return pi*(self.raza**2)

    def detectie_coliziune(self, distanta, raza_figura2):
        """
        Metoda ce afiseaza un raspuns clar privind coliziunea sau nu a doua figuri geometrice.
        Args:
            distanta (float) : reprezinta distanta dintre centrele a 2 figuri geometrice pentru
                               care se verifica coliziunea.
            raza_figura2 (float) : reprezinta raza figurii cu care se verifica coliziunea.
        """
        if distanta <= (self.raza + raza_figura2):
            return True

    def semiincluziune(self, distanta, raza_figura2):
        """
        Metoda ce afiseaza un raspuns clar privind semi-incluziunea dintre doua figuri geometrice.
        Args:
            distanta (float) : reprezinta distanta dintre centrele a 2 figuri geometrice pentru
                               care se verifica semi-incluziunea.
            raza_figura2 (float) : reprezinta raza figurii cu care se verifica coliziunea.
        """
        if (distanta <= self.raza + raza_figura2) and (self.raza >= raza_figura2):
            return True

class Patrat(FormaGeometrica):
    """
    Clasa Patrat este o clasa copil (clasa derivata) a clasei parinte (clasa de baza) FormaGeometrica.
    Aceasta clasa mosteneste toate atributele si metodele clasei parinte si suplimentar primeste
    atribute si metode proprii.
    Tip mostenire - Mostenire Simpla (mosteneste dintr-o singura clasa).
    Args:
        latura (float) : reprezinta valoarea laturii patratului ce va fi creat
    Methods:
        __init__() : este o metoda constructor in care este definita latura patratului, dar si
                     in care sunt mostenite coordonatele centrului patratului;
        arie_figura() : returneaza valoarea arei pentru patratul a carui latura si coordonate au
                        fost definite;
        cerc_incadrare() : calculeaza si returneaza valoarea razei cercului in care va fi incadrat
                           patratul de latura definita;
        detectie_coliziune() : afiseaza un raspuns privind coliziunea sau nu a figurilor geometrice;
        semiincluziune() : afiseaza un raspuns clar cu privire la semi-incluziunea dintre doua
                           figuri geometrice;
    """
    def __init__(self, id, x, y, latura):
        """
        Metoda constructor necesara pentru definirea atributelor x si y, mostenite din clasa parinte
        FormaGeometrica, dar si a atributului propriu latura patratului.
        Args:
            latura (float) : reprezinta valoarea laturii patratului ce va fi creat
        """
        super().__init__(id, x, y)
        self.latura = latura

    def arie_figura(self):
        """
        Metoda ce calculeaza si returneaza aria patratului pentru latura definita.
        Return:
            valoare (float) : valoarea de tip real a arie patratului
        """
        return (self.latura**2)

    def cerc_incadrare(self):
        """
        Metoda ce calculeaza si returneaza valoarea razei pentru cercul in care va fi incadrat patratul.
        Return: raza_incadrare (float) : valoarea reala a razei pentru cercul de incadrare
        """
        raza_incadrare = self.latura / 2
        return raza_incadrare

    def arie_cerc_incadrare(self, raza_incadrare):
        """
        Metoda ce calculeaza si returneaza valoarea ariei cercului in care va fi incadrat patratul.
        Args:
            raza_incadrare (float) : reprezinta valoarea razei cercului de incadrare.
        Return:
            arie_cerc_incadrare (float) : valoarea ariei cercului incadrator.
        """
        arie_cerc_incadrare = pi * (raza_incadrare ** 2)
        return arie_cerc_incadrare

    def detectie_coliziune(self, distanta, raza_figura2):
        """
        Metoda ce afiseaza un raspuns clar privind coliziunea sau nu a doua figuri geometrice.
        Args:
            distanta (float) : reprezinta distanta dintre centrele a 2 figuri geometrice pentru
                               care se verifica coliziunea.
            raza_figura2 (float) : reprezinta raza figurii cu care se verifica coliziunea.
        """
        if distanta <= (Patrat.cerc_incadrare(self) + raza_figura2):
            return True

    def semiincluziune(self, distanta, raza_figura2):
        """
        Metoda ce afiseaza un raspuns clar privind semi-incluziunea dintre doua figuri geometrice.
        Args:
            distanta (float) : reprezinta distanta dintre centrele a 2 figuri geometrice pentru
                                       care se verifica semi-incluziunea.
            raza_figura2 (float) : reprezinta raza figurii cu care se verifica coliziunea.
        """
        if (distanta <= (Patrat.cerc_incadrare(self) + raza_figura2)) and \
                (Patrat.cerc_incadrare(self) >= raza_figura2):
            return True


class Dreptunghi(FormaGeometrica):
    """
    Clasa Dreptunghi este o clasa copil a clasei parinte (clasa de baza) FormaGeometrica.
    Aceasta clasa mosteneste toate atributele si metodele clasei parinte si suplimentar primeste
    atribute si metode proprii.
    Tip mostenire - Mostenire Simpla (mosteneste dintr-o singura clasa).
    Args:
        lungime (float) : reprezinta valoarea lungimii dreptunghiului ce va fi creat
        latime (float)  : reprezinta valoarea latimii dreptunghiului ce va fi creat
    Methods:
        __init__() : este o metoda constructor in care sunt definite lungimea si latimea dreptunghiului,
                     dar si in care sunt mostenite coordonatele centrului dreptunghiului;
        arie_figura() : returneaza valoarea arei pentru dreptunghiul a carui lungime, latime
                        si coordonate au fost definite;
        cerc_incadrare() : calculeaza si returneaza valoarea razei cercului in care va fi incadrat
                           dreptunghiul creat;
        detectie_coliziune() : afiseaza un raspuns privind coliziunea sau nu a figurilor geometrice;
        semiincluziune() : afiseaza un raspuns clar cu privire la semi-incluziunea dintre doua
                           figuri geometrice;
    """
    def __init__(self, id, x, y, lungime, latime):
        """
        Metoda constructor necesara pentru definirea atributelor x si y, mostenite din clasa parinte
        FormaGeometrica, dar si a atributelor proprii lungime si latime dreptunghi.
        Args:
            lungime (float) : reprezinta valoarea lungimii dreptunghiului ce va fi creat
            latime (float)  : reprezinta valoarea latimii dreptunghiului ce va fi crea
        """
        super().__init__(id, x, y)
        self.lungime = lungime
        self.latime = latime

    def arie_figura(self):
        """
        Metoda ce calculeaza si returneaza aria dreptunghiului avand lungimea si latimea definite.
        Return:
            valoare (float) : valoarea de tip real a arie dreptunghiului
        """
        return (self.lungime * self.latime)

    def cerc_incadrare(self):
        """
        Metoda ce calculeaza si returneaza valoarea razei pentru cercul in care va fi incadrat
        dreptunghiul.
        Return:
            raza_incadrare (float) : valoarea reala a razei pentru cercul de incadrare
        """
        raza_incadrare = (max(self.lungime, self.latime)) / 2
        return raza_incadrare

    def arie_cerc_incadrare(self, raza_incadrare):
        """
        Metoda ce calculeaza si returneaza valoarea ariei cercului in care va fi incadrat
        dreptunghiul.
        Args:
            raza_incadrare (float) : reprezinta valoarea razei cercului de incadrare.
        Return:
            arie_cerc_incadrare (float) : valoarea ariei cercului incadrator.
        """
        arie_cerc_incadrare = pi * (raza_incadrare ** 2)
        return arie_cerc_incadrare

    def detectie_coliziune(self, distanta, raza_figura2):
        """
        Metoda ce afiseaza un raspuns clar privind coliziunea sau nu a doua figuri geometrice.
        Args:
            distanta (float) : reprezinta distanta dintre centrele a 2 figuri geometrice pentru
                               care se verifica coliziunea.
            raza_figura2 (float) : reprezinta raza figurii cu care se verifica coliziunea.
        """
        if distanta <= (Dreptunghi.cerc_incadrare(self) + raza_figura2):
            return True

    def semiincluziune(self, distanta, raza_figura2):
        """
        Metoda ce afiseaza un raspuns clar privind semi-incluziunea dintre doua figuri geometrice.
        Args:
            distanta (float) : reprezinta distanta dintre centrele a 2 figuri geometrice pentru
                               care se verifica semi-incluziunea.
            raza_figura2 (float) : reprezinta raza figurii cu care se verifica coliziunea.
        """
        if (distanta <= (Dreptunghi.cerc_incadrare(self) + raza_figura2)) and \
                (Dreptunghi.cerc_incadrare(self) >= raza_figura2):
            return True

class Triunghi(FormaGeometrica):
    """
    Clasa Triunghi este o clasa copil a clasei parinte (clasa de baza) FormaGeometrica.
    Aceasta clasa mosteneste toate atributele si metodele clasei parinte si suplimentar primeste
    atribute si metode proprii.
    Tip mostenire - Mostenire Simpla (mosteneste dintr-o singura clasa).
    Args:
        latura1 (float) : reprezinta valoarea unei laturi a triunghiului ce va fi creat
        latura2 (float) : reprezinta valoarea unei laturi a triunghiului ce va fi creat
        latura3 (float) : reprezinta valoarea unei laturi a triunghiului ce va fi creat
    Methods:
        __init__() : este o metoda constructor in care sunt definite laturile triunghiului,
                     dar si in care sunt mostenite coordonatele centrului triunghiului;
        arie_figura() : returneaza valoarea arei triunghiului a carui laturi si coordonate
                        au fost definite;
        cerc_incadrare() : calculeaza si returneaza valoarea razei cercului in care va fi incadrat
                           triunghiul creat;
        detectie_coliziune() : afiseaza un raspuns privind coliziunea sau nu a figurilor geometrice;
        semiincluziune() : afiseaza un raspuns clar cu privire la semi-incluziunea dintre doua
                           figuri geometrice;
    """
    def __init__(self, id, x, y, latura1, latura2, latura3):
        """
        Metoda constructor necesara pentru definirea atributelor x si y, mostenite din clasa parinte
        FormaGeometrica, dar si a atributelor proprii lungime si latime dreptunghi.
        Args:
            latura1 (float) : reprezinta valoarea unei laturi a triunghiului ce va fi creat
            latura2 (float) : reprezinta valoarea unei laturi a triunghiului ce va fi creat
            latura3 (float) : reprezinta valoarea unei laturi a triunghiului ce va fi creat
        """
        super().__init__(id, x, y)
        self.latura1 = latura1
        self.latura2 = latura2
        self.latura3 = latura3

    def arie_figura(self):
        """
        Metoda ce calculeaza si returneaza aria triunghiului avand laturile definite.
        Return:
            arie_triunghi (float) : valoarea de tip real a arie triunghiului
        """
        semiperimetru = (self.latura1 + self.latura2 + self.latura3) / 2
        arie_triunghi = sqrt(semiperimetru*(semiperimetru-self.latura1)*
                             (semiperimetru-self.latura2)*(semiperimetru-self.latura3))
        return arie_triunghi

    def cerc_incadrare(self):
        """
        Metoda ce calculeaza si returneaza valoarea razei pentru cercul in care va fi incadrat
        triunghiul.
        Return:
            raza_incadrare (float) : valoarea reala a razei pentru cercul de incadrare
        """
        raza_incadrare = (max(self.latura1, self.latura2, self.latura3)) / 2
        return raza_incadrare

    def arie_cerc_incadrare(self, raza_incadrare):
        """
        Metoda ce calculeaza si returneaza valoarea ariei cercului in care va fi incadrat
        triunghiul.
        Args:
            raza_incadrare (float) : reprezinta valoarea razei cercului de incadrare.
        Return:
            arie_cerc_incadrare (float) : valoarea ariei cercului incadrator.
        """
        arie_cerc_incadrare = pi * (raza_incadrare ** 2)
        return arie_cerc_incadrare

    def detectie_coliziune(self, distanta, raza_figura2):
        """
        Metoda ce afiseaza un raspuns clar privind coliziunea sau nu a doua figuri geometrice.
        Args:
            distanta (float) : reprezinta distanta dintre centrele a 2 figuri geometrice pentru
                               care se verifica coliziunea.
            raza_figura2 (float) : reprezinta raza figurii cu care se verifica coliziunea.
        """
        if distanta <= (Triunghi.cerc_incadrare(self) + raza_figura2):
            return True

    def semiincluziune(self, distanta, raza_figura2):
        """
        Metoda ce afiseaza un raspuns clar privind semi-incluziunea dintre doua figuri geometrice.
        Args:
            distanta (float) : reprezinta distanta dintre centrele a 2 figuri geometrice pentru
                               care se verifica semi-incluziunea.
            raza_figura2 (float) : reprezinta raza figurii cu care se verifica coliziunea.
        """
        if (distanta <= (Triunghi.cerc_incadrare(self) + raza_figura2)) and \
                (Triunghi.cerc_incadrare(self) >= raza_figura2):
            return True


class Cadran(object):
    """
    Clasa Cadran este conceputa pentru a determina spatiul de lucru in care se vor incadra figurile
    geometrice. Spatiul de lucru va fi impartit in patru cadrane.
    La initializare, pentru spatiul de lucru, vor fi date doar coordonatele punctului din stanga-jos
    si din dreapta-sus.
    Impartirea in cadrane se va face in urmatoarea ordine:
        Cadran I   - dreapta sus
        Cadran II  - stanga sus
        Cadran III - stanga jos
        Cadran IV  - dreapta jos
    Args:
        x1 (type - int) : reprezinta coordonata pe axa X a punctului din stanga-jos
        y1 (type - int) : reprezinta coordonata pe axa Y a punctului din stanga-jos
        x2 (type - int) : reprezinta coordonata pe axa X a punctului din dreapta-sus
        y2 (type - int) : reprezinta coordonata pe axa Y a punctului din dreapta-sus
    Methods:
        __init__() : este o metoda constructor in care sunt definite coordonatele punctelor
                    dreapta-sus si stanga-jos;
        suprafata_cadran()   : reprezinta o metoda ce va determina aria suprafetei de lucru;
        determinare_cadran() : reprezinta o metoda ce va determina cadranul in care se afla
                               o figura geometrica;
    """
    def __init__(self, x1, y1, x2, y2, cadran1 = None, cadran2 = None, cadran3 = None, cadran4 = None):
        """
        Metoda constructor necesara pentru definirea atributelor x1, y1 si x2, y2 care primeste
        pozitia punctelor de incadrare a spatiului de lucru.
        Args:
            x1 (type - int) : reprezinta coordonata pe axa X a punctului din stanga-jos
            y1 (type - int) : reprezinta coordonata pe axa Y a punctului din stanga-jos
            x2 (type - int) : reprezinta coordonata pe axa X a punctului din dreapta-sus
            y2 (type - int) : reprezinta coordonata pe axa Y a punctului din dreapta-sus
            cadran1, cadran2, cadran3, cadran4 - atribute instanta care primest default "None"
            figuri_exceptionale (list) : lista ce va contine figurile care nu se vor incadra in
                                         spatiul de lucru definit.
        """
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.cadran1 = cadran1
        self.cadran2 = cadran2
        self.cadran3 = cadran3
        self.cadran4 = cadran4
        self.figuri_exceptionale = list()

    def suprafata_cadran(self):
        """
        Metoda ce calculeaza si returneaza aria spatiului de lucru pentru punctele definite.
        Return:
            arie_cadran (float) : valoarea de tip real a arie spatiului de lucru
        """
        arie_cadran = (self.x2 - self.x1) * (self.y2 - self.y1)
        return arie_cadran

    def determinare_cadran(self, centru_figura):
        """
        Metoda ce determina si returneaza cadranul in care este incadrat o figura geometrica.
        Args:
            centru (class) : reprezinta coordonatele figurii pentru care va fi returnata pozitia
                            in spatiul de lucru (incadrarea in cadran)
        Return:
            cadran (int) : o valoare de tip intreg care va reprezenta numarul cadranului in care
                         se gaseste figura geometrica
        """
        xc = (self.x2 + self.x1) / 2
        yc = (self.y2 + self.y1) / 2
        if (centru_figura.x > xc) and (centru_figura.x < self.x2) \
                and (centru_figura.y > yc) and (centru_figura.y < self.y2):
            self.cadran1 = 1
            return self.cadran1
        elif (centru_figura.x > self.x1 and centru_figura.x < xc) \
                and (centru_figura.y > yc and centru_figura.y < self.y2):
            self.cadran2 = 2
            return self.cadran2
        elif (centru_figura.x > self.x1 and centru_figura.x < xc) \
                and (centru_figura.y > self.y1 and centru_figura.y < yc):
            self.cadran3 = 3
            return self.cadran3
        elif (centru_figura.x > xc and centru_figura.x < self.x2) \
                and (centru_figura.y > self.y1 and centru_figura.y < yc):
            self.cadran4 = 4
            return self.cadran4
        else:
            print('Figura geometrica nu apartine spatiului de lucru definit.')
            self.figuri_exceptionale.append(centru_figura)
            print(f'Figuri exceptionale - ce nu apartin cadranului: {self.figuri_exceptionale}')


def program_principal(fisier_input, fisier_output):
    #fisier_input = r'C:\Users\alin9\PycharmProjects\PythonAlin\checker\input\test9'
    lista_continut = list()
    with open(fisier_input, mode='rt', encoding='UTF-8') as file1:
        continut = file1.readlines()
    for index in continut:
        index = index.rstrip('\n')
        lista_continut.append(index)
    coordonate = lista_continut[0]
    coordonate = coordonate.split(' ')
    print(f'Coordonatele cadranului sunt: {coordonate}')
    x1 = int(coordonate[0])
    y1 = int(coordonate[1])
    x2 = int(coordonate[2])
    y2 = int(coordonate[3])
    cadran = Cadran(x1, y1, x2, y2)
    print('S-a initializat spatiul de lucru.')
    print(('-') * 70)
    lista_doc = []
    for parcurgere_index in range(1, len(lista_continut)):
        # print(f'Linia {parcurgere_index+1} are continutul:{lista_continut[parcurgere_index]}')
        variabila = lista_continut[parcurgere_index]
        variabila = variabila.split(' ')
        lista_doc.append(variabila)
    #print(f'Lista finala cu tot fisierul:{lista_doc}')
    figuri = []
    for elem in lista_doc:
        if 'cerc' in elem:
            nume = elem[0] + elem[1]
            nume = Cerc(elem[1], int(elem[2]), int(elem[3]), int(elem[4]))
            spatiu_lucru = cadran.determinare_cadran(nume)
            if (spatiu_lucru == 1) or (spatiu_lucru == 2) or (spatiu_lucru == 3) or (spatiu_lucru == 4):
                figuri.append(nume)

        elif 'patrat' in elem:
            nume = elem[0] + elem[1]
            nume = Patrat(elem[1], int(elem[2]), int(elem[3]), int(elem[4]))
            spatiu_lucru = cadran.determinare_cadran(nume)
            if (spatiu_lucru == 1) or (spatiu_lucru == 2) or (spatiu_lucru == 3) or (spatiu_lucru == 4):
                figuri.append(nume)

        elif 'dreptunghi' in elem:
            nume = elem[0] + elem[1]
            nume = Dreptunghi(elem[1], int(elem[2]), int(elem[3]), int(elem[4]),
                              int(elem[5]))
            spatiu_lucru = cadran.determinare_cadran(nume)
            if (spatiu_lucru == 1) or (spatiu_lucru == 2) or (spatiu_lucru == 3) or (spatiu_lucru == 4):
                figuri.append(nume)

        elif 'triunghi' in elem:
            nume = elem[0] + elem[1]
            nume = Triunghi(elem[1], int(elem[2]), int(elem[3]), int(elem[4]),
                            int(elem[5]), int(elem[6]))
            spatiu_lucru = cadran.determinare_cadran(nume)
            if (spatiu_lucru == 1) or (spatiu_lucru == 2) or (spatiu_lucru == 3) or (spatiu_lucru == 4):
                figuri.append(nume)
        else:
            print('Nu se creaza nicio clasa.')
    print(('-') * 70)
    final = []

    #fisier_output = r'C:\Users\alin9\PycharmProjects\PythonAlin\checker\output\test9'
    with open(fisier_output, mode = 'a') as file2:
        for figura in figuri:
            coliziuni = []
            semi_incluziuni = []
            lista_id = []
            spatiu = cadran.determinare_cadran(figura)
            if spatiu == 1 or spatiu == 2 or spatiu == 3 or spatiu == 4:
                lista_id.append(figura.id)
                if (len(figuri) >= 1):
                    for figura2 in figuri:
                        if not figura is figura2:
                            if figura.detectie_coliziune(figura.distanta_puncte(figura2), figura2.cerc_incadrare()):
                                print(f'Figura {figura.id} este in coliziune cu {figura2.id}.')
                                coliziuni.append(figura2.id)
                            if figura.semiincluziune(figura.distanta_puncte(figura2), figura2.cerc_incadrare()):
                                print(f'Figura {figura.id} semi-include {figura2.id}.')
                                semi_incluziuni.append(figura2.id)
                    print(f'Figura are id: {lista_id}')
                    print(f'Perechi de figuri in coliziune: {coliziuni}')
                    print(f'Perechi de figuri care se semi-includ: {semi_incluziuni}')
                    print(f'Figura se gaseste in cadranul: {cadran.determinare_cadran(figura)}')
                    listadinamica = []

                    if figura.id:
                        listadinamica.append(figura.id)
                        listadinamica.append('|')
                        if len(coliziuni) > 0:
                            listadinamica = listadinamica+coliziuni
                        else:
                            listadinamica.append('')
                        listadinamica.append('|')
                        if len(semi_incluziuni) >0:
                            listadinamica = listadinamica + semi_incluziuni
                        else:
                            listadinamica.append('')
                        listadinamica.append('|')
                        listadinamica.append(str(cadran.determinare_cadran(figura)))
                    print(listadinamica)
                    #Afisare in fisierul de output.
                    text = ""
                    for cc in listadinamica:
                        text += cc+' '
                    print(f'Textul de afisat: {text}')
                    print(('-') * 70)
                    file2.write(text+'\n')
                    final.append(listadinamica)
                    #print(f'Lista fina cf fisier iesire:{final}')

if __name__ == '__main__':
    fisier_input = r'C:\Users\alin9\PycharmProjects\PythonAlin\checker\input\test8'
    fisier_output = r'C:\Users\alin9\PycharmProjects\PythonAlin\checker\output\test8'
    program_principal(fisier_input, fisier_output)