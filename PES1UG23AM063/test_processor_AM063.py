import pytest
from order_processor import calculate_discount, update_order_status

#Example test cases:
def test_regular_low_amount():
    assert calculate_discount("regular", 500) == 0

def test_premium_discount():
    assert calculate_discount("premium", 2000) == 200

#Write the rest of the test cases so that the code is 90- 100% covered.

def test_regular_high_amount():
    # Covers: regular customer, total_amount > 1000 (discount = 5%)
    assert calculate_discount("regular", 1500) == 1500 * 0.05

def test_vip_high_amount():
    # Covers: vip customer, total_amount > 5000 (discount = 20%)
    assert calculate_discount("vip", 6000) == 6000 * 0.2

def test_vip_low_amount():
    # Covers: vip customer, total_amount <= 5000 (discount = 10%)
    assert calculate_discount("vip", 4000) == 4000 * 0.1

def test_unknown_customer_type():
    # Covers: the 'else' block that raises a ValueError
    with pytest.raises(ValueError, match="Unknown customer type"):
        calculate_discount("unknown", 100)

# Tests for update_order_status to cover all branches

def test_pending_paid():
    # Covers: status == "pending" AND order["paid"] is True -> "processing"
    order = {"status": "pending", "paid": True, "items_available": False}
    assert update_order_status(order) == "processing"
    # Ensure the dictionary is updated (optional but good practice)
    assert order["status"] == "processing"

def test_pending_not_paid():
    # Covers: status == "pending" AND order["paid"] is False -> "awaiting_payment"
    order = {"status": "pending", "paid": False, "items_available": False}
    assert update_order_status(order) == "awaiting_payment"
    assert order["status"] == "awaiting_payment"

def test_processing_items_available():
    # Covers: status == "processing" AND order["items_available"] is True -> "shipped"
    order = {"status": "processing", "paid": True, "items_available": True}
    assert update_order_status(order) == "shipped"
    assert order["status"] == "shipped"

def test_processing_backorder():
    # Covers: status == "processing" AND order["items_available"] is False -> "backorder"
    order = {"status": "processing", "paid": True, "items_available": False}
    assert update_order_status(order) == "backorder"
    assert order["status"] == "backorder"

def test_other_status_no_change():
    # Covers: The final implicit 'else' where status is not "pending" or "processing"
    order = {"status": "shipped", "paid": True, "items_available": True}
    assert update_order_status(order) == "shipped"
    assert order["status"] == "shipped"
