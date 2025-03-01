# 🚀 Intelligent Query Routing Chatbot  

This project is a LangGraph-powered chatbot that intelligently routes user queries to the appropriate AI agent for **Summarization, Entity Extraction, and General Knowledge Q&A**.  

## 🛠️ Project Setup  

Follow these steps to set up and run the project:  

### **1️⃣ Create a Conda Environment**  
Run the following command to create a new Conda environment named `routerenv` with Python 3.12.3:  
```sh
conda create -p routerenv python=3.12.3
```
2️⃣ Activate the Conda Environment
```sh
Activate the newly created environment:
conda activate routerenv
```
Note: If the environment was created in the root folder, copy the full path of the routerenv folder and use it to activate the environment.

3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```
4️⃣ Set Up the .env File
OPENAI_API_KEY=your-api-key-here

5️⃣ Run the Streamlit Application
```sh
streamlit run run_app.py
```
below is how graph flow looks like for this application.
![Alt Text](image/graph_flow.jpg)


below are the streamlit page look like for this application:
![Alt Text](image/home.jpg)
![Alt Text](image/response_gk.jpg)
![Alt Text](image/response_summarize.jpg)
![Alt Text](image/response_entities.jpg)




Now your project is set up and ready to use! 🚀
Feel free to contribute and improve the project. 😊


