from typing import Literal
from ..utils import Entry, get_frontmatter, ok, print_error


def single_entry(entry: Entry) -> Literal[1, 0]:
    VALID_TEAMS = ["Writers", "Tech", "Marketing"]
    post = entry.post
    teams: list[str] = post.get("team", None)
    if(teams is None or not isinstance(teams, list) or len(teams) == 0):
        return print_error(entry, "Team must be a non-empty array", True)
    mismatch = []
    for team in teams:
        if team not in VALID_TEAMS:
            mismatch.append(team)
    if(len(mismatch) > 0):
        return print_error(entry, f"Invalid team name(s): {','.join(mismatch)}", True)
    return ok(entry)

def main():
    errors = 0
    for entry in get_frontmatter():
        errors += single_entry(entry)
    return errors
