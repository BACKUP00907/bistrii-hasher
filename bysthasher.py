
def hash(arg1, arg2, arg3):
  # salt
  f = open(str(arg3),"rb")
  salt = f.read()

  # derived opressions
  lopmya =0;
  
  muln = salt[504:]

  addn  = salt[:8]

  mulodr = salt[8:10]

  addrn = salt[10:12]

  if int(addrn) > int(mulodr) :

    lopmya = 1
  else:
    lopmya = -1
  
  # itr

  itr = addrn = salt[216:214]
  
  # plainbin
  f = open(str(arg2),"rb")
  plb = f.read()

  # hasher& compressor
  
  nplb = salt + plb + salt



  
  for itr >= 0:

    if lopmya < 0 :
      nplb= int(nplb) * int(muln)
      nplb= int(nplb) + int(addn)

    if lopmya > 0 :
      nplb= int(nplb) + int(addn)
      nplb= int(nplb) * int(muln)

    itr = itr -1

  nplb = nplb * salt
  return nplb

def dehash(arg1, arg2, arg3):
  # salt
  f = open(str(arg3),"rb")
  salt = f.read()

  # derived opressions
  lopmya =0;
  
  muln = salt[504:]

  addn  = salt[:8]

  mulodr = salt[8:10]

  addrn = salt[10:12]

  if int(addrn) > int(mulodr) :

    lopmya = 1
  else:
    lopmya = -1
  
  # itr

  itr = addrn = salt[216:214]
  
  # plainbin
  f = open(str(arg2),"rb")
  nplb = f.read()

  # hasher& compressor

  nplb = nplb / salt
  



  
  for itr >= 0:

    if lopmya < 0 :
      nplb= int(nplb) - int(addn)
      nplb= int(nplb) / int(muln)
      

    if lopmya > 0 :
      nplb= int(nplb) / int(muln)
      nplb= int(nplb) - int(addn)
      

    itr = itr -1

  
  nplb = byte(nplb)
  nplb = salt + plb + salt

# todo solve for nplb -> plb

  
    
  
    
