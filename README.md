# product_management
product management quiz 
                                              #Django testing

1 Create a django project with the name product_management and connect to postgresql database name product_management_db.(15 min = 4 points)

2 Configure the route url for create category, list all categories, update a category page.(15 min = 4 points)

3 Configure the route url for create product, list all products, update a product page.(15 min = 4 point)

4 Create models based on: (15 min = 4 points)

  #Category:

      Name: length=100, not null

      Created at: default=now, not null

      Updated at:default=null, allowed null

      Visible:default=false, not null

  #Product

      Title: length=200, not null

      Description: text, allowed null

      Created at: default=now, not null

      Updated at:  default=null, allowed null

      Publish: default=false, not null

      Category: foreignkey of Category


5 Implement create category. (30 min = 8 point)

6 Implement list all categories and delete category. (45 min = 12 points)

7 Implement  search category by (visible). (15 min = 4 points)

8 Implement create product. (30 min = 8 points)

9 Implement list all products and delete product. (45 min = 12 points)

10 Implement update product. (30 min = 8 points)

11 Implement update category (category information and add, remove products within a category). (30 min = 8 point)

12 Implement search products by (title, created at, category name). (45 min = 12 points)

13 Implement sort products by title(ascending, descending). (45 min = 12  points)


