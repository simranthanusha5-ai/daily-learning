# Day 19: Structural Pattern Matching

def handle_command(command: str):
    tokens = command.split()
    match tokens:
        case ["quit" | "exit"]:
            return "Exiting application..."
        case ["load", filename]:
            return f"Loading file from: {filename}"
        case ["save", filename, ("--force" | "-f")]:
            return f"Force saving to {filename}"
        case ["save", filename]:
            return f"Saving to {filename}"
        case _:
            return f"Unknown command: '{command}'"

print(handle_command("load data.csv"))
print(handle_command("save backup.json --force"))
print(handle_command("quit"))
