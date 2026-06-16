#FIX: Used agent to refactor get_range_for_difficulty from app.py into logic_utils.py.
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        #FIX: Used agent to correct range to 1-50.
        return 1, 50
    if difficulty == "Hard":
        #FIX: Used agent to correct range to 1-100.
        return 1, 100
    return 1, 100


#FIX: Used agent to refactor parse_guess from app.py into logic_utils.py.
#FIX: ClaudeCode suggested out of range guesses be checked in this function.
def parse_guess(raw: str, low: int, high: int):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    #FIX: Asked Claude Code about where to implement the check for out of range guesses.
    if value < low or value > high:
        return False, None, f"Guess must be between {low} and {high}."

    return True, value, None


#FIX: Used agent to refactor check_guess from app.py into logic_utils.py.
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess < secret:
            #FIX: ClaudeCode pointed out that the outcomes were reversed, resulting in logic being reversed in update_score.
            return "Too Low", "📈 Go HIGHER!"
        else:
            #FIX: ClaudeCode pointed out that the outcomes were reversed, resulting in logic being reversed in update_score.
            return "Too High", "📉 Go LOWER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


#FIX: Used agent to refactor update_score from app.py into logic_utils.py.
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        #FIX: When ClaudeCode explained this function to me I noticed that the scoring was wrong and it also recommended removing the +1 to get the max # of points.
        points = 100 - 10 * (attempt_number)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        #FIX: Removed the divisible-by-2 check that added 5; a wrong guess should always lose 5.
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
