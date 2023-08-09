import tkinter as tk
from tkinter import ttk
import random
import smtplib
import ssl
from email.message import EmailMessage

entry_correo = None
entry_contrasena = None
entry_codigo_verificacion = None
codigo_verificacion = None

def enviar_codigo_verificacion():
    global entry_correo, entry_contrasena, entry_codigo_verificacion, codigo_verificacion

   
    correo = entry_correo.get()

 
    if not correo or '@' not in correo:
        lbl_resultado.config(text="Ingresa un correo válido", fg="red")
        return

    
    codigo_verificacion = random.randint(100000, 999999)

  
    email_sender = 'bautistadaveloze@gmail.com'
    email_password = "gpvynfczlqtwgyuf"
    email_receiver = correo
    subject = 'Verifica Tu Correo'
    body = f"Gracias por registrarte.\nTu código de verificación es {codigo_verificacion}"

   
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

   
    context = ssl.create_default_context()

    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

  
    lbl_correo.destroy()
    entry_correo.destroy()
    lbl_contrasena.destroy()
    entry_contrasena.destroy()
    boton_enviar.destroy()

    
    lbl_resultado.config(text="Enviamos un código de verificación a tu mail")
    lbl_resultado2 = ttk.Label(ventana, text="Compruébalo y escríbelo aquí:", font=font_estetico, foreground="white", background="black")
    lbl_resultado2.place(x=200, y=400)

   
    global entry_codigo_verificacion
    entry_codigo_verificacion = ttk.Entry(ventana, font=font_estetico)
    entry_codigo_verificacion.place(x=500, y=600)

   
    boton_verificar = tk.Button(
        ventana,
        text="Verificar",
        font=font_estetico,
        padx=30,
        pady=20,
        bg="#2ecc71",
        fg="white",
        relief=tk.RAISED,
        command=verificar_codigo
    )
    boton_verificar.place(x=450, y=600)

def verificar_codigo():
    global entry_codigo_verificacion, codigo_verificacion

    codigo_ingresado = entry_codigo_verificacion.get()
    if codigo_ingresado == str(codigo_verificacion):
        # Cerrar la ventana después de 3 segundos
        lbl_resultado.config(text="¡Código de verificación correcto!", fg="green")
        ventana.after(3000, lambda: ventana.destroy())
    else:
        entry_codigo_verificacion.delete(0, tk.END)  # Borrar el contenido del campo de texto
        lbl_resultado.config(text="Código de verificación incorrecto", fg="red")

def mostrar_campos():
    global entry_correo, entry_contrasena, boton_enviar, lbl_correo, lbl_contrasena

   
    registro.destroy()
    lbl_logo.destroy()

   
    lbl_correo = ttk.Label(ventana, text="Correo Electrónico:", font=font_estetico)
    lbl_correo.place(x=200, y=200)
    entry_correo = ttk.Entry(ventana, font=font_estetico)
    entry_correo.place(x=500, y=200)

    lbl_contrasena = ttk.Label(ventana, text="Contraseña:", font=font_estetico)
    lbl_contrasena.place(x=305, y=250)
    entry_contrasena = ttk.Entry(ventana, font=font_estetico, show="*")
    entry_contrasena.place(x=500, y=250)

   
    boton_enviar = tk.Button(
        ventana,
        text="Enviar",
        font=font_estetico,
        padx=30,
        pady=20,
        bg="#3498db",
        fg="white",
        relief=tk.RAISED,
        command=enviar_codigo_verificacion
    )
    boton_enviar.place(x=450, y=350)


ventana = tk.Tk()
ventana.geometry("1000x700")
ventana.title("BetSoccer")
ventana.configure(bg="black")


font_estetico = ("Arial", 20, "bold")


registro = tk.Button(
    ventana,
    text="Registrarse",
    font=font_estetico,
    padx=30,
    pady=20,
    bg="#3498db",
    fg="white",
    relief=tk.RAISED,
    command=mostrar_campos
)
registro.place(x=375, y=300)


logo = tk.PhotoImage(file="../venv/Logo.png")
lbl_logo = tk.Label(ventana, image=logo, borderwidth=0)
lbl_logo.place(x=300, y=50)



lbl_resultado = ttk.Label(ventana, text="", font=font_estetico, foreground="white", background="black")
lbl_resultado.place(x=200, y=350)


ventana.mainloop()

