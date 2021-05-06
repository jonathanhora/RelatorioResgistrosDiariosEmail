def select():
    script ="""select top 100 UPPER(i.descricao), max(format(p.data_proposta, 'yyyy/MM/dd HH:mm:ss')) from tb_instituicao i (nolock)
    left join tb_proposta p (nolock) on p.id_tb_instituicao = i.id_tb_instituicao
    where i.ativo = 1
    and i.id_tb_instituicao not in (1,21,30,64,75,103,104,113,120,123,132,140,141,142)
    group by i.descricao
    order by 1 asc"""
    return  script