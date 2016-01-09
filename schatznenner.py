#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random as r

adjektiven = [['süßer ','süße ','süßes '], 
              ['lieber ', 'liebe ', 'liebes '], 
              ["lieblicher ", "liebliche ", "liebliches "],
              ["holder ","holde ","holdes "]]
pr = [['mein ', 'meine ','mein '],
      ['','',''],
      ['du ','du ','du '],
      ['du bist ein echter ', 'du bist eine echte ', 'du bist ein echtes ']]
artikels = ["der", "die", "das"]

def parse_word(x):
    """Parses the read word"""
    global artikels
    artikel = artikels.index(x[0:3])
    wort = x.split(",")[0][4:-1] + x.split(",")[0][-1]
    return artikel, wort


def get_random_compliment():
    """Gets a random and sweet compliment to name your German girlfriend"""
    global adjektiven, pr, artikels
    idx = r.randint(0,999)
    with open('woerter.txt') as f:
        lines = f.readlines()
        artikel, wort = parse_word(lines[idx])
    pr_idx = r.randint(0,len(pr)-1)
    k = pr[pr_idx][artikel]
    for num_adj in range(r.randint(1,2)):
        adj_idx = r.randint(0,len(adjektiven)-1)
        k =  k + adjektiven[adj_idx][artikel]
    
    schatz = r.randint(0,1)
    if schatz == 1:
        k = k + "Schatz" + wort.lower()
    else:
        k = k + wort
    
    herzi = r.randint(0,1)
    if herzi == 1:
        k = k + " <3"
    k = k[0].upper() + k[1:]
    return k


def main():
    print(get_random_compliment())


if __name__ == "__main__":
    main()
