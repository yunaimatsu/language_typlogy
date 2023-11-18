"""
Este es un tutorial de procesamiento del lenguaje natural (NLP).
Explica cómo usar algunas bibliotecas y técnicas comunes de NLP en Python.
"""
import nltk
from nltk.tokenize import word_tokenize

text = "This is a sample sentence."
tokens = word_tokenize(text)
print(tokens)
