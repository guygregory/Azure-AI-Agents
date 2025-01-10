![image](https://github.com/user-attachments/assets/fea828c1-8545-4dde-b5eb-c4797c6a0220)

## Description

This Python application provides a lightweight Flask frontend to demonstrate the Azure AI Agent service, and builds on the [official sample code](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/ai/azure-ai-projects/samples/agents/sample_agents_openapi.py) in Microsoft Learn. The application leverages the Project client in the Azure AI Foundry SDK and the OpenAPI 3.x specification to retrieve weather information from wttr.in.

## Features

- Use of [Azure AI Agent Service](https://learn.microsoft.com/en-us/azure/ai-services/agents/) to create and manage AI agents.
- Integration with OpenAPI 3.x specification for weather data retrieval.
- Web interface built with Flask to interact with the weather assistant.

## Prerequisites

- Python 3.8 or later
- Azure subscription and necessary credentials
- Azure AI Foundry project and hub, with a gpt-4o deployment
- Flask
- [Azure AI Projects](https://pypi.org/project/azure-ai-projects) library
- wttr.in weather API

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/guygregory/Azure-AI-Agents.git
    cd Azure-AI-Agents
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```sh
    pip install azure-ai-projects azure-identity flask
    ```

4. Set up environment variables:
    ```sh
    set PROJECT_CONNECTION_STRING="your_project_connection_string"
    ```

## Usage

1. Run the Flask application:
    ```sh
    python ".\app - weather.py"
    ```

2. Open your web browser and go to `http://127.0.0.1:5000`.

3. Use the web interface to ask about the weather for a specific location.

## File Structure

- `app - weather.py`: Main Flask application code.
- `templates/weather.html`: HTML template for the web interface.
- `weather_openapi.json`: OpenAPI specification for the weather data API.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgments

- [wttr.in](https://wttr.in) for providing the weather API.
- [official sample code[(https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/ai/azure-ai-projects/samples/agents/sample_agents_openapi.py)
