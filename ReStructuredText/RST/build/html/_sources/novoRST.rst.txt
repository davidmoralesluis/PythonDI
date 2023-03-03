***************************
Exemplo de documentación con RST
***************************

Un parágrafo en Restructure text é o bloque máis básico e non temos que marcalo de forma
especial.
S6 temos que respetar a tabulación. Para remarcar utilizamos *italica* cun só asterisco. Temos
outras opcións como a **negriña**  con dobre asterisco ou con dobre comilla para ``código este e
o texto tipo código``.

Para facer unha lista:

* O primeiro elemento
* Segundo elemento.
  Este elemento utiliza máis dunha liña


Lista autonumerada

    #. Primeiro elemento
    #. Segundo elemento
    #. (Tabular para asociar)

1. Primeiro elemento
2. Segundo elemento

Termino (na parte de arriba do texto)
  Definición do termo, que ten que ser tabulado.

  Pode ter varios parágrafos.

Outro termo.
    Definición doutro termo

Este é un texto do parágrafo. O seguinte parágrafo é un exemplo do código :
  def nomeFuncion (parametro, parametro2):
    print ("Fai algo con "+str(parametro))
    print ("Outra cousa" +parametro2)
    return 1
Xa continuamos co texto normal
