import hashlib

def get_hash(key):
    return hashlib.md5(key.encode('utf-8'))

def hash_object_to_bytes_array(hashkey):
    return list(hashkey.digest())

def transform(entity, msg_context):
    organisation_key = str(entity['id']) + '|' + str(msg_context['source'])
    organisation_hashkey = get_hash(organisation_key)
    entity['organisationHashkey'] = hash_object_to_bytes_array(organisation_hashkey)

    version_key = str(organisation_hashkey) + '|' + str(entity['version'])
    version_hash = get_hash(version_key)
    entity['rowHash'] = hash_object_to_bytes_array(version_hash)

    return entity