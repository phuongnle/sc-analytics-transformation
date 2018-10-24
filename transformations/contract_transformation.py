import hashlib

def get_hashkey(key):
    return hashlib.md5(key.encode('utf-8'))

def hashkey_to_bytes_array(hashkey):
    return list(hashkey.digest())

def transform(entity, msg_context):
    contract_key = str(entity['id']) + '|' + str(msg_context['source'])
    contract_hashkey = get_hashkey(contract_key)
    entity['contractHashkey'] = hashkey_to_bytes_array(contract_hashkey)

    link_client_contract_key = str(contract_hashkey.hexdigest()) + '|' + '|' + str(msg_context['source'])
    link_client_contract_hashkey = get_hashkey(link_client_contract_key)
    entity['linkClientContractHashkey'] = hashkey_to_bytes_array(link_client_contract_hashkey)
    return entity