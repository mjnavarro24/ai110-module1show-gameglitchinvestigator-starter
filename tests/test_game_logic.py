from logic_utils import check_guess, parse_guess, update_score, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    # FIX: Used agent to check for tuple result; check_guess returns (outcome, message)
    assert check_guess(50, 50) == ("Win", "🎉 Correct!")

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    # FIX: Used agent to check for tuple result; check_guess returns (outcome, message)
    assert check_guess(60, 50) == ("Too High", "📉 Go LOWER!")

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    # FIX: Used agent to check for tuple result; check_guess returns (outcome, message)
    assert check_guess(40, 50) == ("Too Low", "📈 Go HIGHER!")

# Used agent to create new test case
def test_parse_guess_below_range():
    # Guess "0" with range 1-100 is below the low bound -> rejected
    # parse_guess returns (ok, guess_int, error_message)
    assert parse_guess("0", 1, 100) == (False, None, "Guess must be between 1 and 100.")

# Used agent to create new test case
def test_parse_guess_at_high_bound():
    # Guess "100" with range 1-100 is valid (inclusive high bound) -> accepted
    assert parse_guess("100", 1, 100) == (True, 100, None)

# Used agent to create new test case
def test_parse_guess_not_a_number():
    # Non-numeric input "hello" cannot be parsed -> rejected
    assert parse_guess("hello", 0, 100) == (False, None, "That is not a number.")

# Used agent to create new test case
def test_update_score_too_high_decreases():
    # A "Too High" outcome with an even attempt number should still lose 5 points
    # (the old divisible-by-2 bonus was removed)
    assert update_score(20, "Too High", 2) == 15
# Used agent to create new test case
def test_update_score_win_first_guess():
    # Winning on the first guess (attempt_number=1) -> 100 - 10*1 = 90 points
    assert update_score(0, "Win", 1) == 90

# Used agent to create new test case
def test_update_score_win_clamped_to_10():
    # A high attempt number would compute 100 - 10*12 = -20, but the score
    # for a win is clamped to a minimum of 10 points
    assert update_score(0, "Win", 12) == 10

# Used agent to create new test case
def test_range_easy():
    assert get_range_for_difficulty("Easy") == (1, 20)

# Used agent to create new test case
def test_range_normal():
    assert get_range_for_difficulty("Normal") == (1, 50)

# Used agent to create new test case
def test_range_hard():
    assert get_range_for_difficulty("Hard") == (1, 100)

# Used agent to create new test case
def test_range_unknown_defaults():
    # Any unrecognized difficulty falls back to the default 1-100 range
    assert get_range_for_difficulty("Whatever") == (1, 100)

def test_parse_guess_decimal():
    # Guess "1.5" with range 1-100
    # parse_guess returns (ok, guess_int, error_message)
    assert parse_guess("1.5", 1, 100) == (True, 1, None)