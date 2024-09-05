import os
diretorioInformado = input("Informe o diretório: ")

os.getcwd()

separador = r'\\'

os.chdir(diretorioInformado.replace(separador,"/"))

arrFiles = os.listdir()

def criaPastas():
    for i in range(len(arrFiles)):
        
        findFormat = arrFiles[i].rsplit(".",1)
        checkFormat = os.path.isfile(arrFiles[i])
        checkNone = len(findFormat)

        if(checkNone > 1 and checkFormat ==True ):
            if(findFormat[1] != "py"):
                os.makedirs(findFormat[1],0o666 , True)
                os.rename(arrFiles[i], "{}/{}".format(findFormat[1],arrFiles[i]))    
            
criaPastas()