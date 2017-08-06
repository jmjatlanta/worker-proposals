from pprint import pprint
from bitshares import BitShares
from bitshares.instance import set_shared_bitshares_instance
from bitshares.vesting import Vesting
from bitshares.price import Price
from bitshares.market import Market
from bitshares.amount import Amount

account = "alfredo-worker"
proposer = "oxarbitrage.a699"
vesting_id = "1.13.1609"

bitshares = BitShares(
    nobroadcast=False,
    bundle=True,
    proposer=proposer,
    proposal_expiration=60 * 60 * 24 * 2,
)
set_shared_bitshares_instance(bitshares)
market = Market("USD:BTS")
price = market.ticker()["quoteSettlement_price"]

bitshares.wallet.unlock("")
vesting = Vesting(vesting_id)

print("Claiming Vesting Balance: %s" % vesting.claimable)
bitshares.vesting_balance_withdraw(
    vesting["id"],
    amount=vesting.claimable,
    account=account
)

print("Buying as much bitUSD at price up to %s or %s" % (
    price * 0.90, (price * 0.90).copy().invert()
))
market.buy(
    price * 0.9,
    Amount(6400, "USD"),
    killfill=True,
    account=account
)

print("Worker alfredo payment - month 1")
bitshares.transfer(
    "oxarbitrage.a699",
    6400, "USD",
    account=account
)

pprint(bitshares.broadcast())