import os
import csv
import random
import sys
import tempfile
from detotime import detotime
from getpass import getpass
from colorama import init, Fore, style

init(autoreset=True)

ACCOUNTS_FILE = "accounts.txt"
TRANSACTIONS_FILE ="transaction.txt"
ACCOUNT_FILEDS = ["account", "name", "pin", "bakance", "status", "created_at"]

#---------------------KOUSHIK GOSHWAMI---------------------
def ensure_files():
    if not os.path.exists(ACCOUNTS_FILE):
        open(ACCOUNTS_FILE, "w").close()
    if not os.path.exists(TRANSACTIONS_FILE):
        open(TRANSACTIONS_FILE, "w").close()


def read_accounts():
    accounts = {}
    if not os.path.exists(ACCOUNTS_FILE):
        return accounts

    with open(ACCOUNTS_FILE, newline="") as f:
        reader = csv.reader(f, delimiter="|")
        for row in reader:
            if not row:
                continue
            record = dict(zip(ACCOUNT_FIELDS, row))
            record["balance"] = float(record["balance"])
            accounts[record["account"]] = record
    return accounts

def write_accounts(accounts):
    fd, tmp = tempfile.mkstemp()
    with os.fdopen(fd, "w", newline="") as f:
        writer = csv.writer(f, delimiter="|")
        for acct in accounts.values():
            writer.writerow([acct[k] if k != "balance" else f"{acct['balance']:.2f}" for k in ACCOUNT_FIELDS])
    os.replace(tmp, ACCOUNTS_FILE)

def log_transaction(account_from, account_to, ttype, amount, balance_after, desc=""):
    ts = datetime.utcnow().isoformat()
    with open(TRANSACTIONS_FILE, "a", newline="") as f:
        writer = csv.writer(f, delimiter="|")
        writer.writerow([ts, account_from or "", account_to or "", ttype, f"{amount:.2f}", f"{balance_after:.2f}", desc])

def generate_account_number(accounts):
    while True:
        acc = "".join(str(random.randint(0, 9)) for _ in range(13))
        if acc not in accounts and acc[0] != "0":
            return acc
