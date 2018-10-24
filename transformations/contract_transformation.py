import hashlib

def transform(entity, msg_context):
    key = (str(entity['id']) + '|' + str(msg_context['source'])).encode('utf-8')
    entity['hashKey'] = hashlib.md5(key).hexdigest()
    return entity