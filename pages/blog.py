import json
from pathlib import Path

import flet as ft


SURFACE = "#07111F"
PANEL = "#0D1B2A"
PANEL_ALT = "#10263A"
TEXT = "#E5EEF8"
MUTED = "#8DA2B8"
BORDER = "#20364D"

ICON_MAP = {
    "CODE": ft.Icons.CODE,
    "STORAGE": ft.Icons.STORAGE,
    "PSYCHOLOGY": ft.Icons.PSYCHOLOGY,
    "PUBLIC": ft.Icons.PUBLIC,
    "TUNE": ft.Icons.TUNE,
    "FLASH_ON": ft.Icons.FLASH_ON,
    "ARTICLE": ft.Icons.ARTICLE,
}

META_MAP = {
    "Python Functions & Optimization": {
        "level": "Systems",
        "read": "6 min",
        "signal": "Reusable logic",
        "tags": ["Python", "Profiling", "Clean APIs"],
    },
    "Data Structures & Complexity": {
        "level": "Core CS",
        "read": "8 min",
        "signal": "Runtime analysis",
        "tags": ["Big-O", "Sorting", "Memory"],
    },
    "Machine Learning Basics": {
        "level": "AI",
        "read": "7 min",
        "signal": "Model training",
        "tags": ["Loss", "Features", "Generalization"],
    },
    "Web Development Principles": {
        "level": "Full Stack",
        "read": "5 min",
        "signal": "Latency budget",
        "tags": ["Backend", "Frontend", "Performance"],
    },
    "Control Systems & Feedback": {
        "level": "Engineering",
        "read": "9 min",
        "signal": "Closed-loop control",
        "tags": ["PID", "Signals", "Stability"],
    },
    "Concurrent Programming": {
        "level": "Advanced",
        "read": "7 min",
        "signal": "Parallel speedup",
        "tags": ["Async", "Threads", "Scaling"],
    },
}

DEFAULT_ARTICLES = [
    {
        "title": "Python Functions & Optimization",
        "icon": "CODE",
        "color": "#3B82F6",
        "formula": "f(x) = sum(cost[i] * weight[i])",
        "desc": "Functions allow code reuse, improve maintainability, and reduce complexity through modular design patterns.",
        "concept": "Code Modularity",
    },
    {
        "title": "Data Structures & Complexity",
        "icon": "STORAGE",
        "color": "#8B5CF6",
        "formula": "T(n) = O(n log n) for sorting",
        "desc": "Understanding data structures helps optimize algorithms and achieve better runtime performance in large-scale applications.",
        "concept": "Algorithm Efficiency",
    },
    {
        "title": "Machine Learning Basics",
        "icon": "PSYCHOLOGY",
        "color": "#EC4899",
        "formula": "Loss = sum((y_i - y_hat_i)^2) / n",
        "desc": "ML models learn patterns from data using cost functions. Minimize loss to improve model accuracy and generalization.",
        "concept": "Neural Networks",
    },
    {
        "title": "Web Development Principles",
        "icon": "PUBLIC",
        "color": "#F59E0B",
        "formula": "Latency = Server + Network + Render",
        "desc": "Front-end and back-end optimization techniques combine to deliver responsive, scalable web applications.",
        "concept": "Full Stack Design",
    },
    {
        "title": "Control Systems & Feedback",
        "icon": "TUNE",
        "color": "#10B981",
        "formula": "u(t) = Kp*e(t) + Ki*int(e(t)) + Kd*de/dt",
        "desc": "PID controllers regulate systems using proportional, integral, and derivative error terms for precise control.",
        "concept": "Signal Processing",
    },
    {
        "title": "Concurrent Programming",
        "icon": "FLASH_ON",
        "color": "#EF4444",
        "formula": "Speedup = T_sequential / T_parallel",
        "desc": "Multithreading and async patterns enable efficient resource utilization and responsive applications.",
        "concept": "Parallelism",
    },
]


def box_border(color=BORDER, left_color=None, left_width=1):
    return ft.Border(
        left=ft.BorderSide(left_width, left_color or color),
        right=ft.BorderSide(1, color),
        top=ft.BorderSide(1, color),
        bottom=ft.BorderSide(1, color),
    )


def load_blog_posts():
    data_path = Path(__file__).parent.parent.joinpath("data", "blog_posts.json")
    try:
        with open(data_path, encoding="utf-8") as f:
            posts = json.load(f)
        if isinstance(posts, list):
            return posts
    except Exception:
        pass

    return DEFAULT_ARTICLES


def metric(label, value, icon):
    return ft.Container(
        expand=True,
        padding=14,
        bgcolor=PANEL,
        border=box_border(),
        border_radius=8,
        content=ft.Row(
            [
                ft.Icon(icon, color="#38BDF8", size=22),
                ft.Column(
                    [
                        ft.Text(value, size=18, weight=ft.FontWeight.BOLD, color=TEXT),
                        ft.Text(label.upper(), size=10, color=MUTED),
                    ],
                    spacing=0,
                ),
            ],
            spacing=10,
        ),
    )


def chip(label, color="#38BDF8"):
    return ft.Container(
        padding=ft.Padding(10, 5, 10, 5),
        bgcolor="#0B1726",
        border=box_border("#1D334B", color),
        border_radius=20,
        content=ft.Text(label, size=10, color=TEXT, no_wrap=True),
    )


