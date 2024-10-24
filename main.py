import flet as ft
import random
import string
from db.queries import auth_user, get_user, reg_user, create_password, get_passwords, delete_passwords
from functions.functions import new_pass

def main(page: ft.Page):
    
    page.title = "Password Generator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.spacing = 20
    page.window_width = 330
    page.window_height = 600
    
    logged_in_email = None
    password_length_dropdown = ft.Ref[ft.Dropdown]()
    password_source_input = ft.Ref[ft.TextField]()

    def show_snackbar(message, color):
        page.snack_bar = ft.SnackBar(
            content=ft.Text(value=message),
            bgcolor=color,
            action="OK",
            duration=3000
        )
        page.snack_bar.open = True
        page.update()
        
    def on_login_click(e):
        email = email_input.value
        password = password_input.value
        if auth_user(email, password):
            show_snackbar('Successfully logged in!', "green")
            nonlocal logged_in_email
            logged_in_email = email
            page.go("/welcome")
        else:
            show_snackbar('Invalid email or password!', "red")

    def on_register_click(e):
        email = email_input.value
        password = password_input.value
        if get_user(email):
            show_snackbar('User already exists!', "red")
        else:
            try:
                reg_user(email, password)
                show_snackbar('User registered successfully!', "green")
                email_input.value = ""
                password_input.value = ""
                page.update()
            except Exception as ex:
                show_snackbar('Error registering user!', "red")

    def copy_to_clipboard(text):
        page.set_clipboard(text)
        show_snackbar('Password copied to clipboard!', "blue")

    def create_password_list(email):
        passwords = get_passwords(email)
        password_controls = []

        for password_record in passwords:
            id, _, password, source = password_record
            password_controls.append(
                ft.Row(
                    controls=[
                        ft.Text(f"{source}: {password}"),
                        ft.IconButton(
                            icon=ft.icons.COPY,
                            tooltip="Copy password",
                            on_click=lambda _, p=password: copy_to_clipboard(p)
                        ),
                        ft.IconButton(
                            icon=ft.icons.DELETE,
                            tooltip="Delete password",
                            on_click=lambda _, i=id: delete_password_callback(i, email)
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    spacing=10
                )
            )
        return password_controls
    
    def list_passwords(email):
        passwords = get_passwords(email)
        list_controls = []

        for password_record in passwords:
            id, _, password, source = password_record
            list_controls.append(
                ft.Row(
                    controls=[
                        ft.Text(f"{source}: {password}"),
                        ft.IconButton(
                            icon=ft.icons.COPY,
                            tooltip="Copy password",
                            on_click=lambda _, p=password: copy_to_clipboard(p)
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    spacing=10
                )
            )
        return list_controls

    def welcome_message(email):
        list_controls = list_passwords(email)
        
        content = ft.Column(
            controls=[
                ft.Text(f"Welcome, {email}!", size=24),
                ft.Divider(),
                ft.Text("Your passwords:", size=20),
                *list_controls,
                ft.Divider(),
                ft.ElevatedButton(text="Manage Passwords", on_click=lambda _: page.go("/manage")),
                ft.ElevatedButton(text="Logout", on_click=lambda _: logout()),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10
        )
        return content

    def password_management(email):
        password_controls = create_password_list(email)

        content = ft.Column(
            controls=[
                ft.Text("Manage Passwords", size=20),
                *password_controls,
                ft.Divider(),
                ft.Text("Add New Password", size=16),
                ft.TextField(
                    label="Password Source (e.g., Amazon, Twitch, Google)",
                    width=300,
                    ref=password_source_input
                ),
                ft.Dropdown(
                    label="Password Length",
                    width=300,
                    options=[
                        ft.dropdown.Option("6"),
                        ft.dropdown.Option("12"),
                        ft.dropdown.Option("24")
                    ],
                    ref=password_length_dropdown
                ),
                ft.ElevatedButton(text="Add Password", on_click=lambda _: generate_and_add_password(email)),
                ft.ElevatedButton(text="Back", on_click=lambda _: page.go("/welcome"))
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10
        )
        return content

    def generate_and_add_password(email):
        try:
            size = int(password_length_dropdown.current.value)
            source = password_source_input.current.value
            if not source:
                raise ValueError("Please specify the password source.")
            new_password = new_pass(size)
            create_password(email, new_password, source)
            show_snackbar(f'{size}-character password added for {source} successfully!', "green")
            password_source_input.current.value = ""  
            update_current_view(email)
        except ValueError as e:
            show_snackbar(str(e), "red")

    def delete_password_callback(id, email):
        delete_passwords(id)
        show_snackbar('Password deleted successfully!', "green")
        update_current_view(email)

    def update_current_view(email):
        if page.route == "/welcome":
            page.views[-1].controls = [welcome_message(email)]
        elif page.route == "/manage":
            page.views[-1].controls = [password_management(email)]
        page.update()

    def logout():
        nonlocal logged_in_email
        logged_in_email = None
        page.go("/")

    def login_page():
        return ft.Column(
            controls=[
                email_input,
                password_input,
                ft.Divider(),
                login_button,
                register_button
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10
        )

    email_input = ft.TextField(label="Email", width=300)
    password_input = ft.TextField(label="Password", password=True, can_reveal_password=True, width=300)
    login_button = ft.ElevatedButton(text="Login", on_click=on_login_click)
    register_button = ft.ElevatedButton(text="Register", on_click=on_register_click)

    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(
                ft.View(
                    "/",
                    [login_page()]
                )
            )
        elif page.route == "/welcome" and logged_in_email:
            page.views.append(
                ft.View(
                    "/welcome",
                    [welcome_message(logged_in_email)]
                )
            )
        elif page.route == "/manage" and logged_in_email:
            page.views.append(
                ft.View(
                    "/manage",
                    [password_management(logged_in_email)]
                )
            )
        page.update()

    page.on_route_change = route_change
    page.go("/")

ft.app(target=main)
