from flask import Flask, render_template, request
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.projects.models import (
    OpenApiTool,
    OpenApiAnonymousAuthDetails
)
import jsonref
import markdown
import os

app = Flask(__name__)

# Initialize AIProjectClient using the connection string from environment variable
project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ.get("PROJECT_CONNECTION_STRING")
)

# Load OpenAPI specification from weather_openapi.json
with open("weather_openapi.json", "r") as f:
    openapi_spec = jsonref.loads(f.read())

# Create Auth object for the OpenApiTool
auth = OpenApiAnonymousAuthDetails()

# Initialize OpenApiTool
openapi = OpenApiTool(
    name="get_weather",
    spec=openapi_spec,
    description="Retrieve weather information for a location",
    auth=auth
)

@app.route('/', methods=['GET', 'POST'])
def index():
    response = ''
    if request.method == 'POST':
        user_question = request.form['question']

        try:
            # Create agent with OpenApi tool
            agent = project_client.agents.create_agent(
                model="gpt-4o",
                name="weather-assistant",
                instructions="You are a helpful weather assistant",
                tools=openapi.definitions
            )
            print(f"Created agent, ID: {agent.id}")

            # Create thread for communication
            thread = project_client.agents.create_thread()
            print(f"Created thread, ID: {thread.id}")

            # Create message to thread
            message = project_client.agents.create_message(
                thread_id=thread.id,
                role="user",
                content=user_question,
            )
            print(f"Created message, ID: {message.id}")

            # Create and process agent run in thread with tools
            run = project_client.agents.create_and_process_run(thread_id=thread.id, assistant_id=agent.id)
            print(f"Run finished with status: {run.status}")

            if run.status == "failed":
                response = "Failed to get weather information."

            # Retrieve the assistant's reply
            messages = project_client.agents.list_messages(thread_id=thread.id)
            assistant_reply = messages['data'][0]['content'][0]['text']['value']
            response = markdown.markdown(assistant_reply)
            print("Retrieved assistant reply.")

            # Delete the assistant when done
            project_client.agents.delete_agent(agent.id)
            print("Deleted agent")

        except Exception as e:
            response = "An error occurred while processing your request."

    return render_template('weather.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)