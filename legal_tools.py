import re

CURRENT_DOCUMENT = ""


def set_document_text(text):
    """Store the latest uploaded legal document."""
    global CURRENT_DOCUMENT
    CURRENT_DOCUMENT = text


def summarize_document(document_text: str):
    """Summarize a legal judgment document."""

    return document_text[:3000]

def extract_ipc_sections(document_text: str):
    """Extract IPC sections from the document."""

    import re

    pattern = r"Section\s\d+"

    return list(set(re.findall(pattern, document_text)))

def extract_case_citations(document_text: str):
    """Extract case precedents."""

    import re

    pattern = r"[A-Z][A-Za-z\s\.&]+ v\. [A-Z][A-Za-z\s\.&]+"

    matches = re.findall(pattern, document_text)

    return list(set(matches))
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