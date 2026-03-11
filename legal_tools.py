import re

CURRENT_DOCUMENT = ""


def set_document_text(text):
    global CURRENT_DOCUMENT
    CURRENT_DOCUMENT = text


def summarize_document():
    """
    Generate a summary of the uploaded legal judgment.
    """
    return CURRENT_DOCUMENT[:3000]


def extract_ipc_sections():
    """
    Extract IPC sections mentioned in the document.
    """

    pattern = r"Section\s\d+"

    matches = re.findall(pattern, CURRENT_DOCUMENT)

    return list(set(matches))


def extract_case_citations():
    """
    Extract case precedents cited in the judgment.
    """

    pattern = r"[A-Z][A-Za-z\s\.&]+ v\. [A-Z][A-Za-z\s\.&]+"

    matches = re.findall(pattern, CURRENT_DOCUMENT)

    cleaned = [m.replace("\n", " ").strip() for m in matches]

    return list(set(cleaned))


def generate_case_brief():
    """
    Generate a structured case brief.
    """

    text = CURRENT_DOCUMENT[:6000]

    return f"""
Analyze the following judgment and produce a case brief.

{text}

Return in this format:

Case Name:
Facts:
Issues:
Arguments:
Court Reasoning:
Final Judgment:
Legal Principles:
"""
def legal_research_tool(query: str):
    """
    Perform legal research using the case database.
    """

    return f"""
Perform legal research for the following query:

{query}

Provide:

1. Explanation of the legal concept
2. Relevant IPC sections
3. Important precedents
4. Legal reasoning from courts
"""