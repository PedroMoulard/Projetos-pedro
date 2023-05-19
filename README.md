# query para metabase
with deliveries as (
select d.*,
    case 
        WHEN TIMESTAMP_DIFF(dp.real_delivered_at,dp.estimated_delivery_at, MINUTE) <= 0 THEN 'SIM'
        WHEN TIMESTAMP_DIFF(dp.real_delivered_at,dp.estimated_delivery_at, MINUTE) > 0 THEN 'NÃO'
        else 'NÃO'
    END AS Entregue_em_tempo,
    dp.order_item_id
from `mecanicity.public_deliveries` d
left join `operations_mdl.deliveries` dp on d.id = dp.delivery_id
    where d.status = 'delivered'
    and dp.order_created_at >= '2023-01-01'
    and d.estimated_delivery_time = 'express_delivery'
),

deliveries_ok as (
select *
from deliveries
where Entregue_em_tempo ='SIM'
)

SELECT 
    d.logistics_driver_name,
    count(do.order_item_id) pedidos_ok,
    count(d.order_item_id) total_pedidos,
    count(do.order_item_id)/count(d.order_item_id) as percent_entregue
from
    deliveries d
left join deliveries_ok do on do.order_item_id = d.order_item_id
where d.logistics_driver_name is not null
[[AND {{d.logistics_driver_name}}]]
group by 1
order by 3 desc
limit 10
