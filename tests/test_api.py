from api import ShippingApi

def test_api():
    best_shippings = ShippingApi().get()
    import ipdb; ipdb.set_trace()