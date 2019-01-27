class Product():
	product_list={}
	name=None
	price=0
	id=0

	def add_product(self,id,name,price):
		temp=[]
		temp.append(name)
		temp.append(price)
		self.product_list[id]=temp

	def remove_product(self,id):
		del self.product_list[id]

	def show_product(self):
		print(self.product_list)


class Inventory():

	def start_inventory(self,class_reference):

		while True:
			print("1:add product\n2:remove product\n3:show products\n4:exit")
			choice=int(input("enter your choice"))

			if choice == 1:
				name = input("enter the name of the product")
				price = input("enter the price of the product")
				id_product=input("enter the id of the product")
				class_reference.add_product(id_product,name,price)
			
			elif choice == 2:
				id_product = input("enter the id of the product")
				class_reference.remove_product(id_product)
			
			elif choice == 3:
				class_reference	.show_product()
			
			elif choice == 4:
				break


if __name__ == "__main__":
	start = Inventory()
	product = Product()

	start.start_inventory(product)

	print("bye")


		