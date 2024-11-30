from crewai import LLM

class MyLLM():
	GPT4o_mini 				= LLM(model='gpt-4o-mini')
	GPT4o_mini_2024_07_18  	= LLM(model='gpt-4o-mini-2024-07-18')
	GPT4o					= LLM(model='gpt-4o')
	GPT_o1 					= LLM(model='01-preview')
	GPT3_5					= LLM(model='gpt-3.5-turbo')
	LLAMA3_70B				= LLM(model='llama3-70b-8192')
	GROQ_LLAMA1             = LLM(model='groq/llama-3.1-8b-instant') #llama3-70b-8192')
    #GROQ_LLAMA2             = LLM(model='groq/llama-3.1-8b-instant')
    #GROQ_LLAMA3             = LLM(model='groq/mixtral-8x7b-32768')