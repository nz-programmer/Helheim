#Helheim V1.0

lotsOfNumbers=[99,0,1,112,2,5,0,1,97,2,5,0,1,115,2,5,0,1,115,2,5,0,1,119,2,5,0,1,111,2,5,0,1,114,2,5,0,1,100,2,5,42,3,115,3,101,3,99,3,114,3,101,3,116,3,32,3,112,3,104,3,114,3,97,3,115,3,101,4]
def numberBaseDoodadFunctionerator(aNumberThatIsNotThatInteresting):
 if aNumberThatIsNotThatInteresting==0: return "0"
 s=""
 while aNumberThatIsNotThatInteresting>0:
  s=str(aNumberThatIsNotThatInteresting%5)+s; aNumberThatIsNotThatInteresting//=5
 return s
P=[numberBaseDoodadFunctionerator(k) for k in lotsOfNumbers]
counter=0;j=0;g=0;counterCounter=0
_g=getattr;_b=__builtins__
pp=_g(_b,"".join([chr(x) for x in [112,114,105,110,116]]))
ii=_g(_b,"".join([chr(x) for x in [105,110,112,117,116]]))
pr="".join(map(chr,[69,110,116,101,114,32,112,97,115,115,119,111,114,100,10]))
e=[ord(i) for i in ii(pr)]
o=[]
while 1:
 if counter<0 or counter>=len(P): break
 t=int(P[counter],5)
 if t==0:
  if j>=len(e): pp("".join(map(chr,[87,114,111,110,103,32,112,97,115,115,119,111,114,100]))); break
  g=e[j]; j+=1
 elif t==1:
  if counter+1>=len(P): pp("".join(map(chr,[87,114,111,110,103,32,112,97,115,115,119,111,114,100]))); break
  counterCounter=int(P[counter+1],5); counter+=1
 elif t==2:
  if g!=counterCounter: pp("".join(map(chr,[87,114,111,110,103,32,112,97,115,115,119,111,114,100]))); break
 elif t==3:
  if counter+1>=len(P): break
  o.append(int(P[counter+1],5)); counter+=1
 elif t==4:
  pp("".join(map(chr,o))); break
 elif t==5:
  pass
 else:
  pass
 counter+=1
