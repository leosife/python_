class MyOpen():
    def __init__(self,caminhoarquivo,modo):
        self.caminhoarquivo = caminhoarquivo
        self._arquivo = None
        self.modo = modo

        ...
    def __enter__(self):
        print('Abrindo Arquivo')
        self._arquivo = open(self.caminhoarquivo, self.modo, encoding='utf8')
    
        return self._arquivo
        ...
    def __exit__(self,class_exception,exception_,traceback_):
        print('Fechando')
        self._arquivo.close()
        # print(class_exception)
        # # print(exception_)
        # # print(traceback_)
        # return True


caminho = 'C:\\Users\\leo_s\\OneDrive\\Documentos\\projeto\\python_\\leo\\orientado_obj\\a240.txt'
with MyOpen(caminho,'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    print('Ola')