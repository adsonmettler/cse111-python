# Author: Adson Mettler do Nascimento

""" Program: Turing Test"""

# Description: Basically this program gets randomly pieces of a sentence from a datatable
# and, by using functions, the program returns a sentence. It is a sentence generator.


########## Exceeding the Requirements ############
# In the exceeding activity I added another call to get_prepositional_phrase so that
# each sentence includes two prepositional phrases.

import random


def main():

    sentence_a = make_sentence(1, "past")
    print(f"{sentence_a.capitalize()}.")
    sentence_b = make_sentence(1, "present")
    print(f"{sentence_b.capitalize()}.")
    sentence_c = make_sentence(1, "future")
    print(f"{sentence_c.capitalize()}.")
    sentence_d = make_sentence(2, "past")
    print(f"{sentence_d.capitalize()}.")
    sentence_e = make_sentence(2, "present")
    print(f"{sentence_e.capitalize()}.")
    sentence_f = make_sentence(2, "future")
    print(f"{sentence_f.capitalize()}.")


def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".
    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    # Randomly choose and return a determiner.
    word = random.choice(words)

    return word


def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"
    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    # Randomly choose and return a noun.
    word = random.choice(words)

    return word

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"
    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    verb = random.choice(verbs)

    return verb

def make_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """
    ########## Exceeding the Requirements ############
    # In the exceeding activity I added another call to get_prepositional_phrase so that
    # each sentence includes two prepositional phrases.

    if quantity == 1 and tense == "past":
        sentence = get_determiner(1) + " " + get_noun(1) + " " + get_prepositional_phrase(1) + " " + get_verb(1, "past") + " " + get_prepositional_phrase(1)
    elif quantity == 1 and tense == "present":
        sentence = get_determiner(1) + " " + get_noun(1) + " " + get_prepositional_phrase(1) + " " + get_verb(1, "present") + " " + get_prepositional_phrase(1)
    elif quantity == 1 and tense == "future":
        sentence = get_determiner(1) + " " + get_noun(1) + " " + get_prepositional_phrase(1) + " " + get_verb(1, "future") + " " + get_prepositional_phrase(1)
    elif quantity != 1 and tense == "past":
        sentence = get_determiner(quantity!=1) + " " + get_noun(quantity!=1) + " " + get_prepositional_phrase(quantity!=1) + " " + get_verb(quantity!=1, "past") + " " + get_prepositional_phrase(quantity!=1)
    elif quantity != 1 and tense == "present":
        sentence = get_determiner(quantity!=1) + " " + get_noun(quantity!=1) + " " + get_prepositional_phrase(quantity!=1) + " " + get_verb(quantity!=1, "present") + " " + get_prepositional_phrase(quantity!=1)
    elif quantity != 1 and tense == "future":
        sentence = get_determiner(quantity!=1) + " " + get_noun(quantity!=1) + " " + get_prepositional_phrase(quantity!=1) + " " + get_verb(quantity!=1, "future") + " " + get_prepositional_phrase(quantity!=1)
    
    return sentence

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"
    Return: a randomly chosen preposition.
    """
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    
    # Randomly choose and return a determiner.
    preposition = random.choice(prepositions)

    return preposition


def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.
    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """
    if quantity == 1:
        phrase = get_preposition() + " " + get_determiner(1) + " " + get_noun(1)
    elif quantity !=1:
        phrase = get_preposition() + " " + get_determiner(2) + " " + get_noun(2)

    return phrase

# Start this program by
# calling the main function.
main()