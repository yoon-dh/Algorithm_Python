-- 코드를 입력하세요
select I.ANIMAL_ID, I.NAME
from ANIMAL_INS I left join ANIMAL_OUTS O on I.ANIMAL_ID = O.ANIMAL_ID
where I.DATETIME > O.DATETIME
order by I.DATETIME;