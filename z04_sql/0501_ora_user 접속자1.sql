drop table students;

update students set id ='aaa',name='홍길동',gender='M' where id='Joelynn';
update students set id='bbb',name='유관순', gender ='F' where id='Bambie';
update students set id='ccc',name='이순신', gender ='M' where id='Orin';
update students set id='ddd',name='강감찬', gender ='M' where id='Puff';
update students set id='eee',name='김구', gender ='M' where id='Godfree';
update students set id='fff',name='김유신', gender ='M' where id='Penny' and pw='8503';
update students set id='ggg',name='홍길자', gender ='F' where id='Matti' and pw='3737';
update students set id='hhh',name='홍길순', gender ='F' where id='Catherin';

select * from students;
commit;

select * from stu_score 
order by no;

-- < rownum : 새롭게 순차적 번호 생성 >
select rownum,a.* from students a;

-- 1. select
select a.* from students a;
-- 2. rownum 함수 실행
select rownum,a.* from students a;
-- 3. order by
select rownum,a.* from students a
order by grade;

-- 1. select  2. order by  3. rownum 함수 실행
select * from students
order by grade;

select rownum, a.* from
(select * from students
order by grade
) a
;


-- 평균 85점 이상이면서 no>=500 출력
select no,name, avg from stu_score
where avg>=85 and no>=500
;

select * from 
(select * from stu_score where avg>=85)
where no>=500
;

select name,s_mount,rank
from (select name, sum(amount) s_mount from shop_product where pdate>='2024/03/01' group by name), customer_rank
where s_mount between lower_amt and higher_amt
;
-- 테이블명 shop_product
select name, amount,pdate from shop_product
where pdate>='2024-03-01';

-- '2024-03-01' 이후, 이름별, 구매내역 합계를 구하시오
-- sum(amount) 가상으로 만들어진 컬럼
select name,sum(amount) from shop_product
where pdate>='2024/03/01'
group by name;

select * from customer_rank;


-- 같은 컬럼이 없으면서 2개 테이블을 사용해 검색하는 방법
select name, avg from stu_score;

-- shop_product, customer_rank -> non-equi join
select name, avg, grade from stu_score,stu_grade
where avg between low_score and high_score;


--<  non-uqui join에서 데이터를 추출한 코드 작성 과정 >

-- 1) 단순히 2테이블을 합치는 식을 작성 -> sum(amount)로 between을 하려면 되지 않는다
select name,sum(amount),rank from shop_product, customer_rank
where pdate>='2024/03/01' and sum(amount) between lower_amount and higher_amount
group by name, rank;

-- 2) 추출한 데이터식 : sum(amount)
select name, sum(amount) as s_amount from shop_product
where pdate>='2004/03/01'
group by name;

-- 3) shop_product 자리에 해당 테이블에서 추출한 데이터식을 넣는다
select name,sum(amount),rank from (select name, sum(amount) as s_amount from shop_product where pdate>='2004/03/01' group by name), customer_rank
where sum(amount) between lower_amount and higher_amount;

select * from customer_rank;


-- <  rownum에서 해당 번호의 데이터를 출력하는 방법  >
-- 1) 전체에서 rownum을 붙임
select rownum, a.* from students a
order by id;

-- 2-1) 해당번호의 데이터를 출력
select rownum,b.* from
(select * from students order by id) b
where rownum>=1 and rownum<=10
;
-- 2-2) 해당번호의 데이터를 출력
select * from 
(select rownum rnum,b.* from
(select * from students order by id) b)
where rnum>=11 and rnum<=20
;

-- error의 이유 : rownum을 붙인상태에서 멈춘상태임
select rownum,a.* from
(select * from students order by id) a
where rownum>=11 and rnum<=20;

select rnum,b.* from
(select rownum rnum,a.* from
(select * from students order by id) a
)b
)
where rnum>=11 and rnum<=20;

select * from 
(select rownum rnum,a.* from
(select * from students order by id) a)
where rnum>=11 and rnum<=20
;

-- rownum을 다시한번 붙은 형태 -> 차이
select rownum rnum,a.* from 
(select rownum rnum,b.* from
(select * from students order by id) b)
a
where rnum>=11 and rnum<=20
;

select * from (
select row_number() over(order by id) rnum,a.* 
from students a)
where rnum>=11 and rnum<=20;



-- <  self join  >
select * from employees;
select * from departments;

select employee_id, emp_name, department_id, manager_id from employees
order by department_id;

select employee_id, emp_name, a.department_id, department_name, a.manager_id from employees a, departments b
where a.department_id = b.department_id
order by a.department_id;

-- 전체에 해당되는 컬럼과 조건에 부합되는 컬럼 2가지
-- cross join 107 * 107 -> 무의미
-- equi join : 같은 컬럼을 가지고 검색
select a.employee_id, a.emp_name, a.department_id, department_name a.manager_id, b.emp_name 
from employees a, employees b, departments c
where a.manager_id = b.employee_id and a.department_id = c.department_id
order by a.employee_id; -- from 키워드가 필요한 위치에 없다고? 이게 말이 되나?

select a.employee_id,a.emp_name,a.department_id,department_name,a.manager_id,b.emp_name
from employees a,employees b,departments c
where a.manager_id = b.employee_id and a.department_id = c.department_id
order by a.employee_id;

-- 철자 하나 안틀린 코드인데 내가 쓴것이 오류가 나는 이유는

select a.employee_id, a.emp_name, a.manager_id, b.emp_name
from employees a, employees b
where a.manager_id = b.employee_id;

-- john chen 과 동일한 부서에 근무하는 사람을 출력하시오
-- 사원명, 부서번호, 부서명, 같이 근무하는 사원명
-- 1. Guy Himuro 부서를 출력
-- 2. 부서번호를 가지고 같은 사람을 출력
select * from employees;

select emp_name, department_id from employees
where emp_name = 'Guy Himuro';

select emp_name, department_id from employees
where department_id = 30;

select e1.emp_name,e1.department_id, e2.emp_name 
from employees e1, employees e2
where e1.department_id = e2.department_id and e1.emp_name='Guy Himuro'
;



-- < 파이썬과 연결 >
insert into member values (
member_seq.nextval, 'fff',1111,'김유신','남자',sysdate
);

insert into member values (
member_seq.nextval, 'ggg',1111,'홍길순','여자',sysdate
);

select * from member;
commit;
rollback;

update member set name='홍길동' where id='aaa';


-- <  0501_03  > 

select emp_name from employees;

select a.* from employees a, employees b
where a.department_id=b.department_id and a.emp_name = 'Pat Fay';

select a.emp_name, b.emp_name from employees a, employees b
where a.department_id=b.department_id and a.emp_name = 'Pat Fay';

select a.emp_name,a.department_id,c.department_name, b.emp_name from employees a, employees b, departments c
where a.department_id=b.department_id and a.emp_name = 'Pat Fay' and a.department_id = c.department_id;

select a.emp_name, a.department_id, b.emp_name from employees a, employees b
where a.department_id = b.department_id;


-- <  0501_04  >
select * from member 
order by id;

commit;

-- < 0501_05  >
create table mem (
id varchar2(30),
pw varchar2(30),
name varchar2(30),
mdate date
);

drop table mem;

select * from mem;

create table yeogi (
yno number(4) primary key,
title varchar2(100) not null,
region varchar2(30),
score number,
member number,
img varchar2(100),
price number

);

select * from yeogi;

alter table yeogi modify (img varchar2(150));

desc yeogi;
