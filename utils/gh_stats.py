from pathlib import Path
import subprocess
from datetime import datetime, timedelta


def generate_commit_graph(repo_path: Path, out_path: Path, days: int = 90):
    """Generate a commits-per-day graph for the last `days` days from a local git repo.

    repo_path: Path to the git repository (root)
    out_path: Path where the PNG graph will be written
    """
    try:
        cmd = [
            "git",
            "-C",
            str(repo_path),
            "log",
            f"--since={days} days ago",
            "--pretty=format:%ci",
        ]
        out = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True)
    except Exception:
        return False

    # parse dates
    dates = []
    for line in out.splitlines():
        line = line.strip()
        if not line:
            continue
        # try parsing with timezone
        try:
            dt = datetime.strptime(line, "%Y-%m-%d %H:%M:%S %z")
        except Exception:
            try:
                dt = datetime.strptime(line, "%Y-%m-%d %H:%M:%S")
            except Exception:
                continue
        dates.append(dt.date())

    # build date range
    end = datetime.now().date()
    start = end - timedelta(days=days - 1)
    day_list = [start + timedelta(days=i) for i in range(days)]

    counts = {d: 0 for d in day_list}
    for d in dates:
        if d in counts:
            counts[d] += 1

    x = day_list
    y = [counts[d] for d in x]

    # plot (import matplotlib here so module import doesn't fail when matplotlib missing)
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
    except Exception:
        return False

    fig, ax = plt.subplots(figsize=(10, 3), facecolor="#06101C")
    ax.set_facecolor("#06101C")
    ax.bar(x, y, color="#48F838", width=0.82)
    ax.set_ylim(0, max(max(y), 1))
    ax.set_ylabel("Commits/day", color="#E5EEF8")
    ax.set_xlabel("Date", color="#E5EEF8")
    ax.tick_params(axis='x', which='major', labelrotation=45, colors="#8DA2B8")
    ax.tick_params(axis='y', colors="#8DA2B8")
    ax.grid(axis="y", color="#20364D", linewidth=0.8, alpha=0.7)
    for spine in ax.spines.values():
        spine.set_color("#20364D")
    # reduce number of x ticks
    if days > 20:
        step = max(1, days // 10)
        ax.set_xticks(x[::step])

    plt.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(str(out_path), facecolor=fig.get_facecolor(), edgecolor="none")
    plt.close(fig)
    return True


def generate_commit_graph_from_dates(dates_list, out_path: Path, days: int = 90):
    """Generate commits-per-day graph from a list of date objects (datetime.date)."""
    # build date range
    end = datetime.now().date()
    start = end - timedelta(days=days - 1)
    day_list = [start + timedelta(days=i) for i in range(days)]

    counts = {d: 0 for d in day_list}
    for d in dates_list:
        if d in counts:
            counts[d] += 1

    x = day_list
    y = [counts[d] for d in x]

    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
    except Exception:
        return False

    fig, ax = plt.subplots(figsize=(10, 3), facecolor="#06101C")
    ax.set_facecolor("#06101C")
    ax.bar(x, y, color="#48F838", width=0.82)
    ax.set_ylim(0, max(max(y), 1))
    ax.set_ylabel("Commits/day", color="#E5EEF8")
    ax.set_xlabel("Date", color="#E5EEF8")
    ax.tick_params(axis='x', which='major', labelrotation=45, colors="#8DA2B8")
    ax.tick_params(axis='y', colors="#8DA2B8")
    ax.grid(axis="y", color="#20364D", linewidth=0.8, alpha=0.7)
    for spine in ax.spines.values():
        spine.set_color("#20364D")
    if days > 20:
        step = max(1, days // 10)
        ax.set_xticks(x[::step])

    plt.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(str(out_path), facecolor=fig.get_facecolor(), edgecolor="none")
    plt.close(fig)
    return True
