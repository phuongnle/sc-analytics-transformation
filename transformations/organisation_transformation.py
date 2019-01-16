import hashlib

def transform(entity, msg_context):
    entity['Organisation Number'] = str(entity['Organisation Number']) + " edited"
    return entity
