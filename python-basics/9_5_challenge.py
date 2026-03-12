# -*- coding: utf-8 -*-
"""
created on 2026-03-09 16:59:20
@author: michael garcia mikejgarcia@gmail.com
version 1.0
"""
import random

nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]

def make_poem():
    noun1 = random.choice(nouns)
    noun2 = random.choice(nouns)
    noun3 = random.choice(nouns)
    while noun1 == noun2:
        noun2 = random.choice(nouns)
    while noun1 == noun3 or noun2 == noun3:
        noun3 = random.choice(nouns)
    vb1 = random.choice(verbs)
    vb2 = random.choice(verbs)
    vb3 = random.choice(verbs)
    while vb1 == vb2:
        vb2 = random.choice(verbs)
    while vb1 == vb3 or vb2 == vb3:
        vb3 = random.choice(nouns)
    adj1 = random.choice(adjectives)
    adj2 = random.choice(adjectives)
    adj3 = random.choice(adjectives)
    while adj1 == adj2:
        adj2 = random.choice(adjectives)
    while adj1 == adj3 or adj2 == adj3:
        adj3 = random.choice(adjectives)
    prep1 = random.choice(prepositions)
    prep2 = random.choice(prepositions)
    while prep1 == prep2:
        prep2 = random.choice(prepositions)
    adv1 = random.choice(adverbs)
    if adj1.startswith(("a", "e", "i", "u")):
        article1 = "An"
    else:
        article1 = "A"
    if adj3.startswith(("a", "e", "i", "u")):
        article2 = "an"
    else:
        article2 = "a"
    poem = (
        f"{article1} {adj1} {noun1} \n\n"
        f"{article1} {adj1} {noun1} {vb1} {prep1} the {adj2} {noun2} \n"
        f"{adj1}, the {noun1} {vb2} \n the {noun2} {vb3} {prep2} {article2} {adj3} {noun3}" 
        )
    return poem

poem = make_poem()
print(poem)
