import math
import re
from collections import Counter
import random as rn 
import itertools as it

file = './04_paper.txt'

def letter_normalization(letter,
                         to_replace):
    if letter in to_replace:
        return to_replace[letter] 
    return letter

with open(file, 'r', encoding='utf8') as text:
    lines = (re.sub(r'[^\w\s]', '', line).lower() for line in text)
    characters = it.chain.from_iterable(lines)
    result = list(characters)

print(set(result))
print(len(Counter(result)))
print("")

to_replace = {
    'ł': 'l',
    'ü': 'u',
    'ä': 'a',
    'ö': 'o',
    'ç': 'c',
    'é': 'e',
    'è': 'e',
    '_': ' '}

norm_result = []

with open(file, 'r', encoding='utf8') as text:
    lines = (re.sub(r'[^\w\s]', '', line).lower() for line in text)
    characters = it.chain.from_iterable(lines)
    result = list(characters)
    for letter in result:
        modified_letter = letter_normalization(letter, to_replace)
        norm_result.append(modified_letter)

print(set(norm_result))
print(len(Counter(norm_result)))
print("")

# words

with open(file, 'r', encoding='utf-8') as f:
    text = f.read().lower()
    words = re.findall(r'\b[a-zàèéìòù]+\b', text)

print(Counter(words).most_common(20))

def apply_temperature(probs, T):
    
    adjusted_prob0 = []
    for w, p in probs:
        adjusted_prob0.append(math.pow(p, 1.0 / T))

    total = sum(adjusted_prob0)
    adjusted_prob = [(probs[i][0], adjusted_prob0[i]/total) for i in range(len(adjusted_prob0))]

    return adjusted_prob

def gen_text_ngrams_entropy(transitions, length, start=None, T=1):

    if start is None:
        start = rn.choice(list(transitions.keys()))
    
    new_text = list(start)
    context = start

    for _ in range(length - len(start)):
        
        if context not in transitions:
            break
        
        probs = transitions[context]
        probs_temp = apply_temperature(probs, T)
        
        ww = []
        pp = []
        for w, p in probs_temp:
            ww.append(w)
            pp.append(p)

        nw = rn.choices(ww, weights=pp, k=1)[0]
        new_text.append(nw)
        context = tuple(new_text[-len(start):])  
    
    return ' '.join(new_text)

def create_ngrams(words, n):
    ngrams = []
    for i in range(len(words) - n + 1):
        ngram = tuple(words[i:i+n])
        ngrams.append(ngram)
    return ngrams

def calculate_transions(words, ngrams):
    
    ngrams_counts = Counter(ngrams)

    ngrams_minus1 = create_ngrams(words, n-1)
    ngrams_minus1_counts = Counter(ngrams_minus1)
    
    prob_cond = {}
    for ng in ngrams_counts:
        context = ng[:-1]  
        prob_cond[ng] = ngrams_counts[ng] / ngrams_minus1_counts[context]
        
    transitions = {}

    for ng, p in prob_cond.items():
        context = ng[:-1]
        if context not in transitions:
            transitions[context] = []
        transitions[context].append((ng[-1], p))
        
    return transitions

n = 2
T = 0.1

ngrams = create_ngrams(words, n)
transitions = calculate_transions(words, ngrams)
new_text = gen_text_ngrams_entropy(transitions, 50, ('the',), T=T)
print(f"testo generato con {n}-grammi e temperatura T={T}")
print(new_text)
print("")