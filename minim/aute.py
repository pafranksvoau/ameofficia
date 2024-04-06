def approve_2():
    """Approve a document with 2 signatures."""
    from google.cloud import documentai

    # You must set the api_endpoint if you use a location other than 'us'.
    opts = {"api_endpoint": "eu-documentai.googleapis.com"}

    client = documentai.DocumentProcessorServiceClient(client_options=opts)

    # The full resource name of the processor, e.g.:
    # projects/project-id/locations/location/processor/processor-id
    # You must create new processors in the Cloud Console first
    name = "projects/YOUR_PROJECT_ID/locations/YOUR_PROCESSOR_LOCATION/processors/YOUR_PROCESSOR_ID"

    # Read the file into memory
    with io.open("path/to/local/pdf", "rb") as image:
        image_content = image.read()

    # Load Binary Data into Document AI RawDocument Object
    raw_document = documentai.RawDocument(content=image_content, mime_type="application/pdf")

    # Configure the process request
    request = documentai.ProcessRequest(name=name, raw_document=raw_document)

    result = client.process_document(request=request)

    # Read the text recognition output from the processor
    text = result.document.text

    # Read the text and form fields output from the processor
    fields = result.document.fields

    # Get all of the document text as one big string
    print("Full Document Text: {}".format(text))

    # For a full list of Document object attributes,
    # please reference this page:
    # https://www.example.com    # Read the text recognition output from the processor
    print("The document contains the following paragraphs:")
    for paragraph in result.document.text.paragraphs:
        print("Paragraph Confidence: {}".format(paragraph.layout.confidence))
        print("Paragraph Text: {}".format(paragraph.layout.text))
        print("Paragraph Layout:")
        print(paragraph.layout.text_anchor)

    # Read the text recognition output from the processor
    print("The document contains the following pages:")
    for page in result.document.pages:
        print("Page Confidence: {}".format(page.layout.confidence))
        print("Page Dimensions:")
        print(page.dimension)
        print("Page Layout:")
        print(page.layout.text_anchor)

    # Read the text recognition output from the processor
    print("The document contains the following tables:")
    for table in result.document.tables:
        print("Table Confidence: {}".format(table.layout.confidence))
        print("Table Rows:")
        for row in table.body_rows:
            print("\tRow Text: {}".format(row.layout.text))
            print("\tRow Layout:")
            print(row.layout.text_anchor)
        print("Table Columns:")
        for col in table.header_rows[0].cells:
            print("\tColumn Text: {}".format(col.layout.text))
            print("\tColumn Layout:")
            print(col.layout.text_anchor)

    # Read the form fields output from the processor
    print("The document contains the following fields:")
    for field in fields:
        print("Field Name: {}".format(field.name))
        print("Field Value: {}".format(field.value.text))
        print("Field Confidence: {}".format(field.confidence))
        print("Field Value Type:")
        print(field.value.type_)
        print("Field Value Text Anchor:")
        print(field.value.text_anchor)

    # Read the entity recognition output from the processor
    print("The document contains the following entities:")
    for entity in result.document.entities:
        print("Entity Text: {}".format(entity.text))
        print("Entity Confidence: {}".format(entity.confidence))
        print("Entity Type: {}".format(entity.type_))
        print("Entity Mentions:")
        for mention in entity.mentions:
            print("\tMention Text: {}".format(mention.text))
            print("\tMention Confidence: {}".format(mention.confidence))
            print("\tMention Type: {}".format(mention.type_))

    # Read the entity relations output from the processor
    print("The document contains the following relationships:")
    for relation in result.document.relations:
        print("Relation Subject: {}".format(relation.subject))
        print("Relation Object: {}".format(relation.object))
        print("Relation Confidence: {}".format(relation.confidence))
        print("Relation Type: {}".format(relation.type_))

    # Get all of the document text as one big string
    print("Full Document Text: {}".format(text))

    return result

