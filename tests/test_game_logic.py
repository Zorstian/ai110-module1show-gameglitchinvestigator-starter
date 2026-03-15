from logic_utils import get_range_for_difficulty, parse_guess, check_guess, update_score


# --- get_range_for_difficulty ---

def test_range_easy():
    assert get_range_for_difficulty("Easy") == (1, 20)

def test_range_normal():
    assert get_range_for_difficulty("Normal") == (1, 50)

def test_range_hard():
    assert get_range_for_difficulty("Hard") == (1, 100)

def test_range_unknown_defaults_to_normal():
    assert get_range_for_difficulty("Unknown") == (1, 50)


# --- parse_guess ---

def test_parse_guess_none():
    ok, val, err = parse_guess(None, 1, 100)
    assert ok is False
    assert val is None
    assert err == "Enter a guess."

def test_parse_guess_empty():
    ok, val, err = parse_guess("", 1, 100)
    assert ok is False
    assert val is None
    assert err == "Enter a guess."

def test_parse_guess_not_a_number():
    ok, val, err = parse_guess("abc", 1, 100)
    assert ok is False
    assert val is None
    assert err == "That is not a number."

def test_parse_guess_valid():
    ok, val, err = parse_guess("42", 1, 100)
    assert ok is True
    assert val == 42
    assert err is None

def test_parse_guess_decimal_truncates():
    ok, val, _ = parse_guess("7.9", 1, 100)
    assert ok is True
    assert val == 7

def test_parse_guess_below_range():
    ok, _, err = parse_guess("0", 1, 100)
    assert ok is False
    assert "between 1 and 100" in err

def test_parse_guess_above_range():
    ok, _, err = parse_guess("101", 1, 100)
    assert ok is False
    assert "between 1 and 100" in err

def test_parse_guess_at_boundary_low():
    ok, val, _ = parse_guess("1", 1, 100)
    assert ok is True
    assert val == 1

def test_parse_guess_at_boundary_high():
    ok, val, _ = parse_guess("100", 1, 100)
    assert ok is True
    assert val == 100


# --- check_guess ---

def test_check_guess_win():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message

def test_check_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_check_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


# --- update_score ---

def test_update_score_win_early():
    # attempt 1: 100 - 10*(1+1) = 80 points
    score = update_score(0, "Win", 1)
    assert score == 80

def test_update_score_win_minimum_points():
    # attempt 10: 100 - 10*(10+1) = -10, floored to 10
    score = update_score(0, "Win", 10)
    assert score == 10

def test_update_score_too_high_subtracts():
    score = update_score(100, "Too High", 1)
    assert score == 95

def test_update_score_too_low_subtracts():
    score = update_score(100, "Too Low", 1)
    assert score == 95

def test_update_score_unknown_outcome_unchanged():
    score = update_score(100, "Unknown", 1)
    assert score == 100
