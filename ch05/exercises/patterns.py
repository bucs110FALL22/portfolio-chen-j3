#part 1
def star_pyramid():
  rows = int(input("Input the number of rows you want:"))
  stars = 1
  for i in range(rows+1): #+1 bc if rows = 5, 5 is inconclusive
    print("*" * stars)
    stars = stars + 1
star_pyramid()

#part 2
# def rstar_pyramid():
#   rows = int(input("Input the number of rows you want:"))
#   while rows != 0:
#     print("*" * rows)
#     rows = rows - 1
# rstar_pyramid()

def rstar_pyramid():
  rows = int(input("Input the number of rows you want:"))
  for i in range(rows + 1):
    print ("*" * rows)
    rows = rows -1
rstar_pyramid()