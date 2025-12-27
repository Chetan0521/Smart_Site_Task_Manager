from datetime import datetime
import re

CATEGORY_KEYWORDS = {
    "scheduling": ["meeting", "schedule", "call", "appointment", "deadline"],
    "finance": ["payment", "invoice", "bill", "budget", "cost", "expense"],
    "technical": ["bug", "fix", "error", "install", "repair", "maintain"],
    "safety": ["safety", "hazard", "inspection", "compliance", "ppe"],
}

PRIORITY_KEYWORDS = {
    "high": ["urgent", "asap", "immediately", "today", "critical", "emergency"],
    "medium": ["soon", "this week", "important"],
}

SUGGESTED_ACTIONS = {
    "scheduling": ["Block calendar", "Send invite", "Prepare agenda", "Set reminder"],
    "finance": ["Check budget", "Get approval", "Generate invoice", "Update records"],
    "technical": ["Diagnose issue", "Check resources", "Assign technician", "Document fix"],
    "safety": ["Conduct inspection", "File report", "Notify supervisor", "Update checklist"],
}


def detect_category(text: str) -> str:
    text = text.lower()
    for category, keywords in CATEGORY_KEYWORDS.items():
        for keyword in keywords:
            if keyword in text:
                return category
    return "general"


def detect_priority(text: str) -> str:
    text = text.lower()
    for priority, keywords in PRIORITY_KEYWORDS.items():
        for keyword in keywords:
            if keyword in text:
                return priority
    return "low"


def extract_entities(text: str) -> dict:
    entities = {}

    date_match = re.search(
        r"\b(today|tomorrow|\d{1,2}/\d{1,2}/\d{2,4})\b",
        text.lower()
    )
    if date_match:
        entities["date"] = date_match.group()

    person_match = re.search(r"(with|by|assign to)\s+([a-zA-Z ]+)", text)
    if person_match:
        entities["person"] = person_match.group(2).strip()

    return entities


def get_suggested_actions(category: str) -> list:
    return SUGGESTED_ACTIONS.get(category, [])


def classify_task(title: str, description: str = "") -> dict:
    combined_text = f"{title} {description}"

    category = detect_category(combined_text)
    priority = detect_priority(combined_text)
    entities = extract_entities(combined_text)
    actions = get_suggested_actions(category)

    return {
        "category": category,
        "priority": priority,
        "extracted_entities": entities,
        "suggested_actions": actions,
    }
