#here lets create different agent for it
from langgraph.graph import StateGraph,START,END
from typing_extensions import TypedDict,Literal
from langchain_openai import ChatOpenAI
from pydantic import BaseModel,Field
from langchain_core.messages import SystemMessage,HumanMessage
from IPython.display import Image, display
from dotenv import load_dotenv
load_dotenv()



llm=ChatOpenAI(model="gpt-4o")

class router(BaseModel):
      step:Literal["general-knowledge","summerizer","extractor"]=Field(None,description="next step in routing") 


llm_with_router=llm.with_structured_output(router)



class State(TypedDict):
      input:str
      decision:str
      output:str
      

def llm_call_router(state:State):
     response=llm_with_router.invoke(
         [
             SystemMessage(content="route the user request to general-knowledge,summerizer or extractor ")
             ,HumanMessage(content=state["input"])
         ]
         
         
     )   
     return {"decision":response.step}
    
    
def route_decision(state:State):
    if state["decision"]=="general-knowledge":
        return "run_gk"
    
    elif state["decision"]=="summerizer":
        return "run_summerizer"
    
    elif state["decision"]=="extractor":
        return "run_extractor"
    

gk_system_message=SystemMessage(content="you are a helpful assistant who are expert in general knowledge, pleaseanswer the following question  ")    
summerizer_system_message=SystemMessage(content="you are a helpful assistant who are expert in summarizing input text in pointwise manner.   ")    
extracter_system_message=SystemMessage(content="you are a helpful assistant who are expert in extracting entities from input text.   ")    

def run_gk(state:State):
    result=llm.invoke([gk_system_message,state["input"]])
    return {"output":result.content}

def run_summerizer(state:State):
    result=llm.invoke([summerizer_system_message ,state["input"]])
    return {"output":result.content}
    

def run_extractor(state:State):
    result=llm.invoke([extracter_system_message, state["input"]])
    return {"output":result.content}


graph=None
def build_graph():
    builder=StateGraph(State)
    builder.add_node("run_gk",run_gk)
    builder.add_node("run_summerizer",run_summerizer)
    builder.add_node("run_extractor",run_extractor)
    builder.add_node("llm_call_router",llm_call_router)

    builder.add_edge(START,"llm_call_router")
    builder.add_conditional_edges("llm_call_router",route_decision,{"run_gk":"run_gk","run_summerizer":"run_summerizer","run_extractor":"run_extractor"})
    builder.add_edge("run_gk",END)
    builder.add_edge("run_summerizer",END)
    builder.add_edge("run_extractor",END)

    graph=builder.compile()
    
    return graph

    #display(Image(graph.get_graph().draw_mermaid_png()))



def run_query(input:str)->str:
    global graph
    if graph is None:
       graph=build_graph()
        
    return graph.invoke({"input":input})



    