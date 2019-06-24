
import shutil
import os
import sys
import json
from utilsx import file_writer
import logging
import glob

from zipfile import ZipFile
from source import templates
from source import config_data_map

from generators.product_generators import generate_products
from generators.product_generators import generate_supplier_product
from generators.product_generators import generate_product_media
from generators.product_generators import generate_product_price
from generators.product_generators import generate_product_product_group
from generators.product_generators import generate_images
from generators.product_generators import generate_product_attribute

from generators.group_generators import generate_product_group
from generators.group_generators import generate_brand_group

from generators.global_generators import generate_colours

shutil.rmtree('configs')
os.mkdir('configs')

generated_data = generate_products.generate()
products_array = generated_data["products_array"]
product_image_map = generated_data["product_image_map"]

generate_product_media.generate(product_image_map)
generate_supplier_product.generate(products_array)
generate_product_price.generate()
generate_product_group.generate()
generate_brand_group.generate()

generate_product_product_group.generate()
generate_images.generate()

generate_product_attribute.generate(products_array)
generate_colours.generate()

# create a zipped object
zipObj = ZipFile('configs/configs.zip', 'w')
workdir = os.getcwd()
for file_path in glob.glob(workdir+"/configs/*.xml"):
    zipObj.write(file_path)
zipObj.close()

# print(json.dumps(product_image_map, indent=4))
# json.dumps(products_array)
