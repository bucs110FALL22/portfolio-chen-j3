class StringUtility:
  def __init__(self, string):
    self.string = string

  def __str__(self):
    """
    Returns original string
    """
    return self.string

  def vowels(self):
    """
    Returns the integer if the number of vowels in the string is less than 5. Otherwise, it returns the string "many"
    """
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
    """
    Returns a new string of the first and last two characters of the original string
    """
    if len(self.string) <= 2:
      return ""
    else:
      return f"{self.string[0]}{self.string[1]}{self.string[-2]}{self.string[-1]}"

  def fixStart(self):
    """
    Returns a string where occurences of the first character after the ffirst character is changed to a *
    """
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
    """
    Returns an integer that is the sum of the ascii values in the string
    """
    sum = 0
    for char in self.string:
      sum = sum + ord(char)
    return sum
    
  def cipher(self):
    """
    Returns a new string that is encoded
    """
    #shift based on length of string
    shift = len(self.string)
    newString = ""
    alphabet = list(string.ascii_letters)
    #wrap around
    
            

        
    # for char in self.string:
    #   new_ascii = ord(char) + shift
    #   char = chr(new_ascii)
    #   newString = newString + char
    return newString