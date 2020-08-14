from typing import Dict

import requests
from requests import Response


class ShippingGateway:
    _BASE_URL = "https://shipping-options-api.herokuapp.com/v1/shipping_options"

    def get_shipping_options(self) -> Response:
        return requests.get(self._BASE_URL)


class ShippingService:
    def __init__(self, gateway: ShippingGateway):
        self._gateway = gateway

    def get_best_shippings(self) -> Dict:
        shipping_options = self._gateway.get_shipping_options().json()
        sorted_shippings = sorted(shipping_options["shipping_options"], key=lambda k: (k["cost"], k["estimated_days"]))
        return dict(shipping_options=sorted_shippings)


def shipping_service_factory() -> ShippingService:
    return ShippingService(gateway=ShippingGateway())
