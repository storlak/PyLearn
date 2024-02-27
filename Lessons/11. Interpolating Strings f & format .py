# f string
open_ = 98
high = 100
low = 35
close = 98
print(f"open: {open_}, {high}, {low}, {close}")
print(f"open: {open_}, close:{close}, delta:{open_ - close}")

# format
print("open_: {}, high: {}, low: {}, close: {}".format(open_, high, low, close))

bid = 1.5760
ask = 1.5763
print("bid: {}, ask: {}, spread: {}".format(bid, ask, ask-bid))
# or
print(f"bid: {bid}, ask: {ask}, spread:{ask-bid}")
# to print with 4 digits
print("bid: {:.4f}, ask: {:.4f}, spread: {:.4f}".format(bid, ask, ask-bid)) # :.4f shows digit count
print(f"bid: {bid:.4f}, ask: {ask:.4f}, spread:{(ask-bid):.4f}") # to print 4 digits :.4f

