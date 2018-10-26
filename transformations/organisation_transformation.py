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
    entity['versionRowHash'] = hash_object_to_bytes_array(version_hash)

    organisation_row_key = \
        str(organisation_hashkey) + '|' + str(msg_context['source']) + '|' + \
        str(entity['id']) + '|' + str(entity['item url']) + '|' + str(entity['registered name']) + '|' + \
        str(entity['retired']) + '|' + str(entity['deleted']) + '|' + str(entity['previous registered name']) + '|' + \
        str(entity['trading name']) + '|' + str(entity['previous trading name']) + '|' + str(entity['organisation number']) + '|' + \
        str(entity['business number']) + '|' + str(entity['business number registration date']) + '|' + str(entity['company number']) + '|' + \
        str(entity['date of incorporation']) + '|' + str(entity['registered for gst']) + '|' + str(entity['indigenous owned entity']) + '|' + \
        str(entity['disability employment organisation']) + '|' + str(entity['erp id']) + '|' + str(entity['organisation website']) + '|' + \
        str(entity['organisation email']) + '|' + str(entity['organisation fax']) + '|' + str(entity['business address line 1']) + '|' + \
        str(entity['business address line 2']) + '|' + str(entity['business address line 3']) + '|' + str(entity['business suburb']) + '|' + \
        str(entity['business postcode']) + '|' + str(entity['postal address line 1']) + '|' + str(entity['postal address line 2']) + '|' + \
        str(entity['postal address line 3']) + '|' + str(entity['postal suburb']) + '|' + str(entity['postal postcode']) + '|' + \
        str(entity['notes']) + '|' + str(entity['phone number']) + '|' + str(entity['organisation type'])
    entity['organisationRowHash'] = hash_object_to_bytes_array(get_hash(organisation_row_key))

    return entity