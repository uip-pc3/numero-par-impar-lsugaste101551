def par_impar(n):
    """
        Par Impar
        Admite un numero y evalua si es par
        Parameters
        -----------
        n : int
            Numero a evaluar
        Returns
        -------
        bool
            Resultado de evaluar si es par el numero
        """
    if n%2 == 0 :
        print("Es par")
        return "Par"
    else:
        print("No es par")
        return "Inpar"

if __name__ == "__main__":
    a = True
    while a:
        n = int(input("Numero: "))
        a = False
    par_impar(n)