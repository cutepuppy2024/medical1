-- drop table member;
-- 무결성 제약조건 : 부적합한 자료가 입력되지 않도록 하기 위한 규칙
-- not null, unique, primary key, foreign key, check


create table member(
memNo number(4) not null,
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30),
gender varchar2(6) check(gender in('남자','여자')),
mdate date default sysdate
);


-- 데이터 입력,출력,수정,삭제 부분
insert into member (memNo,id,pw,name,gender,mdate) values (
member_seq.nextval,'aaa','1111','홍길동','남자',sysdate
);
insert into member(memNo,id,pw,name,gender) values(
member_seq.nextval,'bbb','1111','유관순','여자'
);
insert into member values(
member_seq.nextval,'ccc','1111','이순신','남자',sysdate
);

select * from member;

--테이블생성 : 게시판 테이블구조
create table board (
bno number(4) primary key,
id varchar2(30), -- 외래키 등록
btitle varchar2(1000),
bcontent varchar2(4000),
dbdate date default sysdate,
bgroup number(4),
bstep number default 0,
bindent number default 0,
bhit number default 1,
bfile varchar2(100) default '',
constraint fk_board_id foreign key(id)    -- 외래키(foreign key)의 별칭: fk_id
references member(id)                     -- member테이블의 primary key id
);

alter

select * from member;

insert into board(bno,id,btitle,bcontent,dbdate,bgroup,bstep,bindent,bhit,bfile) values (
board_seq.nextval,'aaa','제목입니다.','내용입니다',sysdate,board_seq.currval,0,0,1,''
);

insert into board values (
board_seq.nextval,'bbb','제목입니다2.','내용입니다2',sysdate,board_seq.currval,0,0,1,''
);

insert into board(bno,id,btitle,bcontent,bgroup) values (
board_seq.nextval,'aaa','제목입니다.3','내용입니다3',board_seq.currval
);
-- primary key를 삭제하려면 foreign key 등록되어 있는 데이터를 우선 삭제를 모두해야 함.
-- primary key 삭제되면 모두삭제하는 방법 - on delete cascade, 모두 존재하는 방법 on update cascade

-- 삭제
delete board where bno=3;

select * from member;
select * from board;

commit;

-- 'aaa'는 primary key로 등록되어 있으므로 삭제되지 않음
delete member where id='aaa';


-- < DECODE >
select emp_name,department_id,
decode(department_id,
10,'총무기획부',
20,'마케팅',
30,'구매/생산부',
40,'인사부'
) as depart_name
from employees
order by department_id asc;

select * from stu_score order by avg desc;

-- decode는 switch/case와 같은 성격 '='외에는 사용할 수 없다
-- 90점-A, 80점-B, 70점-C
select avg,
decode(avg,
90,'A',
80,'B',
70,'C'
) as grade
from stu_score order by avg desc;
select job_id,salary from employees;


-- 월급
-- sh_clerk salary * 15%,  ad_asst *10%,  MK_rep * 5%;
select job_id, salary, decode(job_id,
'SH_CLERK',salary+(salary*0.15),
'PU_CLERK',salary+(salary*0.15),
'ST_CLERK',salary+(salary*0.15),
'SH_CLERK',salary+(salary*0.15),
'AD_ASST',salary+salary*0.1,
'MK_REP',salary+salary*0.05
) as salary_up from employees;


select job_id, salary, decode(job_id,
'SH_CLERK',salary+(salary*0.15),
'PU_CLERK',salary+(salary*0.15),
'ST_CLERK',salary+(salary*0.15),
'SH_CLERK',salary+(salary*0.15),
'AD_ASST',salary+salary*0.1,
'MK_REP',salary+salary*0.05
) as salary_up from employees;

-- error
select job_id, salary, decode(job_id,
like '%CLERK%',salary+(salary*0.15)
) as salary_up from employees;


-- job_id, clerk이 들어가 있는 job_id를 검색하시오.
select job_id from employees;

-- LIKE _ 자리수, % 모든 것
select job_id from employees
where job_id like '%CLERK%';

select name,avg from stu_score;
select name, avg,
case
when avg>=90 then 'A'
when avg>=80 then 'B'
when avg>=70 then 'C'
else 'F'
end as grade
from stu_score;


select department_id,department_name from departments;

-- case 구문, department_id, 이름을 출력하시오.
select department_id from employees
order by department_id asc;

select emp_name,department_id,
case
when department_id=10 then '총무기획부'
when department_id=20 then '마케팅'
when department_id=30 then '구매/생산부'
when department_id=40 then '인사부'
end as depart_name
from employees
order by department_id asc;


-- 월급을 출력하시오.
-- job_id
-- CLERK포함 : salary * 15%,  ad_asst *10%,  rep포함 * 5%, man포함 * 2%
-- case
select job_id,salary from employees;
select job_id,salary,
case
when job_id like '%CLERK%' then salary+(salary*0.15)
when job_id = 'AD_ASST' then salary+(salary*0.1)
when job_id like '%REP%' then salary+(salary*0.05)
when job_id like '%MAN%' then salary+(salary*0.02)
end as salary_up
from employees
order by salary_up asc;

