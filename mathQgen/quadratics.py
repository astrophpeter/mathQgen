import pylatex
from pylatex import Document, Section, Itemize, Enumerate, Description, \
Command, NoEscape
from pylatex.math import Math


def make_quadratic_tex(a, b, c, unknown="x"):
     """Makes the LaTeX code for a given
     quadratic expression
   
     ax^2 + bx + c

     Args:
         a : x^2 coeff
         b : x coeff
         c : constant
         unkown : symbol of the unknown
     Returns:
         expression : LaTeX expression for the quadratic
     """

     return ("$" + str(a) + unknown + "^{2}" + " + "
             + str(b) + unknown + "+"
             + str(c) + "$")

def make_quadratic_factored_tex(a,b,unknown="x"):
    """Makes the LaTeX code for a product of two
    roots of a quadratic
 
    (x-a)(x-b)

    Args:
        a : solution 1
        b : solution 2
    Returns:
        expression : Latex epression for the factored
            quadratic
    """

    return ("$" + "(" + unknown + "-" + str(a) + ")" 
             + "(" + unknown + "-" + str(b) + ")" + "$")

doc = Document()


with doc.create(Section('Factorise the following quadratics')):
    with doc.create(Enumerate()) as enum:
        for i in range(20):    
            enum.add_item(NoEscape(make_quadratic_factored_tex(i,3)))
            

doc.generate_pdf('lists', clean_tex=False)

print(make_quadratic_tex(3,2,1))

     
