from fastmcp import FastMCP
from legal_tools import (
    summarize_document,
    extract_ipc_sections,
    extract_case_citations,
    generate_case_brief,
    legal_research_tool
)

mcp = FastMCP("Legal AI MCP Server")

mcp.tool()(summarize_document)
mcp.tool()(extract_ipc_sections)
mcp.tool()(extract_case_citations)
mcp.tool()(generate_case_brief)
mcp.tool()(legal_research_tool)

if __name__ == "__main__":
    mcp.run()