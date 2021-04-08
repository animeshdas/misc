#!/usr/bin/env python3
########################################################################
# VSC Fix Marketplace
# Copyright (C) 2021-2025, Animesh Das <jobs4ani@gmail.com>.
# GNU Public Licence 3
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
########################################################################
# This script will fix vscode marketplace link.
# Below is sample outdated VSCodium marketplace link.
# "extensionsGallery": {
#     "serviceUrl": "https://open-vsx.org/vscode/gallery",
#     "itemUrl": "https://open-vsx.org/vscode/item"
#   }


import sys
import os.path
import json

if sys.platform.startswith("win"):
    file_path = os.environ['PROGRAMFILES'] + "\\VSCodium\\resources\\app\\product.json"
    if not os.path.isfile(file_path):
        file_path = os.environ['PROGRAMFILES(X86)'] + "\\VSCodium\\resources\\app\\product.json"

elif sys.platform.startswith("linux"):
    file_path = "/usr/share/codium/resources/app/product.json"
elif sys.platform.startswith("darwin"):
    file_path = "/Applications/VSCodium.app/Contents/Resources/app/product.json"

# Only uncomment below line to manually configure, if automatic detection doesn't work above.
# Below is typical path for product.json in MacOSX.
# file_path = "/Applications/VSCodium.app/Contents/Resources/app/product.json"

# URLs
serviceUrl = "https://marketplace.visualstudio.com/_apis/public/gallery"
cacheUrl = "https://vscode.blob.core.windows.net/gallery/index"
itemUrl = "https://marketplace.visualstudio.com/items"
controlUrl = "https://az764295.vo.msecnd.net/extensions/marketplace.json"
recommendationsUrl = "https://az764295.vo.msecnd.net/extensions/workspaceRecommendations.json.gz"


def yesno(question):
    """Simple Yes/No Function."""
    prompt = f'{question} ? (y/n): '
    ans = input(prompt).strip().lower()
    if ans not in ['y', 'n']:
        print(f'{ans} is invalid, please try again...')
        return yesno(question)
    if ans == 'y':
        return True
    return False

def change_product_marketplace():
    with open(file_path, "r") as f:
        config = json.load(f)
        config["extensionsGallery"]["serviceUrl"] = serviceUrl
        config["extensionsGallery"]["cacheUrl"] = cacheUrl
        config["extensionsGallery"]["itemUrl"] = itemUrl
        config["extensionsGallery"]["controlUrl"] = controlUrl
        config["extensionsGallery"]["recommendationsUrl"] = recommendationsUrl
    with open(file_path, "w") as f:
        json.dump(config, f, indent=2)


def main():
    """Run main function."""
    print(f"Checking if {file_path} exists..... ", end = '')
    if os.path.isfile(file_path):
       print("FOUND!")
    else:
        print("NOT FOUND!")
        print("INFO: Please configure product.json correct location in this script.")
        sys.exit("Execution terminated!")
    print("")
    ans = yesno("Are you sure you want to fix the marketplace link in the file ")
    if ans is True:
        print("Fixing......", end = '')
        change_product_marketplace()
        print("DONE")
        print("Bye bye!!!")
    else: print("Bye bye!!!")


if __name__ == '__main__':
    main()
