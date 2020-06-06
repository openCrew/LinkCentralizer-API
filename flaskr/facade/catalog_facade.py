from services.catalog_service import CatalogService


class CatalogFacade:
    def __init__(self) -> None:
        self._catalog_service = CatalogService()

    def save_catalog(self, data) -> None:
        pass
