#!/usr/bin/python

import codecs
from ftplib import FTP
import zipfile,os.path

def unzip(source_filename, dest_dir):
  with zipfile.ZipFile(source_filename) as zf:
    for member in zf.infolist():
      # Path traversal defense copied from
      # http://hg.python.org/cpython/file/tip/Lib/http/server.py#l789
      words = member.filename.split('/')
      path = dest_dir
      for word in words[:-1]:
          drive, word = os.path.splitdrive(word)
          head, word = os.path.split(word)
          if word in (os.curdir, os.pardir, ''): continue
          path = os.path.join(path, word)
      zf.extract(member, path)

def downloadEdict():
  print "Logging in to ftp site to download the latest edict."
  ftp = FTP('ftp.monash.edu.au')
  ftp.login()
  # ftp.retrlines('LIST')
  print "Downloading edict"
  ftp.cwd('pub/nihongo')
  # ftp.retrlines('LIST')
  ftp.retrbinary('RETR edict.zip',open('edict.zip', 'wb').write)
  print "Unzipping edict file."
  unzip('edict.zip',".")

if not os.path.exists("edict"):
  downloadEdict()

with codecs.open("edict","r","eucJP") as input, codecs.open("pairs","w","utf8") as output :
  for line in input:
    line=line.rstrip()
    words=line.split()
    firstWord=words[0]
    if len(firstWord) ==2:
      #fW_utf8=firstWord.encode('UTF-8')
      #print >>output,fW_utf8 
      print >>output,firstWord 
