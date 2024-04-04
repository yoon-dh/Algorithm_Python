select B.name, B.DATETIME
from (
    select rownum as num, A.*
    from (
        select I.NAME, I.DATETIME
        from 
            ANIMAL_INS I left join ANIMAL_OUTS O on I.ANIMAL_ID = O.ANIMAL_ID
            where O.DATETIME is null
            order by I.DATETIME
    ) A
) B
where num <= 3;