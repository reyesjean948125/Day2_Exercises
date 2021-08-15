products = [
	"Sensodyne-100,Close Up-150,Colgate-135",
	"Safeguard-80,Protex-50,Kojic-135",
	"Surf-280,Ariel-350,Tide-635",
	"Clover-60,Piatos-20,Chippy-35",
	"Jelly bean-60,Hany-20,Starr-35"
]
# print(products)
print("[\n\"Sensodyne-100,Close Up-150,Colgate-135\",\n\"Safeguard-80,Protex-50,Kojic-135\",\n\"Surf-280,Ariel-350,Tide-635\",\n\"Clover-60,Piatos-20,Chippy-35\",\n\"Jelly bean-60,Hany-20,Starr-35\"\n]")

prod_type_split = []
cheapest_prod = [] # will handle output

# convert list product types to sub list
[prod_type_split.append(product.split(',')) for product in products]

for prod_type in prod_type_split:
	cheapest_prod_type = []

	[cheapest_prod_type.append(product.split('-')) for product in prod_type]

	
	cheapest_prod_type.sort(key = lambda x: int(x[1]))
	cheapest_prod.append(cheapest_prod_type[0])

def total_price(items):
	total = 0
	for item in items:
		total += int(item[1])
	return total

name_price = ['-'.join(prod) for prod in cheapest_prod]
print("Cheapest: " + ", ".join(name_price))
print("Total: " + str(total_price(cheapest_prod)))