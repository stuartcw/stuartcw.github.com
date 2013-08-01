#!/usr/bin/python

import sys
import codecs

words=sys.argv[1:]
words=[ codecs.decode(c, "utf8") for c in words[:len(words)/2] ]

positions={}
for i, word in enumerate(words):
  position=sys.argv[1+len(words)+i]
  print i, word, position  
  positions[words[i]]=position

wordSets={}
for word in words:
  wordSets[word]=set()

with codecs.open("pairs","r","utf8") as input:
  for line in input:
    line=line.rstrip()
    for word in words: 
      if word in line:
        firstChar=line[0]
        secondChar=line[1]
        if firstChar==word and positions[word]=="start":
           other=secondChar
        elif secondChar==word and not positions[word] == "start":
           other=firstChar
        else:
           continue
        out=line+" "+word+" at "+ positions[word]+ " 2nd char is "+ other
        print out.encode('UTF-8')
        otherChars=wordSets[word]
        otherChars.add(other)
        wordSets[word]=otherChars

answers=wordSets[word[0]]

for word in words[1:]:
  answers=answers.intersection(wordSets[word])

for answer in answers:
  print answer.encode('utf8')
