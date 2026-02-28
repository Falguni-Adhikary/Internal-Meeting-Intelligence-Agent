def generate_summary(text):
    sentences = text.split(".")
    summary = ". ".join(sentences[:3])
    return f"High-level summary of discussion:\n{summary}"


def extract_decisions(text):
    decisions = []
    for line in text.split("."):
        if "decided" in line.lower() or "approved" in line.lower():
            decisions.append(line.strip())
    return decisions[:5]


def extract_action_items(text):
    actions = []
    for line in text.split("."):
        if "will" in line.lower() or "action" in line.lower():
            actions.append(line.strip())
    return actions[:5]


def extract_risks(text):
    risks = []
    for line in text.split("."):
        if "risk" in line.lower() or "issue" in line.lower() or "concern" in line.lower():
            risks.append(line.strip())
    return risks[:5]


def generate_next_steps():
    return [
        "Review assigned action items",
        "Set deadlines for completion",
        "Schedule follow-up meeting",
        "Track progress in internal system"
    ]