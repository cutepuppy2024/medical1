-- < 오라클의 db를 파이썬과 연결 >

select * from stu_score;

select * from stu_score
where name like '_a%'
order by no asc;

select a.*,name from board a, member b
where a.id = b.id;

select bno,id,name, btitle,bcontent,dbdate,bgroup,bstep,bindent,bhit,bfile from board a, member b
where a.id = b.id;

select no,name, total, avg, avg,
case
when avg>=90 then 'A'
when avg>=80 then 'B'
when avg>=70 then 'C'
when avg>=60 then 'D'
else 'F'
end as grade
from stu_score;

select round(avg(salary),2) as salary from employees;

-- employees 테이블에서 사번, 이름, 월급, 실제월급(월급+(월급*커미션)), 월급*1410 원화로 환산해서 천단위표시
select * from employees;
select employee_id,emp_name,salary,salary+(salary*nvl(commission_pct,0)) real_sal, to_char(salary*1410,'L'||'999,999,999') kor_salary from employees;

-- 부서별 평균월급, 최대월급, 최소월급을 출력
select department_id,count(department_id), round(avg(salary),2), max(salary), min(salary) from employees
where department_id is not null
group by department_id
order by department_id;


select * from stu_score
order by no;

-- '홍' 을 검색하면 '홍'에 관련된 모든 사람을 검색하기
select * from stu_score
where name like '%홍%'
order by no;

select name, total, avg from stu_score
where total >= (select avg(total) from stu_score);

select name, total, avg from stu_score
where total >= (select avg(total) from stu_score);

select avg(total) from stu_score;

select name, avg from stu_score
where avg>=60
order by no;

-- 사원번호, 사원명, 부서번호, 부서명을 출력하시오
select employee_id, emp_name, employees.department_id, department_name 
from employees, departments
where employees.department_id = departments.department_id;

--> 별칭으로 간략하게
select employee_id, emp_name, employees.department_id, department_name 
from employees a, departments b
where a.department_id = b.department_id;

-- 두번째 자리에 a가 들어가는 사원을 검색하시오
select emp_name from employees
where emp_name like '_a%';

select employee_id, emp_name, employees.department_id, department_name 
from employees a, departments b
where a.department_id = b.department_id and emp_name like '_a%';

-- 월급이 평균 이상인 사원을 검색하시오
select emp_name, salary from employees
where salary >= (select avg(salary) from employees);

-- and로 조건을 추가
select employee_id, emp_name, employees.department_id, department_name 
from employees a, departments b
where a.department_id = b.department_id and emp_name like '_a%'
and salary >= (select avg(salary) from employees);

select * from employees;

select * from departments;

select * from jobs;

-- 사원번호, 사원명, 부서번호, 부서명, 직급번호, 직급명
select employee_id, emp_name, a.department_id, department_name, a.job_id, job_title from employees a, departments b, jobs c
where a.department_id = b.department_id and a.job_id = c.job_id;

-- 사원번호, 사원명, 월급, 최소월급분, 직급, 직급타이틀
select employee_id, emp_name, salary, min_salary, a.job_id, job_title from employees a, jobs b
where a.job_id = b.job_id;

-- 사원번호, 사원명, 월급, 최소월급분, 인상분(최소월급 몇% 이상을 받고 있는지 : (현재월급-최소월급)/현재월급 *100), 직급, 직급타이틀
select employee_id, emp_name, salary, min_salary, to_char(round(((salary-min_salary)/salary)*100,2))||'%', a.job_id, job_title from employees a, jobs b
where a.job_id = b.job_id;

select job_id,job_title from jobs;

-- job_title Manager 글자가 들어가 있는 사원번호, 사원명, 직급번호, 직급명, 월급, 최대월급을 출력
select employee_id, emp_name, a.job_id, job_title, salary, max_salary from employees a, jobs b
where a.job_id = b.job_id  and job_title like '%Manager%';

-- < 테이블 명 >
select * from employees;
select * from departments;
select * from jobs;

-- google 상품erd
select a.user_id, user_name, user_phone, user_address1, user_address2, user_address3 from User a, Deliver_address b
where a.user_id = b.user_id;


create table stu_grade (
grade varchar2(1) primary key,
low_score number(3) not null,
high_score number(3) not null
);

insert into stu_grade values(
'A',90,100
);
insert into stu_grade values(
'B',80,89
);
insert into stu_grade values(
'C',70,79
);
insert into stu_grade values(
'D',60,69
);
insert into stu_grade values(
'F',0,59
);


commit;

select * from stu_grade ;


-- case when then grade 컬럼 90이상 A, 80점 이상 B... 출력
select no,name,avg,
case
when avg >=90 then 'A'
when avg >=80 then 'B'
when avg >=70 then 'C'
when avg >=60 then 'D'
else 'F'
end as grade
from stu_score;

-- <  non_equi join : 속도가 빠르고 구문도 단순함 -> 코드수정할 필요가 없다 >
select no,name,avg,grade
from stu_score,stu_grade
where avg between low_score and high_score
order by no;

-- 두개의 테이블에는 같은 컬럼이 없음 
select * from stu_score;
select * from stu_grade;

update stu_grade set low_score=92
where grade = 'A'
;
update stu_grade set low_score=82, high_score=91
where grade = 'B'
;
update stu_grade set low_score=72, high_score=81
where grade = 'C'
;
update stu_grade set low_score=62, high_score=71
where grade = 'D'
;
update stu_grade set high_score=62
where grade = 'F'
;

commit;



-- 부서별 월급 합계를 출력
select department_id, sum(salary) a from employees
where department_id is not null
group by department_id
order by a ;


