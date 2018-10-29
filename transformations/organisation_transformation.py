import hashlib

def get_hash(key):
    return hashlib.md5(key.encode('utf-8'))

def hash_object_to_bytes_array(hashkey):
    return list(hashkey.digest())

def get_property_string(entity, property):
    return str(entity[property]) if property in entity else ''

def transform(entity, msg_context):
    organisation_key = get_property_string(entity, 'id') + '|' + str(msg_context['source'])
    organisation_hashkey = get_hash(organisation_key)
    entity['organisationHashkey'] = hash_object_to_bytes_array(organisation_hashkey)

    version_key = str(organisation_hashkey) + '|' + get_property_string(entity, 'version')
    version_hash = get_hash(version_key)
    entity['versionRowHash'] = hash_object_to_bytes_array(version_hash)

    organisation_row_key = \
        str(organisation_hashkey) + '|' + str(msg_context['source']) + '|' + \
        get_property_string(entity, 'id') + '|' + get_property_string(entity, 'item url') + '|' + get_property_string(entity, 'registered name') + '|' + \
        get_property_string(entity, 'retired') + '|' + get_property_string(entity, 'deleted') + '|' + get_property_string(entity, 'previous registered name') + '|' + \
        get_property_string(entity, 'trading name') + '|' + get_property_string(entity, 'previous trading name') + '|' + get_property_string(entity, 'organisation number') + '|' + \
        get_property_string(entity, 'business number') + '|' + get_property_string(entity, 'business number registration date') + '|' + get_property_string(entity, 'company number') + '|' + \
        get_property_string(entity, 'date of incorporation') + '|' + get_property_string(entity, 'registered for gst') + '|' + get_property_string(entity, 'indigenous owned entity') + '|' + \
        get_property_string(entity, 'disability employment organisation') + '|' + get_property_string(entity, 'erp id') + '|' + get_property_string(entity, 'organisation website') + '|' + \
        get_property_string(entity, 'organisation email') + '|' + get_property_string(entity, 'organisation fax') + '|' + get_property_string(entity, 'business address line 1') + '|' + \
        get_property_string(entity, 'business address line 2') + '|' + get_property_string(entity, 'business address line 3') + '|' + get_property_string(entity, 'business suburb') + '|' + \
        get_property_string(entity, 'business postcode') + '|' + get_property_string(entity, 'postal address line 1') + '|' + get_property_string(entity, 'postal address line 2') + '|' + \
        get_property_string(entity, 'postal address line 3') + '|' + get_property_string(entity, 'postal suburb') + '|' + get_property_string(entity, 'postal postcode') + '|' + \
        get_property_string(entity, 'notes') + '|' + get_property_string(entity, 'phone number') + '|' + get_property_string(entity, 'organisation type')
    entity['organisationRowHash'] = hash_object_to_bytes_array(get_hash(organisation_row_key))

    organisation_address_row_key = \
        str(organisation_hashkey) + '|' + str(msg_context['source']) + '|' + \
        get_property_string(entity, 'business address line 1') + '|' + get_property_string(entity, 'business address line 2') + '|' + get_property_string(entity, 'business address line 3') + '|' + \
        get_property_string(entity, 'business suburb') + '|' +  get_property_string(entity, 'business postcode') + '|' + get_property_string(entity, 'business city') + '|' + \
        get_property_string(entity, 'business state/region') + '|' +  get_property_string(entity, 'business country') + '|' + \
        get_property_string(entity, 'postal address line 1') + '|' + get_property_string(entity, 'postal address line 2') + '|' + \
        get_property_string(entity, 'postal address line 3') + '|' + get_property_string(entity, 'postal suburb') + '|' + get_property_string(entity, 'postal postcode') + '|' + \
        get_property_string(entity, 'postal city') + '|' + get_property_string(entity, 'postal state/region') + '|' + get_property_string(entity, 'postal country')
    entity['organisationAddressRowHash'] = hash_object_to_bytes_array(get_hash(organisation_address_row_key))

    return entity