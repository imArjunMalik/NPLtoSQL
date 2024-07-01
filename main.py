import openai
import os 
import pandas as pd 
from sqlalchemy import create_engine
from sqlalchemy import text 

# Creates the prompt to pass to openai 
def create_table_definition(df):
    prompt = """### sqlite SQL table, with properties: 
    #
    # Sales({})
    #
    """.format(",".join(str(col) for col in df.columns))
    return prompt 

# Gets the nlp request from the user
def prompt_input():
    nlp_text = input("Enter the info you want: ")
    return nlp_text

def combine_prompts(df, query_prompt):
    definiton = create_table_definition(df)
    query_init_string = f"### A query to answer: {query_prompt}\nSELECT"
    return definiton+query_init_string

def handle_response(response):
    query = response.choices[0].text
    if query.startswith(" "):
        query = "SELECT"+query
    return query

def main(): 
    # Load and store API key
    openai.api_key = os.getenv('OPENAI_API_KEY')
    os.getenv('OPENAI_API_KEY')

    # Load data
    df = pd.read_csv("/Users/arjunmalik/OpenAI API/NLP_to_SQL/sales_data_sample.csv")

    # Create temporary database in RAM
    temp_db = create_engine('sqlite:///:memory:')

    # Push Pandas Df --> Temp DB
    data = df.to_sql(name='Sales', con=temp_db)

    nlp_request = prompt_input()

    # Pass it to the openai api 
    response = openai.completions.create(
        model = 'text-davinci-002',
        prompt = combine_prompts(df, nlp_request),
        temperature = 0,
        max_tokens = 100,
        top_p = 1.0,
        frequency_penalty = 0,
        presence_penalty = 0,
        stop = [';', '#']
    )
    #print(handle_response(response))

    # Connec to sql table and pass queries
    with temp_db.connect() as conn: 
        # makes the connection 
        # we can write code in this indentation 
        # 'with' operator auto closes the connection 
        result = conn.execute(text(handle_response(response))) # SQL query
    print(result.all())
    
if __name__== "__main__":
    main()