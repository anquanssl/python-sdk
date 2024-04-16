from abc import ABC

from ..client import Client


class AbstractResource(ABC):
    def __init__(self, client: Client) -> None:
        self.client = client
