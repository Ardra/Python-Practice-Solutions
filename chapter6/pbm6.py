def json_encode(data):
	if isinstance(data, bool):
        	if data:
            		return 'true'
        	else:
            		return 'false'
   	 elif isinstance(data, (float, int)):
        	return str(data)
   	 elif isinstance(data, str):
        	return '"' + escape_string(data) + '"'
    	 elif isinstance(data, list):
        	return '[' + ', '.join(json_encode(d) for d in data) + ']'
    	elif isinstance(data, dict):
        	return '{' + ', '.join(k + ':' + json_encode(v) for k, v in data.iteritems()) + '}'
    	else:
        	raise TypeError('%s is not JSON serializable' % repr(data))