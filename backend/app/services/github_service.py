import os
import requests


class GitHubService:
    def __init__(self):
        self.base_url = "https://api.github.com"

    def post_issue_comment(
        self,
        owner: str,
        repo: str,
        pr_number: int,
        review: str,
    ):
        github_token = os.getenv("GITHUB_TOKEN")

        if not github_token:
            raise Exception("GITHUB_TOKEN not found in environment variables.")

        print("Token loaded:", github_token is not None)
        print("Token prefix:", github_token[:15])

        url = (
            f"{self.base_url}/repos/"
            f"{owner}/{repo}/issues/"
            f"{pr_number}/comments"
        )

        headers = {
            "Authorization": f"Bearer {github_token}",
            "Accept": "application/vnd.github+json",
        }

        payload = {
            "body": review
        }

        response = requests.post(
            url=url,
            headers=headers,
            json=payload,
        )

        if response.status_code != 201:
            raise Exception(
                f"GitHub API Error {response.status_code}\n"
                f"{response.text}"
            )

        return response.json()


github_service = GitHubService()