import json
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent

USERS_FILE = BASE_DIR / "users.json"
CART_FILE = BASE_DIR / "user_cart.json"
DB_FILE = BASE_DIR / "db.json"


def _load(path: Path) -> dict:
    if not path.exists():
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _save(path: Path, data: dict) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def save_user(user_id: int, name: str, phone: str) -> None:
    users = _load(USERS_FILE)
    users[str(user_id)] = {"name": name, "phone": phone}
    _save(USERS_FILE, users)


def get_products(category: str) -> list[dict]:
    db = _load(DB_FILE)
    return db.get(category, [])


def add_to_cart(user_id: int, product: dict) -> None:
    cart = _load(CART_FILE)
    uid = str(user_id)
    if uid not in cart:
        cart[uid] = []
    cart[uid].append(product)
    _save(CART_FILE, cart)


def get_cart(user_id: int) -> list[dict]:
    cart = _load(CART_FILE)
    return cart.get(str(user_id), [])
