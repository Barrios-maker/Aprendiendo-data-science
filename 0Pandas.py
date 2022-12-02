import pandas as pd
import numpy as np

a=np.array([[1,3,0,1,8],[1,0,7,9,3],[0,1,8,3,-8],[0,0,0,0,0]])

b=pd.DataFrame(a,index=['r1','r2','r3','r4'],columns=['c1','c2','c3','c4','c5'])

#print(a)
#print(b)

Provincias=['Santa Fe','Jujuy','Entre Rios']
Poblaciones=[54,19,30] 
Diccionario={'Provincias':Provincias,'Poblacion':Poblaciones}

a=pd.DataFrame(Diccionario)

#print(a)

grupos_mundial=pd.read_csv('Fifa_Worldcup_2022_Groups.csv')

grupos_mundial['Puntos']=0

print(grupos_mundial.columns)

print(grupos_mundial[['Country_Name_Short','Puntos']])