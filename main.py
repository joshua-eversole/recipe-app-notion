# main.py
import argparse
from src.notion_api.client import create_recipe_page
from src.scrapers.recipe_scraper import scrape_recipe_data # Import the actual scraper

# This script is the main entry point for the recipe app.
# It orchestrates the scraping of a recipe from a given URL and adds it to Notion.
def main():
    """
    Main function to parse arguments and orchestrate the process.
    """
    parser = argparse.ArgumentParser(
        description="Scrape a recipe from a given URL and add it to Notion."
    )
    parser.add_argument(
        "url",
        type=str,
        help="The URL of the recipe to scrape (e.g., https://www.allrecipes.com/...)"
    )

    args = parser.parse_args()
    recipe_url = args.url

    print(f"Starting recipe app for URL: {recipe_url}")

    # 1. Scrape the recipe data (now using the actual scraper)
    print("\nStep 1: Scraping recipe data...")
    recipe_data = scrape_recipe_data(recipe_url) # CALLING THE REAL SCRAPER

    if not recipe_data or not recipe_data.get("title"):
        print("Error: Could not scrape valid recipe data from the URL or site not supported.")
        return

    print("\nScraped Data:")
    print(f"  Title: {recipe_data.get('title', 'N/A')}")
    print(f"  URL: {recipe_data.get('url', 'N/A')}")
    print(f"  Ingredients: {recipe_data.get('ingredients', ['N/A'])[:2]}...")
    print(f"  Instructions: {recipe_data.get('instructions', ['N/A'])[:2]}...")
    print(f"  Nutritional Facts: {recipe_data.get('nutritional_facts', 'N/A')}")

    # 2. Add to Notion
    print("\nStep 2: Adding recipe to Notion...")
    success = create_recipe_page(recipe_data)

    if success:
        print("\nProcess completed successfully: Recipe data added to Notion!")
    else:
        print("\nProcess failed: Could not add recipe to Notion.")

if __name__ == "__main__":
    main()
