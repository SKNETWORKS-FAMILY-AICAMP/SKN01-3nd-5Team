from abc import ABC, abstractmethod


class ProductService(ABC):
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def createProduct(self, productName, productLocation, productActivity, productDining, productPrice, productImageName):
        pass