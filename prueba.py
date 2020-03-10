import numpy as np
data = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[13,14,15,16,17,18],[13,14,15,16,17,18]])
data2 = np.array([1,2,3,4,5,6,7,8,9])
#print(data2)

binaryFile = open("imagen2.dat", mode='rb')#Abrimos el archivo en modo binario
dataa = np.fromfile(binaryFile, dtype='d') # reads the whole file
print("Longitud: ",len(dataa))
print("Dimension: ",data.shape[1])

def girar(data):
	turn=False
	aux = np.empty((3))
	for i in range(3):
		if(turn==True):
			for k in range(3):
				aux[k]=data[i][k]
			for l in range(3):
				data[i][l]=aux[-(l+1)]
		turn=not(turn)
		
def right(dataDesf,numElm):
    dataAux = np.empty(numElm)
    for i in range(numElm):
        if(i==(numElm-1)):
            dataAux[i]=dataDesf[0]
        else:
            dataAux[i]=dataDesf[i+1]
    return dataAux
    
def left(dataDesf,numElm):
    dataAux = np.empty(numElm)
    for i in range(numElm):
        if(i==0):
            dataAux[0]=dataDesf[numElm-1]
        else:
            dataAux[i]=dataDesf[i-1]
    return dataAux
    
def fase(numFase,dataDesf):
    numElm=len(dataDesf)
    for j in range(numFase):
        dataDesf=left(dataDesf,numElm)
    return dataDesf
    
def acoplar(numAcoplo,data):
    acoplo=True
    for i in range(3):
        if(acoplo==True):
            data[i,:]=fase(numAcoplo,data[i,:])
        acoplo=not(acoplo)
    return data
    
def recortar(data,numRecorte):
    print(data)
    columna=5-(np.arange(0,numRecorte))
    print(columna)
    matrixR=np.delete(data, columna, axis=1)
    return matrixR
    
#dataCouple=acoplar(2,data)
dataElim=recortar(data,2)
print(dataElim)