-- < kor_loan_status 테이블 사용 >

-- 월별 매출액을 기준으로 고객등급
select * from kor_loan_status;

-- 지역별 대출합계를 출력
select region, count(region),sum(loan_jan_amt) from kor_loan_status
group by region
order by region;

-- 2가지로 그룹화 가능
select region,gubun, count(region),sum(loan_jan_amt) from kor_loan_status
group by region,gubun
order by region;

-- 연도별,지역별,대출합계금액
select substr(period,0,4), region, sum(loan_jan_amt) from kor_loan_status
group by substr(period,0,4),region 
order by region ;

-- < lotte_product 테이블 임포트 >
select * from lotte_product;

-- 시간대별, 연령대별 판매량 총합, 가장 판매량 많은 순으로 정렬 출력하시오 -> 시간대, 연령대별 마케팅 자료로 활용가능
select time_cd,age_cd,sum(purh_amt) a from lotte_product
group by time_cd,age_cd
order by a desc;

-- 연도별 판매량 총합
select substr(std_ym,1,4),sum(purh_amt) from lotte_product
group by substr(std_ym,1,4);

-- 월별 판매량 총합
select substr(std_ym,5),sum(purh_amt) from lotte_product
group by substr(std_ym,5)
order by substr(std_ym,5);



-- < shop_product(모카루) 테이블 임포트 >
select * from shop_product;

-- 2024/03/01 이후, 이름별, 금액 합계
select * from shop_product
where pdate>='2024/03/01';

select name, to_char(sum(amount),'L999,999,999') as sum_amt from shop_product
where pdate>='2024/03/01'
group by name
order by name;

-- customer_rank테이블 생성
-- rank => 100만원 미만 : BRONZE, 200만원 미만: SILVER, 300만원 미만 : GOLD, 300만원 이상 : PLATINUM
-- name,2024년3월 이후 합계 sum(amount), rank
-- non-equi join으로 처리

create table customer_rank (
rank varchar2(10),
lower_amt number(30),
higher_amt number(30)
);

insert into customer_rank values(
'BRONZE',0,999999
);

insert into customer_rank values(
'SILVER',1000000,1999999
);

insert into customer_rank values(
'GOLD',2000000,2999999
);
insert into customer_rank values(
'PLATINUM',3000000,9999999
);

select * from customer_rank;

-- non-equi join
select no,name,avg,grade 
from stu_score,stu_grade
where avg between low_score and high_score
;

-- 가상함수가 됨, 순차적 처리 중 -> rank가 안만들어짐 : error
select name,sum(amount),rank
from shop_product,customer_rank
where pdate>='2024/03/01' and sum(amount) between lower_amt and higer_amt
group by name, rank
;

-- 괄호 안의 코드를 먼저 처리함 -> between 가능해짐
select name,s_mount,rank
from (select name, sum(amount) s_mount from shop_product where pdate>='2024/03/01' group by name), customer_rank
where s_mount between lower_amt and higher_amt
;



-- < rownum, row_number() : 순번을 새롭게 부여해서 출력해주는 함수 >
select * from lotte_product
order by std_ym;

-- rownum : 테이블 생성 후 마지막 순서로 붙여짐
select rownum,std_ym,sex_cd,age_cd, time_cd, purh_amt
from lotte_product;


-- ## rownum에 따른  *와 a.* 사용 차이
-- 전체선택자 * 인 경우 번호대로 출력 가능
select * from stu_score 
where no>=1 and no <=10
order by no;

select * from stu_score 
where no>=11 and no <=20
order by no;

select * from stu_score 
where no>=21 and no <=30
order by no;


-- rownum의 경우 아래와 같이 *의 범위를 지정해 주어야 한다
select rownum,a.* from lotte_product a;
select * from lotte_product ;

-- 개수를 지정하는 이유 : 한꺼번에 많은 데이터를 가지고 오면 서버부하, 속도 느려짐
select rownum,a.* from lotte_product a
where rownum <= 10;



select rownum,a.* from lotte_product a
where rownum >=1 and rownum <= 10;

-- error : 테이블 생성후 rownum이 붙는데 번호가 11번이므로 인식이 안됨
select rownum,a.* from lotte_product a
where rownum >=11 and rownum <= 20;
--> 미리 형태를 만들어 주어야 다음 번호가 붙여질 수 있음
select rownum rnum, b.* 
from (select rownum rnum,a.* from lotte_product a) b
where rnum >=11 and rnum <= 20;

select rnum, std_ym, sex_cd, age_cd, time_cd,purh_amt
from (select rownum rnum,a.* from lotte_product a) b
where rnum >=21 and rnum <= 30;

-- rownum이 순번대로 붙여져있지 않다 -> order by 때문에 number 순서가 뒤바뀐것
select rownum,a.* 
from lotte_product a
order by std_ym;

-- 괄호 안의 코드를 먼저 실행 후 번호를 붙임 -> order by가 먼저 실행되었기 때문에 number 순서가 바뀌지 않음
select rownum,b.*
from (select * from lotte_product order by std_ym) b;


select * from stu_score
order by no;

-- kor 점수가 높은순으로 21~30등까지 출력하되, 순번을 부여하시오
select name, kor from stu_score;

select rownum,a.* 
from (select * from stu_score order by kor desc) a
;

-- 1) order by kor 원래 테이블 a 2) rownum, 별칭 rnum 붙인 전체 테이블 b 3) rnum 사용한 컬럼 select와 where절
select rnum,no, name, kor, eng, math, total, avg,rank,c_date 
from ( select rownum rnum, b.* from (select a.* from stu_score a order by kor desc) b  )
where rnum >=21 and rnum <=30;









