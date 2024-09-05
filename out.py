import os

diretorioInformado = input("Informe o diretório: ")

os.getcwd()

separador = r'\\'

os.chdir(diretorioInformado.replace(separador,"/"))

currentDir = os.getcwd()

arrDir = os.listdir()

def deleteDir():
    for i in range(len(arrDir)):
        checkDir = os.path.isdir(arrDir[i])
        if(checkDir == True):
            os.rmdir(arrDir[i])

def outDir(currentDir):
    for i in range(len(arrDir)):
        checkDir = os.path.isdir(arrDir[i])
        if( checkDir == True): 
            os.chdir(arrDir[i])
            arrFiles = os.listdir()
            for i in range(len(arrFiles)):
                os.rename(arrFiles[i], "{}/{}".format(currentDir,arrFiles[i]))

        os.chdir(currentDir)
    
    deleteDir()



outDir(currentDir)