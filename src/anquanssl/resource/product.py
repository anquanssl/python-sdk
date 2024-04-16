from .abstract_resource import AbstractResource


class Product(AbstractResource):

    def product_list(self):
        return self.client.get("/product/list")
