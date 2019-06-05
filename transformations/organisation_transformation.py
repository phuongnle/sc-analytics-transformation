import hashlib

def transform(entity, msg_context):
    entity['Previous Registered Name'] = str(entity['Previous Registered Name']) + " edited"
    return entity
