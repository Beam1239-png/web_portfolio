import asyncio

import flet as ft

from pages.home import home_page
from pages.about import about_page
from pages.timeline import timeline_page
from pages.github_evidence import github_page
from pages.blog import blog_page
from pages.matlab import matlab_page
from pages.contact import contact_page


def main(page: ft.Page):
    page.title = "Mr Kambonde's Portfolio"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#0F172A"
    page.padding = 0
    page.window_width = 1400
    page.scroll = None

    page_content = ft.Column(
        expand=True,
        scroll=ft.ScrollMode.AUTO,
        spacing=20
    )

    content = ft.Container(
        expand=True,
        padding=30,
        content=page_content
    )

    # page cache to avoid regenerating pages on every navigation
    page_cache = {}

    page_factories = {
        "/": home_page,
        "/about": about_page,
        "/timeline": timeline_page,
        "/github": github_page,
        "/blog": blog_page,
        "/matlab": matlab_page,
        "/contact": contact_page,
    }

    sidebar_open_width = 268
    sidebar_slide = ft.Animation(280, ft.AnimationCurve.EASE_IN_OUT)
    sidebar_nav_items = []

    def side_border(color="#20364D", left_color=None, left_width=1):
        return ft.Border(
            left=ft.BorderSide(left_width, left_color or color),
            right=ft.BorderSide(1, color),
            top=ft.BorderSide(1, color),
            bottom=ft.BorderSide(1, color),
        )

    def get_or_create_page(route):
        if route not in page_cache:
            page_factory = page_factories.get(route, home_page)
            page_cache[route] = page_factory()
        return page_cache[route]

    def change_page(route):
        page_content.controls = [get_or_create_page(page.route)]
        refresh_sidebar_nav()
        page_content.update()

    page.on_route_change = change_page

    def refresh_sidebar_nav(active_route=None):
        current_route = active_route or page.route or "/"
        for item in sidebar_nav_items:
            active = current_route == item["route"]
            item["container"].bgcolor = "#E5EEF8" if active else "#081524"
            item["container"].border = side_border("#E5EEF8" if active else "#1D334B", item["accent"], 4)
            item["indicator"].bgcolor = item["accent"] if active else "#20364D"
            item["icon_box"].bgcolor = item["accent"] if active else "#0F1E2D"
            item["icon"].color = "#07111F" if active else item["accent"]
            item["code"].color = "#07111F" if active else item["accent"]
            item["label"].color = "#07111F" if active else "#E5EEF8"
            item["chevron"].color = "#07111F" if active else "#8DA2B8"

    def select_nav(route):
        refresh_sidebar_nav(route)
        page.update()
        page.go(route)

    def nav_item(icon, label, route, accent="#48F838", code="00"):
        active = (page.route or "/") == route
        indicator = ft.Container(width=5, height=34, border_radius=3, bgcolor=accent if active else "#20364D")
        nav_icon = ft.Icon(icon, size=18, color="#07111F" if active else accent)
        icon_box = ft.Container(
            width=34,
            height=34,
            border_radius=8,
            bgcolor=accent if active else "#0F1E2D",
            border=side_border(accent),
            alignment=ft.Alignment(0, 0),
            content=nav_icon,
        )
        code_text = ft.Text(code, size=10, color="#07111F" if active else accent, weight=ft.FontWeight.BOLD)
        label_text = ft.Text(label, size=13, color="#07111F" if active else "#E5EEF8", weight=ft.FontWeight.BOLD, expand=True)
        chevron = ft.Icon(ft.Icons.CHEVRON_RIGHT, size=16, color="#07111F" if active else "#8DA2B8")
        container = ft.Container(
            height=54,
            border_radius=8,
            ink=True,
            on_click=lambda e, target=route: select_nav(target),
            padding=ft.Padding(8, 0, 9, 0),
            bgcolor="#E5EEF8" if active else "#081524",
            border=side_border("#E5EEF8" if active else "#1D334B", accent, 4),
            content=ft.Row(
                [
                    indicator,
                    icon_box,
                    ft.Column([code_text, label_text], spacing=0, expand=True),
                    chevron,
                ],
                spacing=9,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )
        sidebar_nav_items.append(
            {
                "route": route,
                "accent": accent,
                "container": container,
                "indicator": indicator,
                "icon_box": icon_box,
                "icon": nav_icon,
                "code": code_text,
                "label": label_text,
                "chevron": chevron,
            }
        )
        return container

    sidebar_panel = ft.Container(
        width=sidebar_open_width,
        bgcolor="#020814",
        padding=12,
        expand=False,
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
        offset=ft.Offset(0, 0),
        animate_size=sidebar_slide,
        animate_opacity=sidebar_slide,
        animate_offset=sidebar_slide,
        content=ft.Stack(
            [
                ft.Column(
                    [
                        ft.Container(
                            bgcolor="#06101D",
                            border_radius=8,
                            padding=14,
                            border=side_border("#1D334B", "#48F838", 4),
                            content=ft.Column(
                                [
                                    ft.Row(
                                        [
                                            ft.Container(
                                                width=48,
                                                height=48,
                                                bgcolor="#E5EEF8",
                                                border_radius=8,
                                                border=side_border("#48F838"),
                                                alignment=ft.Alignment(0, 0),
                                                content=ft.Icon(ft.Icons.ENGINEERING, size=27, color="#07111F"),
                                            ),
                                            ft.Column(
                                                [
                                                    ft.Text("LK", size=11, color="#48F838", weight=ft.FontWeight.BOLD),
                                                    ft.Text("Portfolio", size=19, weight=ft.FontWeight.BOLD, color="#E5EEF8"),
                                                    ft.Text("Navigation OS", size=11, color="#8DA2B8"),
                                                ],
                                                spacing=0,
                                                expand=True,
                                            ),
                                        ],
                                        spacing=11,
                                    ),
                                    ft.Container(
                                        padding=ft.Padding(10, 7, 10, 7),
                                        bgcolor="#020814",
                                        border_radius=8,
                                        border=side_border("#20364D", "#38BDF8", 3),
                                        content=ft.Row(
                                            [
                                                ft.Icon(ft.Icons.RADAR, size=15, color="#38BDF8"),
                                                ft.Text("ROUTE CONTROL", size=10, color="#E5EEF8", weight=ft.FontWeight.BOLD),
                                                ft.Container(expand=True),
                                                ft.Container(width=8, height=8, bgcolor="#48F838", border_radius=4),
                                            ],
                                            spacing=7,
                                        ),
                                    ),
                                ],
                                spacing=12,
                            ),
                        ),
                        ft.Row(
                            [
                                ft.Text("INDEX", size=10, color="#48F838", weight=ft.FontWeight.BOLD),
                                ft.Container(expand=True),
                                ft.Text("07 ROUTES", size=10, color="#8DA2B8", weight=ft.FontWeight.BOLD),
                            ],
                        ),
                        nav_item(ft.Icons.HOME, "Home", "/", "#48F838", "01"),
                        nav_item(ft.Icons.PERSON, "About", "/about", "#38BDF8", "02"),
                        nav_item(ft.Icons.TIMELINE, "Timeline", "/timeline", "#8B5CF6", "03"),
                        nav_item(ft.Icons.CODE, "GitHub Evidence", "/github", "#F59E0B", "04"),
                        nav_item(ft.Icons.ARTICLE, "Technical Blog", "/blog", "#EC4899", "05"),
                        nav_item(ft.Icons.SCHOOL, "MATLAB Hub", "/matlab", "#10B981", "06"),
                        nav_item(ft.Icons.EMAIL, "Contact", "/contact", "#EF4444", "07"),
                        ft.Container(expand=True),
                    ],
                    spacing=10,
                    expand=True,
                ),
            ],
        ),
    )
    sidebar = ft.Container(
        width=sidebar_open_width,
        expand=False,
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
        animate_size=sidebar_slide,
        content=sidebar_panel,
    )

    sidebar_is_open = True

    async def toggle_sidebar(e):
        nonlocal sidebar_is_open

        sidebar_is_open = not sidebar_is_open
        if sidebar_is_open:
            sidebar.width = sidebar_open_width
            sidebar_panel.offset = ft.Offset(-1, 0)
            sidebar_panel.opacity = 0
            page.update()
            await asyncio.sleep(0.02)
            sidebar_panel.offset = ft.Offset(0, 0)
            sidebar_panel.opacity = 1
        else:
            sidebar_panel.offset = ft.Offset(-1, 0)
            sidebar_panel.opacity = 0
            page.update()
            await asyncio.sleep(0.28)
            if not sidebar_is_open:
                sidebar.width = 0
        page.update()

    # header with toggle button
    header = ft.Container(
        height=60,
        bgcolor="#0F172A",
        padding=10,
        content=ft.Row([
            ft.IconButton(
                ft.Icons.MENU,
                icon_size=28,
                on_click=toggle_sidebar,
                tooltip="Toggle Sidebar"
            ),
            ft.Text("Engineering Portfolio", size=20, weight=ft.FontWeight.BOLD),
        ], alignment=ft.MainAxisAlignment.START, vertical_alignment=ft.CrossAxisAlignment.CENTER)
    )

    # main layout with collapsible sidebar
    main_row = ft.Row(
        [
            sidebar,
            content
        ],
        expand=True
    )

    page.add(
        header,
        main_row
    )

    page_content.controls = [get_or_create_page(page.route or "/")]
    page.update()


ft.run(main)
