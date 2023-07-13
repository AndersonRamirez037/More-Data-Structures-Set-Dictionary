#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None 
    max_score = float()
    for i in a_dictionary:
        if a_dictionary[i] > max_score:
            max_score = a_dictionary[i]
            max_score_name = i
    return max_score_name