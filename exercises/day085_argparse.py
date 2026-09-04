# Day 85: argparse CLI Parser
import argparse

def build_parser():
    parser = argparse.ArgumentParser(description="Daily Learning CLI Helper")
    parser.add_argument("--day", type=int, default=85, help="Day number")
    parser.add_argument("--status", choices=["done", "pending"], default="done")
    return parser

parser = build_parser()
args = parser.parse_args(["--day", "85", "--status", "done"])
print(f"Parsed arguments: Day={args.day}, Status={args.status}")
