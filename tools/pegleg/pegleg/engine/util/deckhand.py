from deckhand.engine import layering
from deckhand import errors as dh_errors

def load_schemas_from_docs(documents):
    '''
    Fills the cache of known schemas from the document set
    '''

    errors = []
    SCHEMA_SCHEMA = "deckhand/DataSchema/v1"

    schema_set = dict()
    for document in documents:
        if document.get('schema', '') == SCHEMA_SCHEMA:
            name = document['metadata']['name']
            if name in schema_set:
                errors.append('Duplicate schema specified for: %s' % name)

            schema_set[name] = document['data']

    return schema_set, errors

def deckhand_render(documents=[], fail_on_missing_sub_src=False, validate=False):

    errors = []
    rendered_documents = []

    schemas, schema_errors = load_schemas_from_docs(documents)
    errors.extend(schema_errors)

    try:
        deckhand_eng = layering.DocumentLayering(
            documents,
            substitution_sources=documents,
            fail_on_missing_sub_src=fail_on_missing_sub_src,
            validate=validate)
        rendered_documents = [dict(d) for d in deckhand_eng.render()]
    except dh_errors.DeckhandException as e:
        errors.append('An unknown Deckhand exception occurred while trying'
                      ' to render documents: %s' % str(e))

    return rendered_documents, errors