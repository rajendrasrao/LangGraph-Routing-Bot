import streamlit as st
import router
import json



def main():
    st.header("🧠 Intelligent Query Routing Chatbot")  
    st.subheader("🚀 Powered by LangGraph")  

    st.write(  
    "This chatbot intelligently routes your queries to the right AI agent. To guide the routing engine, **start your query with keywords like**:"  
    )  

    st.markdown("""  
    - 📝 **"Summarize"** → Condense long text into key points  
    - 🔍 **"Extract entities"** → Identify names, dates, emails, etc.  
    - 📚 **"General knowledge"** → Ask factual questions  
""")  

    st.write("Try it out! Enter your query in the text box below.")  
    with st.form("my_form"):
        user_input=st.text_area("Enter your input:",height=150)
        submitted = st.form_submit_button("Submit")
       
       
        if submitted:
            response=router.run_query(user_input)
            
            st.write(f"routing engine identified it as {response["decision"]} query",)

            st.write(f" {response['output']}")
             



if __name__ == "__main__":
   main()