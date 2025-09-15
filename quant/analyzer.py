# quant/analyzer.py

from .summary import compute_strategy_summary

def analyze_books(books: dict, metric="total_pnl", higher_is_better=True, min_trades=0, round_digits=2):
    allowed_metrics = {"total_pnl", "win_rate", "avg_pnl"}
    if metric not in allowed_metrics:
        raise ValueError(f"metric must be one of {allowed_metrics}")

    summary = {}
    for name, trades in books.items():
        report = compute_strategy_summary(trades, round_digits=round_digits)
        if report["total_trades"] < min_trades:
            continue
        summary[name] = report

    if not summary:
        return {}, [], None

    best_val = None
    best_list = []
    for name, report in summary.items():
        val = report.get(metric, 0.0)
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
