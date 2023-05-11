import random
Nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
Verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
Adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
Prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
Adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]
#a new list to be made from the individual old lists
newNoun = []
newVerb = []
newPreposition = []
newAdverb = []
# 3 different nouns
# 3 different verbs
# 3 different adjectives
# 2 prepositions
# 1 Adverb

def makePoem():
    while random.choice(Nouns) == random.choice(Nouns):

        for x in Nouns:
            print(x)

    # print(random.choice(Adjectives))
    # print(random.choice(Nouns))
    # print(random.choice(Verbs))
    # print(random.choice(Prepositions))
    # print(random.choice(Adverbs))


makePoem()