-- 월급 평균 이하 0.15 평균이상 0.05 인상해서 출력하시오.
select avg(salary) from employees;

select emp_name,salary,
case
when salary >= 6461 then 'down'
when salary < 6461 then 'up'
end as salary_updown
from employees
order by salary asc;

-- employees에서 검색
select emp_name,salary,
case
when salary >= (select avg(salary) from employees) then salary+(salary*0.15)
when salary < (select avg(salary) from employees) then salary+(salary*0.05)
end as salary_up
from (
employees
)
order by salary_up asc;

-- salary_updown있음.
select emp_name,salary,salary_updown,
case
when salary >= (select avg(salary) from employees) then salary+(salary*0.15)
when salary < (select avg(salary) from employees) then salary+(salary*0.05)
end as salary_up
from (
select emp_name,salary,
case
when salary >= 6461 then 'down'
when salary < 6461 then 'up'
end as salary_updown
from employees
order by salary asc
)
order by salary_up asc;

-- case 2개 사용
select emp_name,salary,
case
when salary >= (select avg(salary) from employees) then 'up'
when salary < (select avg(salary) from employees) then 'down'
end as salary_updown
,
case
when salary >= (select avg(salary) from employees) then salary+(salary*0.15)
when salary < (select avg(salary) from employees) then salary+(salary*0.05)
end as salary_up
from (
employees
)
order by salary_up asc;
select * from stu_score;
select total,rank from stu_score
order by total desc
;




-- < rank() 함수 >
select total,rank, rank() over (order by total desc) as ranks from stu_score;
select no,rank() over (order by total desc) as ranks from stu_score;
select total,rank from stu_score
order by total desc;
update stu_score set rank = 1
where total=291
;

-- 1000명 순위를 각각 입력
update stu_score a
set rank = (
select ranks from(
select no,rank() over (order by total desc) as ranks from stu_score
) b
where a.no = b.no
);

update stu_score
set rank = (
1
)
;

select no,rank from stu_score
order by no;

select rank() over (order by total desc) as ranks from stu_score ;

-- 컬럼2개 no,ranks
select no,rank() over (order by total desc) as ranks from stu_score ;

-- 컬럼1개
select ranks from(
select no,rank() over (order by total desc) as ranks from stu_score
)
;

commit;



select department_id,
case
when department_id=10 then '총무기획부'
when department_id=20 then '마케팅'
when department_id=30 then '구매/생산부'
when department_id=40 then '인사부'
when department_id=40 then '인사부'
when department_id=40 then '인사부'
when department_id=40 then '인사부'
when department_id=40 then '인사부'
when department_id=40 then '인사부'
when department_id=40 then '인사부'
when department_id=40 then '인사부'
when department_id=40 then '인사부'
when department_id=40 then '인사부'
when department_id=40 then '인사부'
when department_id=40 then '인사부'
when department_id=40 then '인사부'
end as depart_name
from employees
order by department_id asc;
select emp_name,department_id from employees;
select department_id, department_name from departments
;




-- < 그룹함수 > 
--sum,avg,count,max,min  // stddev : 표준편차, variance :분산

-- 월급 총합
select sum(salary) from employees;
-- 국어점수 총합 stu_score
select sum(kor) from stu_score;
-- 전체 사원수
select count(*) from employees;
-- 부서아이디가 50인 사원수
select count(*) from employees
where department_id = 50
;
-- 커미션을 받는 사원의 수를 구하시오.
select count(*) from employees
where commission_pct is not null
;
-- 커미션이 있는 사원을 검색하시오.
select emp_name,commission_pct from employees
where commission_pct is not null;
-- 
select employee_id from employees;
select employees.employee_id from employees,departments;
-- 전체사원수
select count(*) from employees;
-- 부서번호 50번인 사원수
select count(*) from employees
where department_id = 30
;



-- < 테이블 조인(join) >
-- 2개 테이블 조인

-- employees와 departments 테이블을 조인
-- 아래의 경우 어떤 테이블에서 가지고 와야하는지 찾지 못함
select emp_name,department_id,department_name from employees,departments
-- 가지고 올 테이블의 위치를 지정해 주어야 함.
select emp_name,employees.department_id,department_name from employees,departments;
-- 두개가 같다고 정의내려주면 됨
select emp_name,employees.department_id,department_name from employees,departments
where employees.department_id = departments.department_id
;



