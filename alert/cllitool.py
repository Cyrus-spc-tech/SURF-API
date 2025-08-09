import typer 
import rich
from news import news
from weather import weather
app = typer.Typer()


@app.command()
def get_news():
    news()

@app.command()
def get_weather(city: str):
    weather(city)


if __name__ == "__main__":
    app()
