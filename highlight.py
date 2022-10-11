import fitz

### READ IN PDF
doc = fitz.open("random.pdf")

for page in doc:
    ### SEARCH
    text = "information"
    text_instances = page.searchFor(text)

    ### HIGHLIGHT
    for inst in text_instances:
        highlight = page.addHighlightAnnot(inst)
        highlight.update()


### OUTPUT
doc.save("output.pdf", garbage=4, deflate=True, clean=True)