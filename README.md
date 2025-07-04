Graph Analysis APIA simple FastAPI application that receives graph data in an adjacency list format, analyzes it to determine the number of nodes, number of edges, and whether it is a Directed Acyclic Graph (DAG).📊 FeaturesGraph Representation: Uses an adjacency list for graph input.Node Count: Calculates the total number of unique nodes in the graph.Edge Count: Calculates the total number of directed edges in the graph.DAG Detection: Determines if the graph is a Directed Acyclic Graph (DAG) using Kahn's algorithm (topological sort).Pydantic Validation: Leverages Pydantic for robust request body validation and structured API responses.FastAPI: Provides a modern, fast, and asynchronous web framework with automatic interactive API documentation (Swagger UI).🚀 InstallationClone the repository (if applicable):# If this were a Git repository
# git clone <repository-url>
# cd graph-analysis-api
Create a virtual environment (recommended):python -m venv venv
Activate the virtual environment:On Windows:.\venv\Scripts\activate
On macOS/Linux:source venv/bin/activate
Install the dependencies:pip install fastapi uvicorn pydantic
📂 Project StructureThe project is structured to separate concerns, making it organized and scalable..
├── main.py
├── models
└── endpoints/
    └── graph.py
main.py: The main FastAPI application file, responsible for including routers and starting the application.pydantic_models.py: Contains all Pydantic models used for both incoming request bodies and outgoing API responses. It also includes the graph analysis logic.endpoints/: A directory containing API endpoint definitions.graph.py: Defines the /analyze-graph/ endpoint and its logic.💡 Pydantic Models Explainedpydantic_models.pyThis file defines the data structures for the API:GraphReqBodyThis model defines the structure for the incoming request body, representing the graph as an adjacency list. It also includes methods to perform graph analysis.from pydantic import BaseModel, Field
from typing import Dict, List, Hashable, Set
from collections import deque

class GraphReqBody(BaseModel):
    graph: Dict[Hashable, List[Hashable]] = Field(
        ...,
        description="Adjacency list representation of the graph."
    )

    # Methods for graph analysis:
    def get_num_nodes(self) -> int:
        # ... (implementation for counting nodes)
        pass

    def get_num_edges(self) -> int:
        # ... (implementation for counting edges)
        pass

    def is_dag(self) -> bool:
        # ... (implementation for DAG detection using Kahn's algorithm)
        pass
GraphResBodyThis model defines the structure for the outgoing API response, providing the calculated graph statistics.from pydantic import BaseModel, Field

class GraphResBody(BaseModel):
    num_nodes: int = Field(..., description="The total number of nodes in the graph.")
    num_edges: int = Field(..., description="The total number of directed edges in the graph.")
    is_dag: bool = Field(..., description="True if the graph is a Directed Acyclic Graph (DAG), False otherwise.")
    message: str = "Graph analysis complete."
🚀 Usage1. Run the APINavigate to the root directory of your project (where main.py is located) in your terminal and run:uvicorn main:app --reload
The API will be accessible at http://127.0.0.1:8000. The --reload flag enables auto-reloading on code changes, which is useful for development.2. Access API DocumentationOnce the server is running, you can access the interactive API documentation (Swagger UI) at:http://127.0.0.1:8000/docsThis interface allows you to test the API directly from your browser.3. API EndpointsPOST /analyze-graph/Analyzes a graph provided in the request body and returns its properties.URL: /analyze-graph/Method: POSTRequest Body: application/jsonSchema: GraphReqBody (defined in pydantic_models.py)Example:{
  "graph": {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": ["E"],
    "E": []
  }
}
Response Body: application/jsonSchema: GraphResBody (defined in pydantic_models.py)Success Example (DAG):{
  "num_nodes": 5,
  "num_edges": 4,
  "is_dag": true,
  "message": "Graph analysis performed successfully."
}
Success Example (Not a DAG - Cyclic):{
  "num_nodes": 3,
  "num_edges": 3,
  "is_dag": false,
  "message": "Graph analysis performed successfully."
}
Error Example (HTTP 500 Internal Server Error):{
  "detail": "An error occurred during graph analysis: <error_message>"
}
GET /A simple root endpoint to check if the API is running.URL: /Method: GETResponse Body: application/jsonExample:{
  "message": "Graph analysis API is running!"
}
🤝 ContributingContributions are welcome! Please feel free to open issues or submit pull requests.📄 LicenseThis project is open-sourced under the MIT License.
