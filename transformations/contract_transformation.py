import hashlib

def get_hash(key):
    return hashlib.md5(key.encode('utf-8'))

def hash_object_to_bytes_array(hashkey):
    return list(hashkey.digest())

def transform(entity, msg_context):
    contract_key = str(entity['id']) + '|' + str(msg_context['source'])
    contract_hashkey = get_hash(contract_key)
    entity['contractHashkey'] = hash_object_to_bytes_array(contract_hashkey)

    link_client_contract_key = str(contract_hashkey.hexdigest()) + '|' + '|' + str(msg_context['source'])
    link_client_contract_hashkey = get_hash(link_client_contract_key)
    entity['linkClientContractHashkey'] = hash_object_to_bytes_array(link_client_contract_hashkey)

    link_supplier_contract_key = str(contract_hashkey.hexdigest()) + '|' + '|' + str(msg_context['source'])
    link_supplier_contract_hashkey = get_hash(link_supplier_contract_key)
    entity['linkSupplierContractHashkey'] = hash_object_to_bytes_array(link_supplier_contract_hashkey)

    version_key = str(contract_hashkey) + '|' + str(entity['version'])
    version_hash = get_hash(version_key)
    entity['rowHash'] = hash_object_to_bytes_array(version_hash)

    return entity