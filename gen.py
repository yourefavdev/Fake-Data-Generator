from faker import Faker
import random
import os
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich import box

console = Console()


def red_white_gradient(text: str) -> Text:
    """Applies a red-to-white gradient to the input text."""
    colors = ["#ff0000", "#ff1a1a", "#ff3333", "#ff4d4d", "#ff6666", "#ff8080", "#ff9999", "#ffb3b3", "#ffcccc", "#ffffff"]
    gradient_text = Text()
    steps = max(1, len(colors) // max(len(text), 1))

    for i, char in enumerate(text):
        color = colors[min(i * steps, len(colors) - 1)]
        gradient_text.append(char, style=f"bold {color}")
    return gradient_text

def get_german_cities_and_zips():
    """
    Returns a list of German cities and their typical ZIP codes.
    Note: These are examples for demonstration. For comprehensive,
    real-world data, consider using a dedicated database or API.
    """
    return [
        ("Berlin", "10115"), ("Hamburg", "20095"), ("München", "80331"), 
        ("Köln", "50667"), ("Frankfurt am Main", "60311"), ("Stuttgart", "70173"), 
        ("Düsseldorf", "40213"), ("Leipzig", "04109"), ("Dresden", "01067"),
        ("Hannover", "30159") 
    ]

def generate_fake_data(locale='en_US'):
    """
    Generates fake data for a given locale.
    Supports 'de_DE' for Germany and 'en_US' for the USA.
    """
    fake = Faker(locale)

    if locale == 'de_DE':
        cities = get_german_cities_and_zips()
        city, zip_code = random.choice(cities)
        country = "Germany"
        state = fake.state() 
    else: 
        city = fake.city()
        zip_code = fake.postcode()
        country = "USA"
        state = fake.state_abbr() 

    return {
        "First Name": fake.first_name(),
        "Last Name": fake.last_name(),
        "Country": country,
        "State": state,
        "City": city,
        "ZIP": zip_code,
        "Street Address": fake.street_address()
    }

def show_banner():
    """Displays an ASCII art banner with specific red and white styling."""
    banner = """
[bold red]┌┬┐[/bold red][bold white]┌─┐[/bold white][bold red]─┐ ┬ [/bold red] [bold white]┌─┐[/bold white][bold red]┌─┐[/bold red][bold white]┌┐┌[/bold white]
[bold red] ││[/bold red][bold white]├┤ [/bold white][bold red]┌┴┬┘ [/bold red] [bold white]│ ┬[/bold white][bold red]├┤ [/bold red][bold white]│││[/bold white]
[bold red]─┴┘[/bold red][bold white]└─┘[/bold white][bold red]┴ └─ [/bold red] [bold white]└─┘[/bold white][bold red]└─┘[/bold red][bold white]┘└┘[/bold white]
"""
    centered = Align.center(Text.from_markup(banner), vertical="middle")
    console.print(centered)

def main_menu():
    """Displays the main menu for country selection."""
    panel = Panel(
        "[bold white]Select a country code:[/bold white]\n"
        "[bold red]-[/bold red] de (Germany)\n"
        "[bold red]-[/bold red] us (USA)\n"
        "[bold red]-[/bold red] q  (Quit)\n",
        title="📦 [bold white]Fake Data Generator[/bold white]",
        box=box.DOUBLE,
        padding=(1, 4),
        style="bold red"
    )
    console.print(panel)

def main():
    """Main function to run the fake data generator application."""
    os.system('cls' if os.name == 'nt' else 'clear') 
    show_banner()

    while True:
        main_menu()
        choice = console.input("[bold white]Enter country code: [/bold white]").strip().lower()
        if choice == 'q':
            console.print("\n[bold red]Exiting the generator. Goodbye![/bold red]")
            break
        elif choice in ('de', 'us'):
            locale = 'de_DE' if choice == 'de' else 'en_US'
            num = console.input("[bold white]How many records to generate? (default: 1): [/bold white]").strip()
            try:
                num = int(num) if num else 1
            except ValueError:
                console.print("[red]Invalid input. Generating 1 record.[/red]")
                num = 1

            for _ in range(num):
                data = generate_fake_data(locale)
                output = "\n".join(
                    f"[#ff0000][#ffffff]{key}[/#ffffff]: [bold white]{val}[/bold white]" for key, val in data.items()
                )
                console.print(Panel(output, title="[bold red]Generated Data[/bold red]", box=box.ROUNDED, style="white"))
                console.print("\n") 
        else:
            console.print("[bold red]Invalid code. Please try again.[/bold red]")

if __name__ == "__main__":
    main()