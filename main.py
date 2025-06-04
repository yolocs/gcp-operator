import os
import logging
import click
import uvicorn
from google.adk.cli.fast_api import get_fast_api_app
from tools.tf_export import server as tf_export_server


@click.command()
@click.option("--run-mcp-server", help="The MCP server to run.")
@click.option("--run-agent", default="default", help="The agent to run.")
def main(run_mcp_server: str, run_agent: str) -> None:
    if run_mcp_server:
        dispatch_run_mcp_server(run_mcp_server)
    else:
        logging.info(f"Running agent {run_agent}...")
        app = get_fast_api_app(
            agents_dir=os.path.join(os.path.dirname(__file__), "agent"),
            # allow_origins=["*"],
            web=True,
        )
        uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))


def dispatch_run_mcp_server(tool_name: str) -> None:
    match tool_name:
        case "tf-export":
            tf_export_server.run()
        case _:
            raise ValueError(f"Unknown tool: {tool_name}")


if __name__ == "__main__":
    main()
