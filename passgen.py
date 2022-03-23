#!/usr/bin/env python3
import random
import string
import argparse

parser = argparse.ArgumentParser()

def Generate(length,letters,nums,puncts,rep,out):
    _letters = []
    _nums = []
    _puncts = []
    pas=""
    if letters:
        _letters.insert(0,(string.ascii_letters))
    if nums:
        _nums.insert(0,string.digits)
    if puncts:
        _puncts.insert(0,string.punctuation)
    for i in range(rep):
        pas = pas+"\n"+ ''.join([random.choice( ''.join(_letters + _nums+ _puncts )) for n in range(length)])
    if out.strip():
        f = open(out,'a')
        f.write(pas+"\n")
        f.close()
    print(pas)

def Greshuffle(length,strings,rep,out):
    pas=""
    for i in range(rep):
        pas =pas+"\n"+ ''.join([random.choice( strings ) for n in range(length)])
    if out.strip():
        f = open(out,'a')
        f.write(pas+"\n")
        f.close()
    print(pas)

def GenerateBD(length,alph,rep):
    pas=''
    with open(alph, 'r') as f:
        words = f.read().splitlines()
    for i in range(rep):
        pas = pas+"\n"+ ''.join([random.choice( words ) for n in range(length)])
    print(pas)

parser.add_argument("length",  help = "Password length", type = int)
parser.add_argument("-res","--reshuffle", default=argparse.SUPPRESS, help = "Generate a password from given characters", type = str)
parser.add_argument("-l","--letters", action='store_true', default=argparse.SUPPRESS, help = "Includes letters")
parser.add_argument("-n","--nums", action='store_true', default=argparse.SUPPRESS, help = "Includes numbers")
parser.add_argument("-p","--puncts", action='store_true', default=argparse.SUPPRESS, help = "Includes punctuation")
parser.add_argument("-o","--out", default=argparse.SUPPRESS, help = "Write a password to a file", type = str)
parser.add_argument("-rep","--repetitions", default=argparse.SUPPRESS, help = "Number of generated passwords", type = int)
parser.add_argument("-genBD","--generatebydictionary", default=argparse.SUPPRESS, help = "generate by dictionary", type = str)
args = parser.parse_args()

length = int(args.length)

letters=False
nums = False
puncts = False
out=""
rep=1

if "nums" in args:
    nums = True
if "puncts" in args:
    puncts = True
if "letters" in args:
    letters = True
if "out" in args:
    out = int(args.out)
if "repetitions" in args:
    rep = int(args.repetitions)
if "reshuffle" in args:
    reshuffle = str(args.reshuffle)
    Greshuffle(length,reshuffle,rep,out)
elif "generatebydictionary" in args:
    direct = str(args.generatebydictionary)
    GenerateBD(length,direct,rep)
else:
    Generate(length,letters,nums,puncts,rep,out)
