import shopify

STORE = "YOUR_STORE"
API_KEY = "YOUR_API_KEY"
API_PASS = "YOUR_API_PASSWORD"
API_SHARED = "YOUR_API_SHARED_SECRET"

shop_url = "https://%s:%s@%s.myshopify.com/admin" % (
    API_KEY, API_PASS, STORE)

shopify.ShopifyResource.set_site(shop_url)
