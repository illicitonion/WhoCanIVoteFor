import requests

from .models import PersonPost


def get_wikipedia_extract(wikipedia_url):
    base_url = "https://en.wikipedia.org/api/rest_v1/page/summary/"
    wiki_title = wikipedia_url.strip("/").split("/")[-1]
    url = "{}{}".format(base_url, wiki_title)

    print(url)
    resp = requests.get(url)
    if resp.status_code != 200:
        return None
    try:
        resp = resp.json()
    except Exception:
        return None

    return resp.get("extract", None)


def peopleposts_for_election_post(election, post):
    return PersonPost.objects.filter(election=election, post=post)
