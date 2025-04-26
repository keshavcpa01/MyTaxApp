from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def coming_soon():
    return """
    <html>
        <head>
            <title>Coming Soon</title>
        </head>
        <body style="text-align: center; margin-top: 100px;">
            <h1>?? Coming Soon!</h1>
            <p>We are working hard to launch our tax software. Stay tuned!</p>
        </body>
    </html>
    """


