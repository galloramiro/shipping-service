from services.shipping_service import shipping_service_factory

class ShippingApi:

    def get(self):
        shipping_service = shipping_service_factory()
        return shipping_service.get_best_shippings()
