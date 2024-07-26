drop table students;

select * from employees;

select * from stu_score;

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

select * from stu_score 
where id like '%a%';

select * from 
( select row_number() over(order by no) rnum,a.* from stu_score a
where id like '%a%' ) 
;

select * from 
( select row_number() over(order by no) rnum,a.* from stu_score a
where id like '%a%' ) 
where rnum>=11 and rnum<=20
;

select count(*) from stu_score where id like '%a%';

select count(*) from 
( select row_number() over(order by no) rnum,a.* from stu_score a
where id like '%a%' )
;


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






-- 테이블명 : melon
-- 순번(시퀀스), 순위, 변동 v_rank ,이미지 img, 곡제목 title, 뮤지션명 singer, 좋아요수 likeNum

create table melon (
mno number primary key,
rank number,
v_rank number,
img varchar2(150),
title varchar2(100),
singer varchar2(100),
likeNum number
);

drop table melon;

-- alter table melon modify (img varchar2(150));

desc melon;

select * from melon
order by rank;

select melon_seq.nextval from dual;


create table yanolja (
yno number primary key,
img varchar2(100),
title varchar2(100),
grade number,
grade_num number,
price number
);

alter table yanolja modify img varchar2(500);