-- 부서별 그룹지어 사원수 출력
select department_id,count(department_id) from employees
group by department_id
order by department_id
;
-- avg grade
-- stu_score 90점이상 A, 80점이상 B, 70점이상 C, 60점이상 D, 60점 미만 F
select name, avg,
case
when avg>=90 then 'A'
when avg>=80 then 'B'
when avg>=70 then 'C'
when avg>=60 then 'D'
else 'F'
end as grade
from stu_score;
-- A학점 몇명인지 출력하시오.
select avg,
case
when avg>=90 then 'A'
when avg>=80 then 'B'
when avg>=70 then 'C'
when avg>=60 then 'D'
else 'F'
end
from stu_score
where avg>=90
;
select grade,count(grade) from
(
select avg,
case
when avg>=90 then 'A'
when avg>=80 then 'B'
when avg>=70 then 'C'
when avg>=60 then 'D'
else 'F'
end as grade
from stu_score
)
group by grade
order by grade asc
;
-- total 점수를 100->100, 91,92,93,94....99->90 81,..89-> 80
-- 출력하시오.
-- trunc(total,-1)
select trunc(kor,-1),count(*) from stu_score
where trunc(kor,-1)=90
group by trunc(kor,-1)
;
-- trunc(kor,-1)를 group by 사용
select trunc(kor,-1),count(trunc(kor,-1)) from stu_score
group by trunc(kor,-1);

select k_kor,count(k_kor) as k_count from
( select trunc(kor,-1) as k_kor from stu_score )
group by k_kor
;



select nvl(department_id,0),count(*) from employees
group by department_id
order by department_id;

select emp_name, count(emp_name) from employees
group by emp_name;

-- 부서별 평균 월급을 구하시오.
select department_id, round(avg(salary),2) from employees
group by department_id
order by department_id;

-- CLERK, MEP, MAN 별 월급 평균을 구하시오

select job_id, avg(salary) as salavg from employees
where job_id like '%CLERK%'
group by job_id
order by job_id;

select job_id, avg(salary) as salavg from employees
where job_id like '%MEP%'
group by job_id
order by job_id;

select job_id, avg(salary) as salavg from employees
where job_id like '%MAN%'
group by job_id
order by job_id;


-- 1) CLERK 찾기
select job_id from employees
where job_id like '%CLERK%';
-- 2) CLERK 카운트
select job_id,count(job_id) from employees
where job_id like '%CLERK%'
group by job_id;
-- 3) CLERK만 출력되도록
select job_id, emp_name, substr(job_id,4,5) from employees
where job_id like '%CLERK%';

select job_id,substr(job_id,4,length(job_id)-3) from employees;

select substr(job_id,4,7) as job_id, count(substr(job_id,4,7)) as c_job_id from employees
group by substr(job_id,4,7)
order by c_job_id;



-- 부서별 최대월급, 최소월급, 평균월급을 출력하시오
select * from employees;

select department_id,department_name, count(department_id),max(salary), min(salary), trunc(avg(salary),2) from employees
group by department_id
order by department_id;

select a.department_id,department_name, count(salary), sum(salary),round(avg(salary),2), max(salary), min(salary) from employees a, departments b
where a.department_id= b.department_id
group by a.department_id, department_name
order by a.department_id
;


select count(commission_pct) from employees
where commission_pct is not null
order by department_id;

-- 부서별 사원수, 커미션을 받는 사원수를 출력
select department_id, count(department_id), count(commission_pct) from employees
group by department_id ;




-- having group by 조건절, where 일반 컬럼의 조건절
select department_id, round(avg(salary),2) from employees
group by department_id
order by avg(salary);

-- emp_name 두번째 글자가 a로 시작하는 것은 제외
select department_id, round(avg(salary),2) from employees
where emp_name not like '_a%' 
group by department_id
having avg(salary) >= 6000
order by avg(salary);

select department_id, round(avg(salary),2) from employees
where emp_name not like '_a%' 
group by department_id
having avg(salary) >= (select avg(salary) from employees)
order by avg(salary)
;

-- 부서별 최대월급이 8000 이상인 부서, 최대월급을 출력하시오
select department_id, max(salary) from employees
group by department_id
having max(salary) >= 8000
order by avg(salary)
;



-- < Join : 테이블 간의 관계 설계 >
-- department_id, department_name 중복
select emp_name, department_id, department_name, salary from employees;
select department_id, department_name from departments;

select count(*) from employees; 
select count(*) from departments;

-- 각 테이블의 튜플 개수의 곱으로 표현됨 : 107 * 27 -> 의미없음 : Cross Join
select count(*) from employees, departments;

select * from employees, departments;

-- 1) Equi Join : 106개 (null은 검색되지 않음)
-- 두 테이블 간 같은 컬럼을 가지고 비교해서 해당되는 데이터를 출력
select employee_id, emp_name, employees.department_id, department_name, salary 
from employees, departments
where employees.department_id = departments.department_id; 

select department_id, department_name from departments;


-- ID 대신 사용자명을 넣고 싶을 때
select * from board;
select * from member;

select id, name from member;
select id, btitle, bcontent from board;

update member set name='홍길자'
where id = 'aaa';


select member.id, name, btitle, bcontent from board, member
where member.id = board.id;

select bno, name, gender, btitle, bcontent, dbdate, bgroup, bstep,bindent,bhit,bfile from board, member
where member.id = board.id;












