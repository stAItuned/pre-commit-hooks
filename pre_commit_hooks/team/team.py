from ..utils import get_frontmatter, ok, print_error


def main():
    VALID_TEAMS = ["Writers", "Tech", "Marketing"]
    post = get_frontmatter()
    teams: list[str] = post.get("team", None)
    if(teams is None or not isinstance(teams, list) or len(teams) == 0):
        return print_error("Team must be a non-empty array", True)
    mismatch = []
    for team in teams:
        if team not in VALID_TEAMS:
            mismatch.append(team)
    if(len(mismatch) > 0):
        return print_error(f"Invalid team name(s): {','.join(mismatch)}", True)
    ok()
