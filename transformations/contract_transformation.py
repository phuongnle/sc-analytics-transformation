import hashlib

def transform(entity, msg_context):
    key = (entity['id'] + '|' + msg_context['source']).encode('utf-8')
    entity['hashCode'] = hashlib.md5(key).hexdigest()
    return entity