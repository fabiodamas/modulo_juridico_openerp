# -*- encoding: utf-8 -*-
##############################################################################

from osv import osv, fields

class juridico_processo(osv.osv):
    _name = 'juridico.processo'
    _inherit = 'product.product'
    _table = 'product_product'
    _columns = {
        'posicao_cliente'        : fields.selection([('adverso','Adverso'),('advogado','Advogado'),('advogado_adverso','Advogado Adverso'),('cliente','Cliente'),('reclamada','Reclamada'),('reclamante','Reclamante'),('relator','Relator'),('requerente','Requerente'),('requerido','Requerido'),('reu','Réu'),('testemunha','Testemunha')], 'Posição do Cliente'),
        'cliente_adverso_id'     : fields.many2one('res.partner', 'Cliente Adverso'),
        'posicao_cliente_adverso': fields.selection([('adverso','Adverso'),('advogado','Advogado'),('advogado_adverso','Advogado Adverso'),('cliente','Cliente'),('reclamada','Reclamada'),('reclamante','Reclamante'),('relator','Relator'),('requerente','Requerente'),('requerido','Requerido'),('reu','Réu'),('testemunha','Testemunha')], 'Posição do Cliente Adverso'),
		'privado'                : fields.boolean('Privado'),
		'data_processo'          : fields.datetime('Data do Processo'),		
        'classeprocessual'       : fields.many2one('juridico.classe_processual', 'Classe Processual'),
        'naturezaacao'           : fields.many2one('juridico.natureza_acao', 'Natureza da Ação'),
        'rito'                   : fields.many2one('juridico.rito', 'Rito'),
        'forum_escolha'          : fields.many2one('juridico.forum', 'Fórum'),
        'cliente_adverso_id'     : fields.many2one('res.partner', 'Cliente Adverso'     ),
		'advogado_responsavel'   : fields.many2one('res.users'  , 'Advogado Responsável'),
        'estado_processo'        : fields.selection ([('andamento','Andamento'), ('concluido','Concluído'),('finalizado','Finalizado')] , 'Estado do Processo'),
        'cliente_id'             : fields.many2one('res.partner', 'Cliente')
    }
	# _defaults = {
    #    'privado': lambda *a: False
	# }
juridico_processo()

class juridico_forum(osv.osv):
    _name = 'juridico.forum'
    _columns = {
        'name': fields.char('Nome do Fórum', size=50),
        'cidade': fields.char('Cidade', size=50),
        'pais': fields.many2one('res.country', 'País')
    }
juridico_forum()

class juridico_classe_processual(osv.osv):
    _name = 'juridico.classe_processual'
    _columns = {
        'name': fields.char('Classe Processual', size=50),
        'adicionais': fields.char('Dados adicionais', size=50),
    }
juridico_classe_processual()

class juridico_natureza_acao(osv.osv):
    _name = 'juridico.natureza_acao'
    _columns = {
        'name': fields.char('Natureza da Ação', size=50),
        'adicionais': fields.char('Dados adicionais', size=50),
    }
juridico_natureza_acao()

class juridico_rito(osv.osv):
    _name = 'juridico.rito'
    _columns = {
        'name': fields.char('Rito', size=50),
        'adicionais': fields.char('Dados adicionais', size=50),
    }
juridico_rito()




# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

