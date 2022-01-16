from item import item

print("Starting item watcher with defualt items..")

url = "https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149"
obj = item("PS5", "BestBuy", url, [])
obj.connect()