from page_objects.CatalogPage import CatalogPage


def test_check_products_in_catalog(browser, url):
    browser.get(f"{url}/desktops")
    assert len(browser.find_elements(*CatalogPage.CATALOG_ELEMENTS)) == 12
