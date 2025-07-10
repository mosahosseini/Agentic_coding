# Initialize the local model
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_ollama import OllamaLLM  # Or use OpenAI
import wikipedia 
from langchain_core.runnables import RunnableSequence
import warnings
from bs4 import GuessedAtParserWarning

warnings.filterwarnings("ignore", category=GuessedAtParserWarning)
llm_ollama = OllamaLLM(model="gemma3:4b")


def wikipedia_search(query: str , num_sentences:int = 5) ->str:
    """
    Docstring:   Searches wikipedia homepage given a word.
    
    args:
        query (str): the query for wikipedia.
        num_sentences  (int): number of output sentences.

    returns:
        result (str): the result from wikipedia.

    """
    try:
        most_close_query = wikipedia.search(query)[0]

        summary = wikipedia.page(most_close_query , auto_suggest=False, redirect=True).summary
        sentences = summary.split('. ')
        return '. '.join(sentences[:num_sentences]) + '.'
        #return summary
        
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Too many results please choose from following topics: {e.options[0:6]}" 
    except Exception as e:
        return f"Error: {str(e)}"



def ask_llm(question:str  ) -> str:
    """
    This function will use ollama for converting the question into a valid wikipedia search keyword.

    Args:
        question (str): The entered question. 
    
    Returns:
        result (str): The valid wikipedia keyword
    """
    prompt = PromptTemplate.from_template(
        "Given the following question, output only the most relevant Wikipedia search keyword or page title, and nothing else.\n\nQuestion: {question}\n\nKeyword:"
    )

    chain = prompt | llm_ollama
    return chain.invoke({"question":question}) 

def ask_llm_with_context(question:str , wikipedia_context:str) -> str:
    """
    This function will take the question and context and will gives the answer to the question.

    Args:
        question (str): The entered question
        context (str): The summary from wikipedia page
    Returns:
        result (str): The full answer to the question
    """
    if wikipedia_context.startswith("Too many"):
        
        prompt = PromptTemplate.from_template(
            "You are a helpful assistant, answer the question based, be consice and never hallucinate. \n\n Question: {question}"
        )
        
        # chain = LLMChain(llm = llm_ollama , prompt = prompt)
        chain = prompt | llm_ollama
        return chain.invoke({"question": question})
    else: 
        prompt = PromptTemplate.from_template(
        "You are a helpful assistant, answer the question based on context. \n\n Question: {question} \n\n Context: {context}"
        )
    
        # chain = LLMChain(llm = llm_ollama , prompt = prompt)
        chain = prompt | llm_ollama
        return chain.invoke({"context": wikipedia_context, "question": question})
      
def run_bot(question):
    
    topic_for_wikipedia = ask_llm(question) 
    context = wikipedia_search(topic_for_wikipedia)
    return ask_llm_with_context(question , context)

if __name__ == "__main__":
    print(r"Welcome to wikipedia QA bot. Type [\exit , \stop ,\q , \s] to stop the bot")
    while(True):
        question = str(input("Ask a question:"))
        if question.lower() in [r"\exit", r"\stop" , r"\stopp" , r"\quit" , r"\quitt" , r"\q"]: 
            print("Goodbye! :) ")
            break

        print(run_bot(question) , "\n\n")
        