import re

import flet as ft


TEXT = "#E5EEF8"
MUTED = "#8DA2B8"
PANEL = "#07111F"
PANEL_2 = "#0D1B2A"
BORDER = "#20364D"
GREEN = "#48F838"
BLUE = "#38BDF8"
PURPLE = "#8B5CF6"
AMBER = "#F59E0B"
PINK = "#EC4899"
RED = "#EF4444"

EMAIL_ADDRESS = "lehabeamk@gmail.com"
GITHUB_URL = "https://github.com/Pehovelo/UNAM-I3691CP-QuoteWise-development-team--QuoteWise"
LINKEDIN_URL = "https://linkedin.com/in/lehabeam-kambonde/"


def contact_page():
    def outline_border(color=BORDER, left_color=None):
        return ft.Border(
            left=ft.BorderSide(3, left_color or color),
            right=ft.BorderSide(1, color),
            top=ft.BorderSide(1, color),
            bottom=ft.BorderSide(1, color),
        )

    def border_all(color):
        return ft.Border(
            left=ft.BorderSide(1, color),
            right=ft.BorderSide(1, color),
            top=ft.BorderSide(1, color),
            bottom=ft.BorderSide(1, color),
        )

    def pill(icon, label, color):
        return ft.Container(
            padding=ft.Padding(10, 6, 10, 6),
            border_radius=8,
            bgcolor="#0F1E2D",
            border=border_all(color),
            content=ft.Row(
                [
                    ft.Icon(icon, size=14, color=color),
                    ft.Text(label, size=11, color=TEXT, weight=ft.FontWeight.BOLD),
                ],
                spacing=6,
                tight=True,
            ),
        )

    def show_snack(page, message, color=BLUE):
        page.snack_bar = ft.SnackBar(
            content=ft.Row(
                [
                    ft.Icon(ft.Icons.INFO, size=18, color=color),
                    ft.Text(message, color=TEXT),
                ],
                spacing=10,
            ),
            bgcolor=PANEL,
        )
        page.snack_bar.open = True
        page.update()

    def field(label, icon, hint="", multiline=False):
        return ft.TextField(
            label=label,
            hint_text=hint,
            icon=icon,
            multiline=multiline,
            min_lines=5 if multiline else None,
            max_lines=9 if multiline else None,
            bgcolor="#07111F",
            color=TEXT,
            cursor_color=GREEN,
            border_color=BORDER,
            focused_border_color=GREEN,
            label_style=ft.TextStyle(color=MUTED),
            hint_style=ft.TextStyle(color="#50647A"),
        )

    name = field("Name", ft.Icons.PERSON, "Your full name")
    email = field("Email", ft.Icons.EMAIL, "name@example.com")
    subject = field("Subject", ft.Icons.SUBJECT, "Project, coursework, collaboration...")
    message = field("Message", ft.Icons.CHAT, "Tell me what you want to build or discuss.", True)

    form_status = ft.Container(
        padding=ft.Padding(12, 9, 12, 9),
        border_radius=8,
        bgcolor="#07111F",
        border=outline_border(BORDER, BLUE),
        content=ft.Row(
            [
                ft.Icon(ft.Icons.RADAR, size=18, color=BLUE),
                ft.Text("Ready to receive a message", size=12, color=MUTED, expand=True),
            ],
            spacing=10,
        ),
    )

    def set_status(text, color, icon=ft.Icons.INFO):
        form_status.border = outline_border(BORDER, color)
        form_status.content.controls[0].name = icon
        form_status.content.controls[0].color = color
        form_status.content.controls[1].value = text
        form_status.content.controls[1].color = TEXT if color == GREEN else MUTED

    def submit(e: ft.ControlEvent):
        errors = []
        clean_name = (name.value or "").strip()
        clean_email = (email.value or "").strip()
        clean_subject = (subject.value or "").strip()
        clean_message = (message.value or "").strip()

        if len(clean_name) < 2:
            errors.append("name")
        if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", clean_email):
            errors.append("email")
        if len(clean_subject) < 4:
            errors.append("subject")
        if len(clean_message) < 10:
            errors.append("message")

        if errors:
            set_status("Check " + ", ".join(errors) + " before sending.", RED, ft.Icons.ERROR)
            form_status.update()
            show_snack(e.page, "Please complete the highlighted contact details.", RED)
            return

        set_status("Message validated and queued locally.", GREEN, ft.Icons.CHECK_CIRCLE)
        for control in (name, email, subject, message):
            control.value = ""
        e.page.update()
        show_snack(e.page, "Message ready. Use Email Me for a real email send.", GREEN)

    def action_button(label, icon, color, url=None, on_click=None):
        return ft.Container(
            height=44,
            padding=ft.Padding(14, 0, 14, 0),
            border_radius=8,
            bgcolor="#10263A",
            border=border_all(color),
            ink=True,
            url=url,
            on_click=on_click,
            content=ft.Row(
                [
                    ft.Icon(icon, size=18, color=color),
                    ft.Text(label, size=12, color=TEXT, weight=ft.FontWeight.BOLD),
                ],
                spacing=8,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        )

    def contact_channel(title, value, icon, color, action, url):
        return ft.Container(
            padding=16,
            border_radius=8,
            bgcolor=PANEL,
            border=outline_border(BORDER, color),
            content=ft.Row(
                [
                    ft.Container(
                        width=44,
                        height=44,
                        border_radius=8,
                        bgcolor="#0F1E2D",
                        border=border_all(color),
                        alignment=ft.Alignment(0, 0),
                        content=ft.Icon(icon, size=22, color=color),
                    ),
                    ft.Column(
                        [
                            ft.Text(title, size=14, color=TEXT, weight=ft.FontWeight.BOLD),
                            ft.Text(value, size=11, color=MUTED),
                        ],
                        spacing=3,
                        expand=True,
                    ),
                    action_button(action, ft.Icons.ARROW_OUTWARD, color, url=url),
                ],
                spacing=12,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

    def route_step(number, title, description, color):
        return ft.Container(
            padding=12,
            border_radius=8,
            bgcolor="#07111F",
            border=outline_border(BORDER, color),
            content=ft.Row(
                [
                    ft.Container(
                        width=34,
                        height=34,
                        border_radius=8,
                        bgcolor="#0F1E2D",
                        alignment=ft.Alignment(0, 0),
                        content=ft.Text(number, size=13, color=color, weight=ft.FontWeight.BOLD),
                    ),
                    ft.Column(
                        [
                            ft.Text(title, size=13, color=TEXT, weight=ft.FontWeight.BOLD),
                            ft.Text(description, size=11, color=MUTED),
                        ],
                        spacing=2,
                        expand=True,
                    ),
                ],
                spacing=10,
            ),
        )

    header = ft.Container(
        padding=22,
        border_radius=8,
        bgcolor=PANEL_2,
        border=outline_border(BORDER, GREEN),
        content=ft.Column(
            [
                ft.Row(
                    [
                        pill(ft.Icons.MAIL, "CONTACT SYSTEM", GREEN),
                        pill(ft.Icons.SCHEDULE, "RESPONSE READY", BLUE),
                        pill(ft.Icons.CODE, "PROJECT DISCUSSION", AMBER),
                    ],
                    wrap=True,
                    spacing=8,
                    run_spacing=8,
                ),
                ft.Text("Contact", size=38, color=TEXT, weight=ft.FontWeight.BOLD),
                ft.Text(
                    "Reach out for coursework discussions, project feedback, engineering ideas, or collaboration opportunities.",
                    size=14,
                    color=MUTED,
                ),
            ],
            spacing=12,
        ),
    )

    form_panel = ft.Container(
        col={"sm": 12, "lg": 7},
        padding=20,
        border_radius=8,
        bgcolor=PANEL_2,
        border=outline_border(BORDER, BLUE),
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Icon(ft.Icons.EDIT_NOTE, size=24, color=BLUE),
                        ft.Text("Message Console", size=20, color=TEXT, weight=ft.FontWeight.BOLD),
                    ],
                    spacing=10,
                ),
                form_status,
                name,
                email,
                subject,
                message,
                ft.Row(
                    [
                        action_button("Validate Message", ft.Icons.SEND, GREEN, on_click=submit),
                        action_button("Email Me", ft.Icons.EMAIL, AMBER, url=f"mailto:{EMAIL_ADDRESS}"),
                    ],
                    wrap=True,
                    spacing=10,
                    run_spacing=10,
                ),
            ],
            spacing=13,
        ),
    )

    channels_panel = ft.Container(
        col={"sm": 12, "lg": 5},
        padding=20,
        border_radius=8,
        bgcolor=PANEL_2,
        border=outline_border(BORDER, PURPLE),
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Icon(ft.Icons.CONNECT_WITHOUT_CONTACT, size=24, color=PURPLE),
                        ft.Text("Direct Channels", size=20, color=TEXT, weight=ft.FontWeight.BOLD),
                    ],
                    spacing=10,
                ),
                contact_channel("Email", EMAIL_ADDRESS, ft.Icons.EMAIL, GREEN, "Send", f"mailto:{EMAIL_ADDRESS}"),
                contact_channel("GitHub", "QuoteWise development repository", ft.Icons.CODE, AMBER, "View", GITHUB_URL),
                contact_channel("LinkedIn", "linkedin.com/in/lehabeam-kambonde", ft.Icons.WORK, BLUE, "Open", LINKEDIN_URL),
                ft.Container(
                    padding=16,
                    border_radius=8,
                    bgcolor=PANEL,
                    border=outline_border(BORDER, PINK),
                    content=ft.Column(
                        [
                            ft.Row(
                                [
                                    ft.Icon(ft.Icons.LOCATION_ON, size=20, color=PINK),
                                    ft.Text("Location Signal", size=15, color=TEXT, weight=ft.FontWeight.BOLD),
                                ],
                                spacing=8,
                            ),
                            ft.Text(
                                "Available for academic, portfolio, and software engineering conversations.",
                                size=12,
                                color=MUTED,
                            ),
                            ft.Row(
                                [
                                    pill(ft.Icons.PUBLIC, "Remote", BLUE),
                                    pill(ft.Icons.SCHOOL, "Student", GREEN),
                                ],
                                wrap=True,
                                spacing=8,
                                run_spacing=8,
                            ),
                        ],
                        spacing=10,
                    ),
                ),
            ],
            spacing=12,
        ),
    )

    workflow = ft.ResponsiveRow(
        [
            ft.Container(
                col={"sm": 12, "md": 4},
                content=route_step("01", "Introduce", "Share who you are and what you need.", GREEN),
            ),
            ft.Container(
                col={"sm": 12, "md": 4},
                content=route_step("02", "Context", "Add project, coursework, or repository details.", BLUE),
            ),
            ft.Container(
                col={"sm": 12, "md": 4},
                content=route_step("03", "Follow Up", "Use email or LinkedIn for a real send.", AMBER),
            ),
        ],
        spacing=12,
        run_spacing=12,
    )

    return ft.Container(
        padding=20,
        content=ft.Column(
            [
                header,
                ft.ResponsiveRow([form_panel, channels_panel], spacing=14, run_spacing=14),
                workflow,
            ],
            spacing=16,
        ),
    )
