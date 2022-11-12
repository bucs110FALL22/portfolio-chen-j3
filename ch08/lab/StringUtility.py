class StringUtility:
  def __init__(self, string):
    self.string = string

  def __str__(self):
    return self.string

  def vowels(self):
    count = 0
    string = self.string.lower()
    for char in string:
      if char in "aeiou":
        count += 1
    if count >= 5:
      return "many"
    else:
      return str(count)

  def bothEnds(self):
    if len(self.string) <= 2:
      return ""
    else:
      return f"{self.string[0]}{self.string[1]}{self.string[-2]}{self.string[-1]}"

  def fixStart(self):
    if len(self.string) <= 1:
      return self.string
    else:
      firstChar = self.string[0]
      newString = ""
      for i in self.string:
        if i == self.string[0]:
          newString = newString + firstChar
        elif i != firstChar:
          newString = newString + i
        else:
          newString = newString + "*"
      return newString

  def asciiSum(self):
    sum = 0
    for char in self.string:
      sum = sum + ord(char)
    return sum
    
  def cipher(self):
    shift = len(self.string)
    newString = ""
    for char in self.string:
      new_ascii = ord(char) + shift
      char = chr(new_ascii)
      newString = newString + char
    return newString

#extra credit
  def methodName(self):
    pass