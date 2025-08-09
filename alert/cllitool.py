import typer 
import rich
from news import news

@app.command
def news():
    news()  

if __name__ == "__main__":
    app()
