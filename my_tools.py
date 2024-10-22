from crewai_tools import tool
import requests
        
    
@tool    
def url_checker_tool(url:str):
    """
    Testar se url retorna 200, indicando que site is ok
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return 'True' #f"The URL {url} is working."
        else:
            return 'False' # f"The URL {url} returned status code {response.status_code}."
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"    

################################


#url_checker_tool = Tool(
#    name="URL Checker",
#    description="Checks if a given URL is accessible.",
#    func=check_url
#)
