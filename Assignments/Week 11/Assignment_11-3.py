def largeOddNum(s):
  result = ""
  digit_list = list(s)
  for i in range(len(digit_list)-1,-1,-1):
    if int(digit_list[i])%2 != 0:
      result = "".join(digit_list[:i+1:])
      while result[0] == '0':
        result = result[1::]
      return '"'+result+'"'
  return '"'+'"'