from workshop.api.weather import fetch_weather
from workshop.api.universe import fetch_galaxy


def main():
    print("Painting the sky")
    fetch_galaxy()
    fetch_weather()

if __name__ == "__main__":
    main()