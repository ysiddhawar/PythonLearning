def compute_strategy_summary(trades: dict, round_digits = 2):
    total_pnl = 0
    wins = 0
    losses = 0

    for trade in trades:
        pnl = float(trade.get("pnl", 0))
        total_pnl += pnl
        if pnl > 0:
            wins = 1
        else:
            losses = 1
    
    total_pnl = round(total_pnl, round_digits)
    total_trades = wins + losses
    if total_trades == 0:
        win_rate = 0
        avg_pnl = 0
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
    
