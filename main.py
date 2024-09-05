def BracketMatcher(strParam):
  # Sinan Koşar
  strParam = strParam.split(" ")
  x=0
  y=0
  if len(strParam) >1:
    for i in strParam:
      for j in range(len(i)):
        if i[j] == "(":
          x+=1
        elif i[j] == ")":
          y+=1

  else:
    strParam = "".join(strParam)
    for i in range(len(strParam)):
      if strParam[i] == "(":
        x += 1
      if strParam[i] == ")":
        y += 1

  if x == y:
    return "true"
  else:
    return "false"
  # code goes here
  return strParam

# keep this function call here
print(BracketMatcher("(merhaba() 3dünya))"))#false
print(BracketMatcher("(merhaba(dünya))"))#true