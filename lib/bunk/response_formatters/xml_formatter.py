from response_formatter import ResponseFormatter

class XmlFormatter (ResponseFormatter):

    @staticmethod
    def format (response_data):
        """
        Format response data into XML

        @param response_data           (*) All data types are accepted. If response_data is of a type not supported by
                                           the implemented response format then a ResponseFormatException is raised.

        @return (str)
        """

        supported_data_types = (type(None), str, int, long, float, list, dict, bool)

        # validate response_data type
        ResponseFormatter.validate_response_data_type(type(response_data), supported_data_types)

        return get_xml(response_data)

# ----------------------------------------------------------------------------------------------------------------------

def get_xml (obj, obj_name=None):
    """
    Format incoming Python data into a crude XML document.

    @param obj      (object)
    @param obj_name (str)

    @return (str)
    """

    if obj == None:
        return ""

    if not obj_name:
        obj_name = "xml"

    adapt = {
        dict:  get_xml_dict,
        list:  get_xml_list,
        tuple: get_xml_list
    }

    if adapt.has_key(obj.__class__):
        return adapt[obj.__class__](obj, obj_name)

    else:
        return "<%(n)s>%(o)s</%(n)s>"%{'n':obj_name,'o':str(obj)}

# ----------------------------------------------------------------------------------------------------------------------

def get_xml_dict (in_dict, obj_name=None):
    """
    Return XML for a dict object.

    @param indict   (dict)
    @param obj_name (str)

    @return (str)
    """

    xml = "<%s>"%obj_name

    for k, v in in_dict.items():
        xml += get_xml(v, k)

    xml += "</%s>" % obj_name

    return xml

# ----------------------------------------------------------------------------------------------------------------------

def get_xml_list (in_list, obj_name=None):
    """
    Return XML for a list type object such as a list or tuple.

    @param in_list  (list/tuple)
    @param obj_name (str)

    @return (str)
    """

    xml = ""

    for i in in_list:
        xml += get_xml(i, obj_name)

    return xml
