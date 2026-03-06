import requests


def start_workflow(token, repo, workflow):

    url = f"https://api.github.com/repos/{repo}/actions/workflows/{workflow}/dispatches"

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }

    data = {"ref": "main"}

    r = requests.post(url, headers=headers, json=data)

    return r.status_code


def list_runs(token, repo):

    url = f"https://api.github.com/repos/{repo}/actions/runs"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    r = requests.get(url, headers=headers)

    return r.json()


def cancel_run(token, repo, run_id):

    url = f"https://api.github.com/repos/{repo}/actions/runs/{run_id}/cancel"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    r = requests.post(url, headers=headers)

    return r.status_code
