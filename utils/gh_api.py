import os
import requests
from datetime import datetime, timedelta
from typing import List

REQUEST_TIMEOUT = 5


def fetch_commit_dates(username: str, token: str | None = None, days: int = 90) -> List[datetime.date]:
    """Fetch commit dates for `username` across their public repos over the last `days` days.

    Returns a list of date objects for each commit authored by the user.
    """
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"token {token}"

    since_iso = (datetime.utcnow() - timedelta(days=days)).isoformat() + "Z"
    commit_dates = []

    # list user repos
    page = 1
    per_page = 100
    while True:
        url = f"https://api.github.com/users/{username}/repos?per_page={per_page}&page={page}"
        r = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
        if r.status_code != 200:
            break
        repos = r.json()
        if not repos:
            break

        for repo in repos:
            repo_name = repo.get("name")
            owner = repo.get("owner", {}).get("login")
            # fetch commits by author
            commits_url = f"https://api.github.com/repos/{owner}/{repo_name}/commits?author={username}&since={since_iso}&per_page=100"
            try:
                rc = requests.get(commits_url, headers=headers, timeout=REQUEST_TIMEOUT)
                if rc.status_code != 200:
                    continue
                commits = rc.json()
                for c in commits:
                    date_str = None
                    # prefer commit.author.date
                    if c.get("commit", {}).get("author"):
                        date_str = c["commit"]["author"].get("date")
                    if date_str:
                        try:
                            dt = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
                        except Exception:
                            try:
                                dt = datetime.fromisoformat(date_str)
                            except Exception:
                                continue
                        commit_dates.append(dt.date())
            except Exception:
                continue

        page += 1

    return commit_dates


def fetch_commit_dates_from_repo(owner: str, repo_name: str, author: str, token: str | None = None, days: int = 90) -> List[datetime.date]:
    """Fetch commit dates for a specific GitHub repo authored by `author`."""
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"token {token}"

    since_iso = (datetime.utcnow() - timedelta(days=days)).isoformat() + "Z"
    commit_dates = []

    page = 1
    per_page = 100
    while True:
        commits_url = f"https://api.github.com/repos/{owner}/{repo_name}/commits?author={author}&since={since_iso}&per_page={per_page}&page={page}"
        r = requests.get(commits_url, headers=headers, timeout=REQUEST_TIMEOUT)
        if r.status_code != 200:
            break

        commits = r.json()
        if not commits:
            break

        for c in commits:
            date_str = None
            if c.get("commit", {}).get("author"):
                date_str = c["commit"]["author"].get("date")
            if date_str:
                try:
                    dt = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
                except Exception:
                    try:
                        dt = datetime.fromisoformat(date_str)
                    except Exception:
                        continue
                commit_dates.append(dt.date())

        page += 1

    return commit_dates


def fetch_recent_commits_from_repo(owner: str, repo_name: str, author: str, token: str | None = None, days: int = 90, max_commits: int = 10):
    """Fetch the most recent commits authored by `author` in a specific GitHub repo."""
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"token {token}"

    since_iso = (datetime.utcnow() - timedelta(days=days)).isoformat() + "Z"
    recent_commits = []

    page = 1
    per_page = 100
    while len(recent_commits) < max_commits:
        commits_url = f"https://api.github.com/repos/{owner}/{repo_name}/commits?author={author}&since={since_iso}&per_page={per_page}&page={page}"
        r = requests.get(commits_url, headers=headers, timeout=REQUEST_TIMEOUT)
        if r.status_code != 200:
            break

        commits = r.json()
        if not commits:
            break

        for c in commits:
            date_str = None
            if c.get("commit", {}).get("author"):
                date_str = c["commit"]["author"].get("date")
            if not date_str:
                continue
            try:
                dt = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
            except Exception:
                try:
                    dt = datetime.fromisoformat(date_str)
                except Exception:
                    continue
            message = c.get("commit", {}).get("message", "No commit message")
            html_url = c.get("html_url") or c.get("url")
            recent_commits.append({
                "date": dt,
                "message": message.splitlines()[0],
                "repo": repo_name,
                "url": html_url,
            })
            if len(recent_commits) >= max_commits:
                break

        page += 1

    recent_commits.sort(key=lambda item: item["date"], reverse=True)
    return recent_commits[:max_commits]


def fetch_recent_commits(username: str, token: str | None = None, days: int = 90, max_commits: int = 10):
    """Fetch the most recent commits authored by a GitHub user across public repos."""
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"token {token}"

    since_iso = (datetime.utcnow() - timedelta(days=days)).isoformat() + "Z"
    recent_commits = []

    page = 1
    per_page = 100
    while len(recent_commits) < max_commits:
        repos_url = f"https://api.github.com/users/{username}/repos?per_page={per_page}&page={page}"
        r = requests.get(repos_url, headers=headers, timeout=REQUEST_TIMEOUT)
        if r.status_code != 200:
            break
        repos = r.json()
        if not repos:
            break

        for repo in repos:
            repo_name = repo.get("name")
            owner = repo.get("owner", {}).get("login")
            if not repo_name or not owner:
                continue

            commits_url = f"https://api.github.com/repos/{owner}/{repo_name}/commits?author={username}&since={since_iso}&per_page=100"
            try:
                rc = requests.get(commits_url, headers=headers, timeout=REQUEST_TIMEOUT)
                if rc.status_code != 200:
                    continue
                commits = rc.json()
                for c in commits:
                    date_str = None
                    if c.get("commit", {}).get("author"):
                        date_str = c["commit"]["author"].get("date")
                    if not date_str:
                        continue
                    try:
                        dt = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
                    except Exception:
                        try:
                            dt = datetime.fromisoformat(date_str)
                        except Exception:
                            continue
                    message = c.get("commit", {}).get("message", "No commit message")
                    html_url = c.get("html_url") or c.get("url")
                    recent_commits.append({
                        "date": dt,
                        "message": message.splitlines()[0],
                        "repo": repo_name,
                        "url": html_url,
                    })
                    if len(recent_commits) >= max_commits:
                        break
            except Exception:
                continue

            if len(recent_commits) >= max_commits:
                break

        page += 1

    recent_commits.sort(key=lambda item: item["date"], reverse=True)
    return recent_commits[:max_commits]
