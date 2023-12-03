#!/usr/bin/python3
def multiple_returns(sentence):
    sentence_len = len(sentence)
    if sentence_len == 0:
        result = None
    else:
        result = (sentence_len, sentence[0])
    return result
