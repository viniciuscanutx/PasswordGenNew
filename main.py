import flet as ft 
import random 
import string
import db.queries
import functions.functions

def main(page: ft.Page):
    
    page.title="Password Generator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.spacing = 20
    page.window_width = 330
    page.window_height = 600
    
    logged_in_email = None
    password_length_dropdown = ft.Ref[ft.Dropdown]()
    password_source_input = ft.Ref[ft.TextField]()


ft.app(target=main)
