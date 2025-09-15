# run_analysis.py

from quant.analyzer import analyze_books
from quant.io import save_summary_to_csv, save_summary_to_json

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

if __name__ == "__main__":
    # analyze
    summary, bests, best_val = analyze_books(My_trades, round_digits=4)

    # pretty print to screen (explain: this is the last-print you always want explained)
    print("Summary (formatted):")
    for name, data in summary.items():
        # f-string with formatting:
        # {data['total_pnl']:.4f} -> show 4 decimal places
        # {data['win_rate']:.2f}% -> show 2 decimal places + percent sign
        print(f"{name} -> PnL: {data['total_pnl']:.4f}, WinRate: {data['win_rate']:.2f}%, AvgPnL: {data['avg_pnl']:.4f}")

    # print best strategies and best value
    print("Best:", bests, f"(value = {best_val:.4f})")

    # save to files
    save_summary_to_csv(summary, "summary.csv")
    #summary — the dictionary your analyzer returned (mapping strategy → report). 
    # This is the data to save. 
    # "summary.csv" — a string telling the function the filename to write to. 
    # The quotes indicate it's text.
    #So the full line: “Run the CSV-saving function and give it the summary data and the 
    # filename summary.csv.”
    save_summary_to_json(summary, "summary.json")
    print("Saved summary.csv and summary.json")
