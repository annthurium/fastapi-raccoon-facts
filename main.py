from fastapi import FastAPI
from fastapi.responses import HTMLResponse

import requests

app = FastAPI()

async def get_raccoon_fact(api_version):
    url = f"https://versioned-api.onrender.com/v{api_version}/fact/"
    headers = {"Accept": "application/json", "User-Agent": "LaunchDarkly Progressive Rollout Tutorial"}
    response = requests.get(url=url, headers=headers)
    return response.json()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    api_version = 0
    fact = await get_raccoon_fact(api_version=api_version)

    html = """
    <html>
        <head>
            <title>Raccoon facts!</title>
        </head>
        <body>
            <h1>Wacky raccoon facts!!!</h1>
            <h2>{fact}</h2>
            <p>api version: {api_version}</p>
        </body>
    </html>
    """.format(fact=fact, api_version=api_version)
    return html