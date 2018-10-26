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
        str(msg_context['id']) + '|' + str(msg_context['item url']) + '|' + str(msg_context['registered name']) + '|' + \
        str(msg_context['retired']) + '|' + str(msg_context['deleted']) + '|' + str(msg_context['previous registered name']) + '|' + \
        str(msg_context['trading name']) + '|' + str(msg_context['previous trading name']) + '|' + str(msg_context['organisation number']) + '|' + \
        str(msg_context['business number']) + '|' + str(msg_context['business number registration date']) + '|' + str(msg_context['company number']) + '|' + \
        str(msg_context['date of incorporation']) + '|' + str(msg_context['registered for gst']) + '|' + str(msg_context['indigenous owned entity']) + '|' + \
        str(msg_context['disability employment organisation']) + '|' + str(msg_context['erp id']) + '|' + str(msg_context['organisation website']) + '|' + \
        str(msg_context['organisation email']) + '|' + str(msg_context['organisation fax']) + '|' + str(msg_context['business address line 1']) + '|' + \
        str(msg_context['business address line 2']) + '|' + str(msg_context['business address line 3']) + '|' + str(msg_context['business suburb']) + '|' + \
        str(msg_context['business postcode']) + '|' + str(msg_context['postal address line 1']) + '|' + str(msg_context['postal address line 2']) + '|' + \
        str(msg_context['postal address line 3']) + '|' + str(msg_context['postal suburb']) + '|' + str(msg_context['postal postcode']) + '|' + \
        str(msg_context['notes']) + '|' + str(msg_context['phone number']) + '|' + str(msg_context['organisation type'])
    entity['organisationRowHash'] = hash_object_to_bytes_array(get_hash(organisation_row_key))

    return entity