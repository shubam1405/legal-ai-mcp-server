import re

CURRENT_DOCUMENT = ""


def set_document_text(text):
    """Store the latest uploaded legal document."""
    global CURRENT_DOCUMENT
    CURRENT_DOCUMENT = text


def summarize_document():
    """Generate a summary of the uploaded legal judgment."""
    return CURRENT_DOCUMENT[:3000]


def extract_ipc_sections():
    """Extract IPC sections mentioned in the document."""
    pattern = r"Section\s\d+"
    matches = re.findall(pattern, CURRENT_DOCUMENT)
    return list(set(matches))


def extract_case_citations():
    """Extract case precedents cited in the judgment."""
    pattern = r"[A-Z][A-Za-z\s\.&]+ v\. [A-Z][A-Za-z\s\.&]+"
    matches = re.findall(pattern, CURRENT_DOCUMENT)
    cleaned = [m.replace("\n", " ").strip() for m in matches]
    return list(set(cleaned))


def generate_case_brief():
    """Generate a structured legal case brief from the judgment."""

    text = CURRENT_DOCUMENT[:6000]

    return f"""
Analyze the following judgment and produce a case brief.

{text}

Return the result in this format:

Case Name:
Facts:
Issues:
Arguments:
Court Reasoning:
Final Judgment:
Legal Principles:
"""


def legal_research_tool(query: str):
    """Perform legal research and provide explanation, IPC sections, and precedents."""

    return f"""
Perform legal research for:

{query}

Provide:
1. Explanation
2. Relevant IPC sections
3. Important precedents
4. Court reasoning
"""
def set_document_text(text: str):
    """Store the uploaded legal document for analysis."""
    global CURRENT_DOCUMENT
    CURRENT_DOCUMENT = text
    return "Document stored successfully."