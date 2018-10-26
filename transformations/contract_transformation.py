import hashlib
import binascii

def get_hash(key):
    return hashlib.md5(key.encode('utf-8'))

def hash_object_to_bytes_array(hashkey):
    return list(hashkey.digest())

def get_organisation_hashKey(organisation_id, sql_helper):
    if organisation_id is None:
        return None
    query = "select top 1 [Organisation HashKey] from [Data Vault].[Hub Organisation] where [Organisation ID] = ?"
    return sql_helper.fetch_value(query, organisation_id)

def transform(entity, msg_context, sql_helper):
    contract_key = str(entity['id']) + '|' + str(msg_context['source'])
    contract_hashkey = get_hash(contract_key)
    entity['contractHashkey'] = hash_object_to_bytes_array(contract_hashkey)

    version_key = str(contract_hashkey) + '|' + str(entity['version'])
    version_hash = get_hash(version_key)
    entity['rowHash'] = hash_object_to_bytes_array(version_hash)

    organisation_hashKey = get_organisation_hashKey(entity['organisation id'], sql_helper)
    if organisation_hashKey is not None:
        entity['supplierHashKey'] = list(organisation_hashKey)
        link_supplier_contract_key = str(contract_hashkey.hexdigest()) + '|' + binascii.hexlify(organisation_hashKey).decode('utf-8') + '|' + str(msg_context['source'])
    else:
        link_supplier_contract_key = str(contract_hashkey.hexdigest()) + '|' + '|' + str(msg_context['source'])

    link_supplier_contract_hashkey = get_hash(link_supplier_contract_key)
    entity['linkSupplierContractHashkey'] = hash_object_to_bytes_array(link_supplier_contract_hashkey)


    link_client_contract_key = str(contract_hashkey.hexdigest()) + '|' + '|' + str(msg_context['source'])
    link_client_contract_hashkey = get_hash(link_client_contract_key)
    entity['linkClientContractHashkey'] = hash_object_to_bytes_array(link_client_contract_hashkey)


    return entity