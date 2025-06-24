arr = [1,  2,  3,  4,  5, "1", "2", "3"]
print(arr[-8])

arr1= [1, 2, 3, 4, 5, "1", "2", "3", [[1,2,3],[1,2,3]]]
print(arr1[-1][-1][-1])              #^^^^^^^^^^^^^^^^
#mutable                                  123
arr1[-1]= "123"                         # ^^^
print(arr1[-1])

string = "Otari" #imutable
string = 123
print(string)

og = int(input("ent number:"))
arr2= [1, 2, 3, 4, 5, "1", "2", "3", [[1,2,3],[1,2,3]]]
print(arr2 [og][-1][-1])


bob = [1,  2,  3,  4,  5,]
print(bob[:4])