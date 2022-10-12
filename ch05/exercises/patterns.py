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

#prof solution
# def star_pyramid():
#     levels = int(input("Enter the desired pyramid height: "))
#     for i in range(1, levels + 1):
#         print("*" * i)


# def rstar_pyramid():
#     levels = int(input("Enter the desired pyramid height: "))
#     for i in range(levels, 0, -1):
#         print("*" * i)


# star_pyramid()
# rstar_pyramid()