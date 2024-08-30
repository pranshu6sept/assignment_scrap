import click
from scrapper import scrape_data,save_data
from processor import data,calculate,display

def cli():
    pass

def scrape():
    data = scrape_data()
    save_data(data)
    click.echo('Data scraped and saved to file')

def show():
    data = data()
    display(data)

def search(keyword):
    data = data()
    result = [item for item in data if keyword.lower() in item['name'.lower()]]
    display(result)

def stats():
    data = data()
    stats = calculate(data)
    click.echo(stats)

cli.add_command(scrape)
cli.add_command(show)
cli.add_command(search)
cli.add_command(stats)

if __name__ == '__main__':
    cli()
                