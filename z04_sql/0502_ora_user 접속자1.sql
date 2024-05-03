select * from employees;
select name from stu_score;
-- 이름검색
select * from stu_score where id like '%a%'
order by no
;
-- row_number() over()
-- 11~20까지 출력하시오.
select rownum,a.* from stu_score a
order by no
;
select count(*) from ( select row_number() over(order by no) rnum,a.* from stu_score a
where id like '%a%' )
;
select count(*) from ( select row_number() over(order by no) rnum,a.*
from stu_score a where id like '%a%' )
;
select * from ( select row_number() over(order by no) rnum,a.* from stu_score a
where id like '%a%' ) where rnum>=11 and rnum<=20
;
select count(*) from stu_score where id like '%a%';

create table melon (
mno number primary key,
rank number,
v_rank number,
img varchar2(150),
title varchar2(100),
singer varchar2(100),
likeNum number
);

select * from melon;