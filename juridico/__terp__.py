# -*- encoding: utf-8 -*-
##############################################################################
{
    "name" : "Gestão Jurídica",
    "author" : "Fabio Damas",
    "version" : "1.0",
    "depends" : ["base","product"],
    "init_xml" : [],
    "update_xml" : [
        #"security/ir.model.access.csv",
        "custom_view.xml"
    ],
    'demo_xml': ['juridico_demo.xml'],
    "category" : "Módulos jurídicos específicos / Gestão Jurídica",
    "active": False,
    "installable": True
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

