#!/usr/bin/env python
# ransom_note.py
# https://www.hackerrank.com/challenges/ctci-ransom-note/

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    hash_dict_note = get_hash_dict(note)
    hash_dict_magazine = get_hash_dict(magazine)
    for k,v in hash_dict_note.items():
    	note_count = hash_dict_note.get(k)
    	magazine_count = hash_dict_magazine.get(k)
    	if (not magazine_count) or (magazine_count < note_count):
    		return False
    return True


def get_hash_dict(input_list):
	counts = dict()
	for i in input_list:
	  counts[i] = counts.get(i, 0) + 1
	return(counts)

magazine = "apgo clm w lxkvg mwz elo bg elo lxkvg elo apgo apgo w elo bg".split()
note = "elo lxkvg bg mwz clm w".split()
# magazine = "give me one grand today night".split()
# note = "give one grand round today".split()
print(checkMagazine(magazine, note))
