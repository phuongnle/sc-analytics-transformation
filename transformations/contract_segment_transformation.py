import hashlib
import binascii

def get_hash(key):
    return hashlib.md5(key.encode('utf-8'))

def hash_object_to_bytes_array(hashkey):
    return list(hashkey.digest())

def get_property_string(entity, property):
    return str(entity[property]) if property in entity else ''

def transform(entity, msg_context, sql_helper):
    contract_segment_key = get_property_string(entity, 'id') + '|' + str(msg_context['source'])
    contract_segment_hashkey = get_hash(contract_segment_key)
    entity['contractSegmentHashkey'] = hash_object_to_bytes_array(contract_segment_hashkey)

    version_key = str(contract_segment_key) + '|' + get_property_string(entity, 'version')
    version_hash = get_hash(version_key)
    entity['rowHash'] = hash_object_to_bytes_array(version_hash)

    return entity