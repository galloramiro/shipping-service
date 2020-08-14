from unittest.mock import Mock

from requests import Response

from services.shipping_service import ShippingGateway, ShippingService


def test_shipping_gateway():
    gateway = ShippingGateway()

    shipping_options = gateway.get_shipping_options()

    assert shipping_options.status_code == 200
    assert shipping_options.json()


def test_shipping_service_same_costs_same_days():
    gateway = Mock(spec_set=ShippingGateway)
    expected_json = dict(shipping_options=[
        dict(name="Option 1", type="Delivery", cost=10, estimated_days=3),
        dict(name="Option 2", type="Custom", cost=10, estimated_days=3),
        dict(name="Option 3", type="Pickup", cost=10, estimated_days=3),
    ])
    stations_response = Mock(spec_set=Response)
    stations_response.json.return_value = expected_json

    gateway.get_shipping_options.return_value = stations_response

    shipping_service = ShippingService(gateway=gateway)

    best_shippings = shipping_service.get_best_shippings()

    expected_best_shippings = dict(shipping_options=[
        dict(name="Option 1", type="Delivery", cost=10, estimated_days=3),
        dict(name="Option 2", type="Custom", cost=10, estimated_days=3),
        dict(name="Option 3", type="Pickup", cost=10, estimated_days=3),
    ])

    assert best_shippings == expected_best_shippings


def test_shipping_service_same_cost_different_days():
    gateway = Mock(spec_set=ShippingGateway)
    expected_json = dict(shipping_options=[
        dict(name="Option 1", type="Delivery", cost=10, estimated_days=5),
        dict(name="Option 2", type="Custom", cost=10, estimated_days=2),
        dict(name="Option 3", type="Pickup", cost=10, estimated_days=3),
    ])
    stations_response = Mock(spec_set=Response)
    stations_response.json.return_value = expected_json

    gateway.get_shipping_options.return_value = stations_response

    shipping_service = ShippingService(gateway=gateway)

    best_shippings = shipping_service.get_best_shippings()

    expected_best_shippings = dict(shipping_options=[
        dict(name="Option 2", type="Custom", cost=10, estimated_days=2),
        dict(name="Option 3", type="Pickup", cost=10, estimated_days=3),
        dict(name="Option 1", type="Delivery", cost=10, estimated_days=5),
    ])

    assert best_shippings == expected_best_shippings


def test_shipping_service_same_days_different_costs():
    gateway = Mock(spec_set=ShippingGateway)
    expected_json = dict(shipping_options=[
        dict(name="Option 1", type="Delivery", cost=6, estimated_days=3),
        dict(name="Option 2", type="Custom", cost=5, estimated_days=3),
        dict(name="Option 3", type="Pickup", cost=10, estimated_days=3),
    ])
    stations_response = Mock(spec_set=Response)
    stations_response.json.return_value = expected_json

    gateway.get_shipping_options.return_value = stations_response

    shipping_service = ShippingService(gateway=gateway)

    best_shippings = shipping_service.get_best_shippings()

    expected_best_shippings = dict(shipping_options=[
        dict(name="Option 2", type="Custom", cost=5, estimated_days=3),
        dict(name="Option 1", type="Delivery", cost=6, estimated_days=3),
        dict(name="Option 3", type="Pickup", cost=10, estimated_days=3),
    ])

    assert best_shippings == expected_best_shippings


def test_shipping_service_different_days_different_costs():
    gateway = Mock(spec_set=ShippingGateway)
    expected_json = dict(shipping_options=[
        dict(name="Option 1", type="Delivery", cost=10, estimated_days=5),
        dict(name="Option 2", type="Custom", cost=5, estimated_days=3),
        dict(name="Option 3", type="Pickup", cost=7, estimated_days=2),
    ])
    stations_response = Mock(spec_set=Response)
    stations_response.json.return_value = expected_json

    gateway.get_shipping_options.return_value = stations_response

    shipping_service = ShippingService(gateway=gateway)

    best_shippings = shipping_service.get_best_shippings()

    expected_best_shippings = dict(shipping_options=[
        dict(name="Option 2", type="Custom", cost=5, estimated_days=3),
        dict(name="Option 3", type="Pickup", cost=7, estimated_days=2),
        dict(name="Option 1", type="Delivery", cost=10, estimated_days=5),
    ])

    assert best_shippings == expected_best_shippings
