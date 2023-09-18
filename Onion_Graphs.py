"""
Onion graphs are aesthetically pleasing series that plots for any positive integer n:
[x^(1/n) , x^(1/(n-1)) , ...., x^0 , x^1, ..., x^n] in the x range of [0, 1]
This altogether looks like an onion.
This code will plot the onion lines for the given n number.

"""
from fractions import Fraction
import matplotlib.pyplot as plt


n = 15 #Number of Onions

#Creating the list of Exponent Coefficients
list1 = [x for x in range(1, n+1)]  #List of integer coeeficients

liste = [Fraction(1, x) for x in range(2, n+1)] #Fraction(1, x) = 1/x #List of fractional coefficents
liste.reverse()

liste.extend(list1)

print("Exponent coefficients are:", liste)


#Creating Onion Lines #Key^leri matris ismi, value'ları boş matris olan bir dictionary yaratacağım.
mat_dict = {} #A dictionary which will have matrice names as keys and empty list as values.
for x in range(len(liste)):
    Matrix_name = "Matrix" + str(liste[x])
    mat_dict[Matrix_name] = []

print(f"Created matrice dictionary is: {mat_dict}")

#Filling the matrice
Range = [0, 1.001] #Range of the x values. You should not change it because it only looks like "onion" in the range [0-1]
#The upper value has been chosen a little over 1 to prevent floating point error.

sensitivity = 0.005 #The x value will increase this much in every while loop
i = Range[0] #Initial value of x
A = [] #I willl save x values in this matrice

while i <= Range[1]:

    for x in range(len(liste)):
        mat_dict["Matrix" + str(liste[x])].append(i ** liste[x]) #The matrice in the values is appended by x^liste[x]

    A.append(i)
    i += sensitivity

#Plotting

plt.figure(facecolor="grey", figsize=(12, 12))
plt.axes(facecolor="lightblue")

plt.xlabel("x")
plt.ylabel("y")
plt.grid(color="black", which="both")

for x in mat_dict:

    label = str(("y=x^" + x.removeprefix("Matrix")))
    plt.plot(A, mat_dict[x], label=label)


plt.legend(facecolor="grey", loc=(1, 0))
plt.show()
