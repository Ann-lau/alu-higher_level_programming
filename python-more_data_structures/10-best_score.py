#!/usr/bin/python3
def best_Score(a_dictionary):
    if not a_dictionry:
        return None
    max = list(a_dictionary.items())[0][1]
    for key value in a_dictionary.items():
        if value > max:
    for key  value in a_dictionary.items():
        if value == max:
            return key
