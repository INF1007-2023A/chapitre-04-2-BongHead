#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_first_part_of_name(name):
	nom=""
	for i in name:
		if not i.isalpha():
			break
		nom+=i
	nom=nom.capitalize()
	return nom

def get_random_sentence(animals, adjectives, fruits):
	return f"Aujourd'hui, j'ai vu un {random.choice(animals)} s'emparer d'un panier {random.choice(adjectives)} plein de {random.choice(fruits)}."
	

def encrypt(text, shift):
	a=""
	for lettre in text:
		if lettre.isalpha():
			lettre = chr(ord(lettre)+shift)
			if not lettre.isalpha():
				lettre = chr(ord(lettre)-26)
		a+=lettre
	return a


def decrypt(encrypted_text, shift):
	return encrypt(encrypted_text,-shift)


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangue")
	print(get_random_sentence(animals, adjectives, fruits))
	
	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
