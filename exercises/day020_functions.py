# Day 20: Functions and Default Arguments

# Safe default argument pattern
def append_log(entry: str, log_list=None):
    """Safely appends entry to a log list without shared state."""
    if log_list is None:
        log_list = []
    log_list.append(entry)
    return log_list

session_a = append_log("Login at 08:00")
session_a = append_log("Action performed", session_a)
session_b = append_log("New independent session")

print("Session A:", session_a)
print("Session B:", session_b)