def article_card(article):
    accent = article.get("color", "#38BDF8")
    meta = META_MAP.get(article.get("title"), {})
    tags = meta.get("tags", [article.get("concept", "Engineering")])

    return ft.Card(
        elevation=10,
        shape=ft.RoundedRectangleBorder(radius=8),
        col={"sm": 12, "md": 6, "lg": 6},
        content=ft.Container(
            bgcolor=PANEL,
            border_radius=8,
            border=box_border(left_color=accent, left_width=4),
            padding=18,
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Container(
                                width=46,
                                height=46,
                                bgcolor="#07111F",
                                border_radius=8,
                                border=box_border(accent),
                                content=ft.Icon(
                                    ICON_MAP.get(article.get("icon"), ft.Icons.ARTICLE),
                                    size=25,
                                    color=accent,
                                ),
                                alignment=ft.Alignment(0, 0),
                            ),
                            ft.Column(
                                [
                                    ft.Row(
                                        [
                                            ft.Text(
                                                meta.get("level", "Technical"),
                                                size=10,
                                                color=accent,
                                                weight=ft.FontWeight.BOLD,
                                            ),
                                            ft.Text("|", size=10, color="#35516B"),
                                            ft.Text(meta.get("read", "6 min"), size=10, color=MUTED),
                                        ],
                                        spacing=7,
                                    ),
                                    ft.Text(
                                        article.get("title", "Untitled"),
                                        size=18,
                                        weight=ft.FontWeight.BOLD,
                                        color=TEXT,
                                        max_lines=2,
                                    ),
                                ],
                                spacing=2,
                                expand=True,
                            ),
                        ],
                        spacing=14,
                        vertical_alignment=ft.CrossAxisAlignment.START,
                    ),
                    ft.Text(article.get("desc", ""), size=12, color="#B8C7D8", max_lines=3),
                    ft.Container(
                        bgcolor="#06101C",
                        border_radius=8,
                        border=box_border("#1E3A53"),
                        padding=12,
                        content=ft.Column(
                            [
                                ft.Row(
                                    [
                                        ft.Icon(ft.Icons.TERMINAL, size=14, color=accent),
                                        ft.Text("MODEL NOTE", size=10, color=accent, weight=ft.FontWeight.BOLD),
                                    ],
                                    spacing=6,
                                ),
                                ft.Text(article.get("formula", ""), size=12, color="#EAF2FF", selectable=True),
                            ],
                            spacing=7,
                        ),
                    ),
                    ft.Row([chip(tag, accent) for tag in tags], wrap=True, spacing=8, run_spacing=8),
                    ft.Container(
                        bgcolor=PANEL_ALT,
                        border_radius=6,
                        padding=10,
                        content=ft.Row(
                            [
                                ft.Icon(ft.Icons.INSIGHTS, size=18, color=accent),
                                ft.Text(meta.get("signal", article.get("concept", "")), size=12, color=TEXT, expand=True),
                                ft.Icon(ft.Icons.ARROW_FORWARD, size=18, color=accent),
                            ],
                            spacing=8,
                        ),
                    ),
                ],
                spacing=14,
            ),
        ),
    )


def blog_page():
    articles = load_blog_posts()

    header = ft.Container(
        bgcolor="#081827",
        border_radius=8,
        border=box_border(),
        padding=22,
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Text("Technical Blog", size=32, weight=ft.FontWeight.BOLD, color=TEXT),
                                ft.Text(
                                    "Engineering notes on code, systems, data, control, and performance.",
                                    size=14,
                                    color=MUTED,
                                ),
                            ],
                            spacing=4,
                            expand=True,
                        ),
                        ft.Container(
                            padding=ft.Padding(12, 8, 12, 8),
                            bgcolor="#0B1726",
                            border_radius=20,
                            content=ft.Row(
                                [
                                    ft.Icon(ft.Icons.AUTO_AWESOME, size=16, color="#38BDF8"),
                                    ft.Text("ADVANCED NOTES", size=11, color=TEXT, weight=ft.FontWeight.BOLD),
                                ],
                                spacing=6,
                            ),
                        ),
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.START,
                ),
                ft.Row(
                    [
                        metric("Articles", str(len(articles)), ft.Icons.ARTICLE),
                        metric("Domains", "6", ft.Icons.HUB),
                        metric("Focus", "Applied", ft.Icons.ENGINEERING),
                    ],
                    spacing=12,
                ),
            ],
            spacing=18,
        ),
    )

    cards_grid = ft.ResponsiveRow(
        [article_card(article) for article in articles],
        spacing=18,
        run_spacing=18,
    )

    return ft.Container(
        content=ft.Column(
            [
                header,
                ft.Row(
                    [
                        chip("Algorithms"),
                        chip("Control Systems", "#10B981"),
                        chip("Machine Learning", "#EC4899"),
                        chip("Full Stack", "#F59E0B"),
                        chip("Concurrency", "#EF4444"),
                    ],
                    wrap=True,
                    spacing=10,
                    run_spacing=10,
                ),
                cards_grid,
            ],
            spacing=18,
            expand=True,
        ),
        padding=20,
        bgcolor=SURFACE,
        expand=True,
    )
