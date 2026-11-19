"""CLI for Belief Tracker."""
import argparse
from .core import BeliefRevisionTracker

def main():
    parser = argparse.ArgumentParser(description="Agent Belief Revision Tracker CLI")
    parser.add_argument("--demo", action="store_true", help="Run belief tracker demo")
    args = parser.parse_args()

    tms = BeliefRevisionTracker()
    tms.add_premise("db_online", active=True)
    tms.add_premise("auth_valid", active=True)
    tms.add_justification("can_query", ["db_online", "auth_valid"])
    print(f"Initial can_query active: {tms.is_believed('can_query')}")

    tms.retract_premise("db_online")
    print(f"After db_online retracted, can_query active: {tms.is_believed('can_query')}")

if __name__ == "__main__":
    main()
