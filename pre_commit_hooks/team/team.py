import sys
from .utils import get_frontmatter, print_error


def main():
    VALID_TEAMS = ["Writers", "Tech", "Marketing"]
    post = get_frontmatter()
    teams: list[str] = post.get("team", None)
    if(teams is None or not isinstance(teams, list) or len(teams) == 0):
        print("team must be a non-empty array")
        sys.exit(1)
    mismatch = []
    for team in teams:
        if team not in VALID_TEAMS:
            mismatch.append(team)
    if(len(mismatch) > 0):
        print_error(f"Invalid team name(s): {','.join(mismatch)}")
        sys.exit(1)
    sys.exit(0) // ok
