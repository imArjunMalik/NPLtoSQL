# NLP to SQL Query Generator

This project is designed to translate natural language inputs into SQL queries using OpenAI's API. The application takes user-provided natural language queries and generates corresponding SQL queries to interact with a database.

## Features

- **Natural Language Processing**: Converts user inputs in natural language into SQL queries.
- **OpenAI Integration**: Utilizes OpenAI's API for NLP processing.
- **Data Loading**: Loads data from CSV files to create table definitions.
- **SQLAlchemy Integration**: Uses SQLAlchemy to execute the generated SQL queries.

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/nlp-to-sql-query-generator.git
   cd nlp-to-sql-query-generator

## Set up OpenAI API Key

- Create a .env file in the root directory.
- Add your OpenAI API key to the .env file
  ```sh
  OPENAI_API_KEY=your_openai_api_key

## Example run

```sh
Enter the info you want: Show me the total sales for the last month
Generated SQL Query: 
SELECT SUM(sales) 
FROM Sales 
WHERE date >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH)

## Acknowledgements

- OpenAI
- SQLAlchemy
