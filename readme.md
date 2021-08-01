# Daimler technical coding test 

Instructions of a Programming script that satisfies the requirements of the coding test.
Could be mainly written in Python / Scala / C# 
It is highly appreciate the implementation with descriptions and uses at least one lambda functions

# Functionality

By running the code, the input file Daimler-test-data.json will be read
and then ask the user to insert a sku code in order to find its closest similar skus.

It will check for irregularities in the format of the inserted sku code and throw an exception if one was found.

Then, it creates a matching score with all skus depending on digit importance
and prints out the 10 most similar skus.

Include also in a theorical way what algorithim could be the best case for finding recomendations.

# Example

The following will be the output if sku-123 is inserted as an input.

sku-123: {"att-a": "att-a-2", "att-b": "att-b-13", "att-c": "att-c-7", "att-d": "att-d-1", "att-e": "att-e-7", "att-f": "att-f-10", "att-g": "att-g-1", "att-h": "att-h-8", "att-i": "att-i-7", "att-j": "att-j-1"} is more similar to 
sku-12507: {"att-a": "att-a-2", "att-b": "att-b-13", "att-c": "att-c-7", "att-d": "att-d-1", "att-e": "att-e-12", "att-f": "att-f-5", "att-g": "att-g-6", "att-h": "att-h-8", "att-i": "att-i-15", "att-j": "att-j-8"} than to 
sku-11992: {"att-a": "att-a-11", "att-b": "att-b-5", "att-c": "att-c-4", "att-d": "att-d-1", "att-e": "att-e-7", "att-f": "att-f-13", "att-g": "att-g-1", "att-h": "att-h-8", "att-i": "att-i-7", "att-j": "att-j-4"} than to 
sku-954: {"att-a": "att-a-2", "att-b": "att-b-13", "att-c": "att-c-7", "att-d": "att-d-13", "att-e": "att-e-1", "att-f": "att-f-10", "att-g": "att-g-3", "att-h": "att-h-15", "att-i": "att-i-6", "att-j": "att-j-3"} than to 
sku-3613: {"att-a": "att-a-2", "att-b": "att-b-13", "att-c": "att-c-8", "att-d": "att-d-1", "att-e": "att-e-13", "att-f": "att-f-5", "att-g": "att-g-1", "att-h": "att-h-3", "att-i": "att-i-10", "att-j": "att-j-8"} than to 
sku-4196: {"att-a": "att-a-2", "att-b": "att-b-13", "att-c": "att-c-5", "att-d": "att-d-13", "att-e": "att-e-7", "att-f": "att-f-9", "att-g": "att-g-1", "att-h": "att-h-11", "att-i": "att-i-13", "att-j": "att-j-4"} than to 
sku-7956: {"att-a": "att-a-2", "att-b": "att-b-13", "att-c": "att-c-8", "att-d": "att-d-12", "att-e": "att-e-7", "att-f": "att-f-7", "att-g": "att-g-1", "att-h": "att-h-6", "att-i": "att-i-1", "att-j": "att-j-13"} than to 
sku-13091: {"att-a": "att-a-2", "att-b": "att-b-13", "att-c": "att-c-10", "att-d": "att-d-14", "att-e": "att-e-7", "att-f": "att-f-1", "att-g": "att-g-12", "att-h": "att-h-6", "att-i": "att-i-12", "att-j": "att-j-1"} than to 
sku-9697: {"att-a": "att-a-2", "att-b": "att-b-13", "att-c": "att-c-3", "att-d": "att-d-4", "att-e": "att-e-3", "att-f": "att-f-10", "att-g": "att-g-1", "att-h": "att-h-12", "att-i": "att-i-6", "att-j": "att-j-2"} than to 
sku-11470: {"att-a": "att-a-2", "att-b": "att-b-13", "att-c": "att-c-15", "att-d": "att-d-3", "att-e": "att-e-2", "att-f": "att-f-10", "att-g": "att-g-1", "att-h": "att-h-3", "att-i": "att-i-11", "att-j": "att-j-13"} than to 
sku-1023: {"att-a": "att-a-2", "att-b": "att-b-13", "att-c": "att-c-8", "att-d": "att-d-13", "att-e": "att-e-8", "att-f": "att-f-10", "att-g": "att-g-12", "att-h": "att-h-2", "att-i": "att-i-8", "att-j": "att-j-1"}
