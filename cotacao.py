import urllib.request
import tkinter 

def pegarcotação():
    try:
        req = urllib.request.urlopen("https://dolarhoje.com/")
        texto = req.read().decode("utf8")
        valor=texto[texto.find('id="nacional"')+21:texto.find('id="nacional"')+25]
        return valor 

    except:
        print("Erro. Verifique sua conexão com a internet.")

programa = tkinter.Tk()
programa.title("Pegar cotação do dolar")
valordodolar = tkinter.Label(programa, text='', font=('Arial', 50))
texto1 = tkinter.Label(programa, text="Valor:", font=('Arial', 50))
texto1.pack()
valordodolar.pack()
valordodolar.configure(text=pegarcotação())

programa.mainloop()




