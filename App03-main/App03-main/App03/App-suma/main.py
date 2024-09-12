import flet as ft

def result(text_field,text_field2,page):
    text=float(text_field.value.strip())
    text2=float(text_field2.value.strip())
    r=text + text2
    dialog=ft.AlertDialog(
        title=ft.Text("Resultado"),
        content=ft.Text(f"El resultado es: {r}"),
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
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    img=ft.Image(src="meme.jpeg",width=200,height=200)
    text_field=ft.TextField(label="primer numero")
    text_field2=ft.TextField(label="segundo numero")
    btn=ft.ElevatedButton(
        "suma",
        on_click=lambda e: result(text_field,text_field2,page)
        )
    def limpiar(e):
        text_field.value=""
        text_field2.value=""
        page.update()

    btn_2=ft.ElevatedButton(
        text="Limpiar",
        on_click=lambda e: limpiar(e)
    )
    page.add(
        ft.Column( 
            [
                img,
                    
                ft.Row(controls=
                    [text_field,
                    text_field2],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(controls=[
                    btn,btn_2],
                       alignment=ft.MainAxisAlignment.CENTER
                       ),
                ],
            alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )
    
        
    
    
    


ft.app(main)
