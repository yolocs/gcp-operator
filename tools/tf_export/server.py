from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Export Google Cloud Resources as Terraform")


# TODO: Need to add more description.
@mcp.tool(name="export_project_resources")
def export_project_resources(project_id: str) -> str:
    """
    Export the resources of a Google Cloud project as Terraform code.
    :param project_id: The ID of the Google Cloud project to export resources from.
    :return: The Terraform code for the resources in the project.
    """
    return f"Unimplemented: {project_id}"


def run() -> None:
    mcp.run(transport="stdio")
