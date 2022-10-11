import fitz
import openpyxl

### READ IN PDF
doc = fitz.open("history-of-western-phil.pdf")

# for page in doc:
#     ### SEARCH
#     text = "information"
#     text_instances = page.searchFor(text)

#     ### HIGHLIGHT
#     for inst in text_instances:
#         highlight = page.addHighlightAnnot(inst)
#         highlight.update()
 
# Define variable to load the dataframe
dataframe = openpyxl.load_workbook("index.xlsx")
 
# Define variable to read sheet
dataframe1 = dataframe.active
 
# Iterate the loop to read the cell values
for row in dataframe1.iter_cols(1, 4):
    for col in range(4, dataframe1.max_column):
        keyword = row[2].value
        print(type(keyword), keyword)
        print(row[col].value)

### OUTPUT
doc.save("output.pdf", garbage=4, deflate=True, clean=True)