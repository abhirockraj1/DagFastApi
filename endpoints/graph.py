# endpoints/graph.py
from fastapi import APIRouter, HTTPException, status
from models import GraphReqBody, GraphResBody # Correct import path

router = APIRouter()

@router.post("/pipelines/parse", response_model=GraphResBody)
async def calGraph(graph_request: GraphReqBody): # Renamed `graph` to `graph_request` for clarity
    """
    Receives a graph in adjacency list format, analyzes it,
    and returns graph statistics.
    """
    # # Print the incoming request body (for debugging, can be removed in production)
    # print("--- Received Graph Request Body (Pydantic Model Instance) ---")
    # print(graph_request) # This will print the Pydantic object
    # print("\n--- Request Body as Dictionary ---")
    # print(graph_request.model_dump()) # This will print the dict representation
    # print("\n--- Request Body as JSON String ---")
    # print(graph_request.model_dump_json(indent=2)) # This will print the JSON string

    try:
        # Calculate the required metrics using the methods on the GraphReqBody instance
        num_nodes = graph_request.get_num_nodes()
        num_edges = graph_request.get_num_edges()
        is_dag_result = graph_request.is_dag()

        # Create an instance of GraphResBody with the calculated values
        # This is where you MUST provide all required fields of GraphResBody
        response_data = GraphResBody(
            num_nodes=num_nodes,
            num_edges=num_edges,
            is_dag=is_dag_result,
            message="Graph analysis performed successfully."
        )

        return response_data

    except Exception as e:
        # Catch any exceptions during graph analysis and return an error response
        print(f"Error during graph analysis: {e}") # Log the actual error
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred during graph analysis: {str(e)}"
        )