# tests/test_summary.py

from quant.summary import compute_strategy_summary

def test_empty_trades_returns_zero():
#test_empty_trades_returns_zero is the function name — pytest looks for functions whose 
# names start with test_ and will automatically run them.
    """
    If no trades are given, the summary should be zeros.
    """
    report = compute_strategy_summary([])
    assert report["total_pnl"] == 0.0
    assert report["wins"] == 0
    assert report["losses"] == 0
    assert report["total_trades"] == 0

def test_one_positive_trade():
    trades = [{"pnl": 10}]
    report = compute_strategy_summary(trades)
    assert report["total_pnl"] == 10.0
    assert report["wins"] == 1
    assert report["losses"] == 0
    assert report["win_rate"] == 100.0

def test_mixed_trades_rounding():
    trades = [{"pnl": 1.2345}, {"pnl": -0.2345}]
    report = compute_strategy_summary(trades, round_digits=3)
    assert report["total_pnl"] == 1.000
