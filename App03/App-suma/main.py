import flet as ft

def result(text_field,text_field2,page):
    text=float(text_field.value.strip())
    text2=float(text_field2.value.sprint())
    dialog=ft.AlertDialog(
        title=ft.Text("Resultado"),
        content=ft.Text(f"El resultado es: {text + text2}"),
        actions=[
            ft.TextButton("Salir", on_click=lambda e: clouse_dialog(page))
        ],
    )
    page.dialog= dialog
    page.dialog.open=True
    page.update()
    
def clouse_dialog(page):
    page.dialog.open=False
    page.update()
    

def main(page: ft.Page):
    page.title="Calculador"
    page.bgcolor="blue"
    img=ft.Image(src="descarga.jpg",width=200,helght=200)
    text_field=ft.TextField(label="primer numero")
    text_field2=ft.TextField(label="segundo numero")
    button=ft.ElevatedButton(
        text="suma",
        
    )
    button_2=ft.ElevatedButton(
        text="Limpiar"
    )
    


ft.app(main)
