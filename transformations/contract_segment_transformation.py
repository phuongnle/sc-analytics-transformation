import hashlib
import binascii

def get_hash(key):
    return hashlib.md5(key.encode('utf-8'))

def hash_object_to_bytes_array(hashkey):
    return list(hashkey.digest())

def transform(entity, msg_context, sql_helper):
    contract_segment_key = str(entity['id']) + '|' + str(msg_context['source'])
    contract_segment_hashkey = get_hash(contract_segment_key)
    entity['contractSegmentHashkey'] = hash_object_to_bytes_array(contract_segment_hashkey)

    version_key = str(contract_segment_key) + '|' + str(entity['version'])
    version_hash = get_hash(version_key)
    entity['rowHash'] = hash_object_to_bytes_array(version_hash)

    return entity