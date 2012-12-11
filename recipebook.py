#!/usr/bin/env python3

import argparse
import os
import sys

class Ingredient:
    amt = None
    units = None
    item = None
    def __init__(self, quantity, units, item):
        self.amt = quantity
        self.units = units
        self.item = item

    def to_tex(self):
        ret = ""
        if self.amt:
            ret += "$" + str(self.amt) + "$"

        if self.units:
            if len(self.units) > 2:
                ret += " "
            ret += self.units

        if self.item:
            if (self.units or self.amt):
                ret += " "
            ret += self.item

        return ret

    def __repr__(self):
        return self.item

def instr_to_tex(s):
    return s.replace("\degc", "$^{\circ}\\text{C}$")

class Recipe:
    def __init__(self):
        self._ingredients = []
        self._instructions = []
        self._name = None
        self._serves = None
        self._comment = None

    def comment(self, words)
        self._comment = words

    def do(self, instr):
        assert(type(instr) == str)
        self._instructions.append(instr)

    def image(self, fname):

    def ingredient(self, *args):
        I = None
        if len(args) == 1: # e.g. A pinch of salt
            I = Ingredient(None, None, args[0])
        elif len(args) == 2: # e.g. 2 onions. Technically 'onions' is the unit.
            I = Ingredients(args[0], args[1], None)
        elif len(args) == 3: # Quantity, units, ingredient
            I = Ingredient(args[0], args[1], args[2])
        else:
            print("Recipe.ingredient: Invalid number of arguments (%d)"
                  % (len(args)))

        if (I != None):
            self._ingredients.append(I)

    def name(self, n):
        self._name = n

    def serves(self, n):
        self._serves = n

    def to_tex(self):
        ret = "\\section{" + self._name + "}\n"
        if len(self._ingredients) > 0:
            ret += ("  \\subsection*{Ingredients}\n"
                    "    \\begin{itemize}\n")
            for i in self._ingredients:
                ret += "      \\item " + i.to_tex() + "\n"
            ret += "    \\end{itemize}\n"

        if len(self._instructions) > 0:
            ret += ("  \\subsection*{Method}\n"
                    "    \\begin{itemize}\n")
            for i in self._instructions:
                ret += "      \\item " + instr_to_tex(i) + "\n"
            ret += "    \\end{itemize}\n"

        return ret

    def __eq__(self, other): return self._name == other._name
    def __ne__(self, other): return self._name != other._name
    def __lt__(self, other): return self._name <  other._name
    def __le__(self, other): return self._name <= other._name
    def __gt__(self, other): return self._name >  other._name
    def __ge__(self, other): return self._name >= other._name

class Book:
    recipes = []

    def add_recipe(self, R):
        if type(R) != Recipe:
            raise TypeError
        self.recipes.append(R)
        self.recipes.sort()

    def run_recipe(self, filename):
        fp = open(filename, "r")
        code = compile(fp.read(), filename, 'exec')
        exec(code, {"Recipe":Recipe, "add":self.add_recipe})

    def to_tex(self):
        ret = ("\\documentclass[a4paper]{article}\n"
               "\\usepackage{amsmath}\n"
               "\\usepackage{graphicx}\n\n"
               "\\title{Recipes}\n"
               "\\author{}\n"
               "\\date{}\n"
               "\\begin{document}\n"
               "\\maketitle\n"
               "\\tableofcontents\n"
               "\\newpage\n"
               "\n")
        
        for i in self.recipes:
            ret += i.to_tex() + "\n"

        ret += "\\end{document}"
        return ret

def recurse_dirs(fname_list):
    ret = []
    for fname in fname_list:
        if os.path.isdir(fname) and not os.path.islink(fname):
            ret.extend(recurse_dirs([fname + os.path.sep + x
                                    for x in os.listdir(fname)]))
        elif not os.path.exists(fname):
            print("Warning: File '%s' doesn't exist." % (fname))
        elif os.path.splitext(fname)[1] == '.py':
            ret.append(fname)

    return ret

def parse_arguments():
    parser = argparse.ArgumentParser(description = "Convert recipes to LaTeX.")
    parser.add_argument("-o", "--out", type = str, default = None,
                        help = "specify the output file name")
    parser.add_argument("infiles", type = str, nargs = '+',
                        metavar = "file/dir")

    return parser.parse_args()

args = parse_arguments()
B = Book()
files = recurse_dirs(args.infiles)
for fname in files:
    B.run_recipe(fname)

print(B.to_tex())
