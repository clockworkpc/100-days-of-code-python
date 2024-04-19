"""Day 9: Auction Engine"""


class Auction:
    def __init__(self):
        self.bids = {}

    def bid(self, hsh):
        name = list(hsh.keys())[0]
        amount = list(hsh.values())[0]
        ok = name is not None and amount > self.highest_bid()
        status = "ok" if ok else "rejected"

        if ok:
            self.bids[name] = amount

        return {"status": status, name: amount}

    def batch_bids(self, bids_hsh):
        for k, v in bids_hsh.items():
            hsh = {k: v}
            self.bid(hsh)

    def find_highest_bidder(self):
        return max(self.bids, key=self.bids.get)

    def highest_bid(self):
        return max(self.bids.values()) if len(self.bids) > 0 else 0


def main():
    g = Auction()
    g.run()


if __name__ == "__main__":
    main()
