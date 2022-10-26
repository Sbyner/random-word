#!/usr/bin/env python3
import secrets
from json import load
from os.path import abspath, dirname, join

def get_random_word():
    source = join(dirname(__file__), "database", "words.json")
    with open(source) as word_database:
        valid_words = load(word_database)
    return secrets.choice(list(valid_words.keys()))
