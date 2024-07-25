def base7(num):
    if num ==0:
    
        return "0"
    negative = num < 0
    num = abs (num)
    result = " "
    while num > 0:
        remainder = num %7
      reslut = str (remainder )+ result;
      num // = 7
      if negative :
          result = "_" + result
          return result
     num = 100
     print (base7(num))


