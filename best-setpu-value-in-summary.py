def compute_strategy_summary(trades: list, round_digits: int = 2) -> dict:
    """
    Compute summary statistics for one strategy.
    trades: list of dicts (each trade can have "pnl")
    round_digits: how many decimals to round the totals to
    returns: dictionary with total_pnl, wins, losses, total_trades, win_rate, avg_pnl
    """
    total_pnl = 0.0
    wins = 0
    losses = 0

    for trade in trades:
        pnl = float(trade.get("pnl", 0.0))
        total_pnl += pnl
        if pnl > 0:
            wins += 1
        else:
            losses += 1

    total_pnl = round(total_pnl, round_digits)
    total_trades = wins + losses

    if total_trades == 0:
        win_rate = 0.0
        avg_pnl = 0.0
    else:
        win_rate = round((wins / total_trades) * 100, round_digits)
        avg_pnl = round(total_pnl / total_trades, round_digits)

    return {
        "total_pnl": total_pnl,
        "wins": wins,
        "losses": losses,
        "total_trades": total_trades,
        "win_rate": win_rate,
        "avg_pnl": avg_pnl
    }


def analyze_books(books: dict,
                  metric: str = "total_pnl",
                  higher_is_better: bool = True,
                  min_trades: int = 0,
                  round_digits: int = 2) -> tuple:
    """
    Analyze multiple strategy books and return:
      - summary: dict mapping strategy_name -> report (dict)
      - best_list: list of strategy names that are best by chosen metric
      - best_value: the numeric value of that metric (or None if none)
    Parameters:
      books: dict of strategy_name -> list of trades
      metric: which key in the report to use for comparison
      higher_is_better: True if bigger numbers are better, False if smaller better
      min_trades: ignore strategies with fewer than min_trades trades
      round_digits: how many decimals for rounding numbers
    """
    # Validate metric quickly
    allowed_metrics = {"total_pnl", "win_rate", "avg_pnl"}
    if metric not in allowed_metrics:
        raise ValueError(f"metric must be one of {allowed_metrics}")

    summary = {}

    # Build summary for each strategy (skip if below min_trades)
    for strategy_name, trades in books.items():
        report = compute_strategy_summary(trades, round_digits=round_digits)
        if report["total_trades"] < min_trades:
            # skip strategies that don't meet minimum trades
            continue
        summary[strategy_name] = report

    # If nothing to compare, return empty results
    if not summary:
        return {}, [], None

    best_val = None
    best_list = []

    for name, report in summary.items():
        val = report.get(metric, 0.0)  # safe fetch

        if best_val is None:
            best_val = val
            best_list = [name]
        else:
            if higher_is_better:
                if val > best_val:
                    best_val = val
                    best_list = [name]
                elif val == best_val:
                    best_list.append(name)
            else:
                if val < best_val:
                    best_val = val
                    best_list = [name]
                elif val == best_val:
                    best_list.append(name)

    return summary, best_list, best_val


My_trades = {
    "Strategy A": [
        {"stock": "RELI", "entry": 400, "exit": 347.5, "pnl": 347.5 - 400},
        {"stock": "TATA",  "entry": 97,  "exit": 105,   "pnl": 105 - 97}
    ],
    "Strategy B": [
        {"stock": "RCOM", "entry": 6983.76, "exit": 6982.74, "pnl": 6982.74 - 6983.76},
        {"stock": "BPCL", "entry": 56,      "exit": 84,      "pnl": 84 - 56}
    ],
    "Strategy C": [
        {"stock": "X", "entry": 1, "exit": 2, "pnl": 1}
    ]
}

# default behavior: best by total_pnl
summary, best_list, best_val = analyze_books(My_trades, round_digits=4)
print(summary)
print("Best:", best_list, best_val)

# ignore strategies with fewer than 2 trades
s2, b2, v2 = analyze_books(My_trades, min_trades=2, round_digits=4)
print("Skipped single-trade strategies:", s2.keys())

# best by win_rate (higher is better)
s3, b3, v3 = analyze_books(My_trades, metric="win_rate", higher_is_better=True, round_digits=4)
print("Best by win rate:", b3, v3)

# Quick check: does compute_strategy_summary use the round_digits parameter?
