#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:
integer = 5
print(integer)


# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:
type(8.5)




# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:

type(integer)



# 4) Crear una variable que contenga tu nombre

# In[2]:
name = "Mathias VIllanueva"



# 5) Crear una variable que contenga un número complejo

# In[3]:
complex = 3j




# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:
type(complex)




# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:


pi = 3.1416


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:

bool = True
strg = "True"


# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:
print(type(bool))
print(type(strg))




# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:
sum1 = 3+3.14




# 11) Realizar una operación de suma de números complejos

# In[2]:
15j -3j




# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:

13 + 8j



# 13) Realizar una operación de multiplicación

# In[5]:

3*3



# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:
print(2**8)



# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:
print(27/4)




# 16) De la división anterior solamente mostrar la parte entera

# In[9]:
print(27//4)




# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:
print(27%4)




# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:
6*4 + 3



# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:

name1 = "sandra"
name2 = "ana"
names = name1 + name2
print(names)


# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:
2 == "2"




# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:
2 == int("2")




# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:
a = float('3,8')




# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:
valor = 3
valor -=1
print(valor)


# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:
1 << 2




# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:

2 + '2'




# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:
2 * '2'



# %%
