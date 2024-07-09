# Amazon Used Condition

This Python script allows you to modify Amazon product URLs to filter by product condition (new, used, or renewed). It's particularly useful for automatically generating condition-specific links from a given Amazon product URL.

## Features

- Adds condition filters to Amazon product URLs
- Supports different condition IDs for various product categories
- Generates URLs for new, used, and renewed product conditions
- Maintains original URL parameters while adding or updating necessary ones
- Handles URL encoding and decoding

## Requirements

- Python 3.x
- No external libraries required (uses only built-in Python modules)

## Usage

1. Run the script:
   ```
   python amazon_url_filter.py
   ```

2. When prompted, enter an Amazon product URL.

3. The script will output four URLs:
   - The original URL
   - URL filtered for new products
   - URL filtered for used products
   - URL filtered for renewed products

4. You can enter multiple URLs. Type 'quit' to exit the program.

## Functions

### `get_condition_ids(category)`
Returns a dictionary of condition IDs based on the product category.

### `add_condition_filter(url, condition='used')`
Modifies the given URL to include the specified condition filter.

### `get_all_condition_urls(url)`
Generates URLs for all conditions (new, used, renewed) based on the input URL.

### `main()`
Handles user input and output in a loop until the user quits.

## Notes

- The script assumes certain URL parameters and structures typical of Amazon product pages. It may need updates if Amazon significantly changes their URL format.
- The 'kitchen' category uses different condition IDs. Other categories use a default set of IDs.
- The script generates a random 'qid' parameter if one doesn't exist in the original URL.

## Disclaimer

This script is for educational purposes only. Ensure you comply with Amazon's terms of service and robots.txt when using this script.

## Contributing

Feel free to fork this repository and submit pull requests for any enhancements.

## License

[MIT License](https://opensource.org/licenses/MIT)