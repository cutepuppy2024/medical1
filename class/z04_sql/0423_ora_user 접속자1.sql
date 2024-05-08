select * from students;

-- 순차정렬
select * from students
order by name asc;

-- drop table students;

-- 컬럼추가
alter table students add rank number(3);

select * from students;

update students set rank = 0;

commit;

select * from students;

select total, rank from students;

select rank() over(order by total desc) rank
from students;

update students set total = 0;

select * from students;

-- 1개의 행 내의 데이터를 연산
update students set total = (kor+eng+math);

-- rank()는 total이라는 컬럼 전체의 값들을 비교한 것이므로 에러-> 비교를 해 주어야 한다
update students s1 set rank = (select ranks
from (select no no2, rank() over(order by total desc ) as ranks from students) s2
where s1.no = s2.no2 )
;

-- 1. update 구문
update student a set rank = (rank);

-- 2. no,rank() 구문 -> table이 너무 길어서 별칭을 줌
(select no,rank() over(order by total desc) ranks from students) b;

-- 3. update 구문과 rank 구문을 no 컬럼으로 비교, rank 컬럼을 검색
update students a set rank = (  --rank만 있으니까
(select ranks from (students) b            --(students)를 ranks로 바꾸어 주어야 함
where a.no = b.no
);

-- 4. students 테이블에서 ranks가 들어가 있는 테이블을 넣어줌
update students a set rank = (  --rank만 있으니까
(select ranks from (select no,rank() over(order by total desc) ranks from students) b            
where a.no = b.no)
);

-- 역순정렬
select no,total,rank from students
order by total desc;

-- no 순차정렬
select no,total,rank from students
order by total asc;

select no,kor,eng,math,total,rank from students
order by kor desc, eng asc;

select manager_id from employees
order by manager_id desc;

-- max/min : 최대/최소값 적용 하여 계산
select max(hire_date) -min(hire_date) from employees
order by hire_date desc;

select max(kor)-min(kor) from students;
select max(kor),max(eng),max(math) from students;

-- 퀴즈 1.
-- 입사일로 오름차순, 컬럼 사원번호, 사원명, job_id-직급, 월급 컬럼을 출력하시오.
select * from employees;
select employee_id, emp_name,job_id,hire_date,salary from employees 
order by hire_date asc;

-- 퀴즈 2. 
-- 급여를 적게 받는 순으로 출력하되 월급이 같으면, 사원명으로 역순정렬하시오.
select emp_name, salary from employees
order by salary, emp_name desc;

-- 숫자함수
-- abs : 절대값
select -10, abs(-10) from dual;

-- floor 소수점 이하 버림
select 34.789, floor(34.789) as f0,round(34.789) as r from dual;
-- round(대상,자리수) ex) round(34.178,2) 2자리까지 표시
select 34.178,round(34.178), round(34.178,2) from dual;

select * avg from students;
select round(avg,2) from students;

-- 음수는 소수점 앞칸
select 34.5678, round(34.5678,-1) from students;

-- trunc 지정한 자리수 이하 버림
select trunc(34.5678,2) from dual;

select trunc(34.5678,-1) from dual;

select trunc(34.5678) from dual;

-- ceil : 올림
select ceil(34.123) from dual;

-- 국어점수 일단위 절사해서 출력하시오
select trunc(kor,-1) from students
order by kor;

-- 국어, 영어, 수학 점수를 일단위 절사해서 합을 출력하시오
select trunc(kor,-1), trunc(eng,-1), trunc(math,-1), (kor+eng+math)as t3 from students;

select trunc(kor,-1) 국어,trunc(eng,-1) 영어, trunc(math,-1) 수학,(trunc(kor-1)+trunc(eng-1) + trunc(math-1)) total from students; 

-- mod : 나머지-> (주어지는 수,나누는 수)
select round(100/7,2) from dual;
select mod(10,7) from dual;

-- 나누기
select 10/7 from dual;

-- 퀴즈: 사원번호가 짝수인 것을 출력하시오
-- 파이썬 : employee_id%2 =0
select employee_id from employees;

select employee_id from employees
where mod(employee_id,2)=0;

-- 몫
select floor(10/7) form dual;
-- 나머지 : 나머지가 0이면 짝수, 1이면 홀수
select mod(10,7) from dual;

-- 퀴즈: 학번이 3의 배수인것만 출력하시오
select * from students;
select no, name from students
where mod(no,3)=0;

-- 시퀀스
create sequence seq_no 
increment by 1 -- 증감 1씩 됨
start with 1   -- 시작이 1부터 진행
minvalue 1     -- 최소값 1
maxvalue 9999  -- 최대값 설정 9999
nocycle        -- 순환하지 않음
nocache        -- 캐시사용 안함
;

-- nextval 시퀀스번호 1씩 증가
select seq_no.nextval from dual;

-- currval 시퀀스 번호 확인
select seq_no.currval from dual;

--drop table member;

--drop table mem;

create table member(
mno number(4),
id varchar2(30),
pw varchar2(20),
name varchar2(30),
phone varchar2(15)
);

create sequence seq_mno
increment by 1
start with 1
minvalue 1
maxvalue 9999
nocycle
nocache
;


select seq_mno.nextval from dual;

insert into member values (
seq_mno.nextval,'aaa','1111','홍길동','010-1111-1111'
);

select * from member;

select 's000'+seq_mno.currval from dual;

select sysdate from dual;
select to_char(sysdate,'yy') from dual;

-- '00000' 자리수
select 's'||to_char(seq_mno.nextval,'00000') from dual; -- 합쳐짐

-- 퀴즈
-- 한국대학교 ko20240001.....
-- 시퀀스 seq_kono 1-99999
create sequence seq_kono
increment by 1
start with 1
minvalue 1
maxvalue 99999
nocycle
nocache
;
select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(seq_kono.nextval,'00000')) as stuno from dual;


-- 게시판
create table board (
bno number(5) primary key,
btitle varchar2(1000),
bcontent varchar2(3000),
id varchar2(30),
bdate date,
bhit number(10)--조회수
);



-- 퀴즈
-- 시퀀스 이름: seq_deptno 시작1001, 증감10, 최소: 1, 최대:99999
-- 5번 실행을 해 보세요
-- cycle -> 중복이 됨, 같은 번호가 들어가면 에러
create sequence seq_deptn
start with 1001
increment by 10
minvalue 1
maxvalue 99999
cycle
nocache
;

select to_char(seq_deptno.nextval,'00000') as num from dual;


create table emp01(
empno number(4) primary key,
ename varchar(30),
hare_date date
);

create sequence emp_seq
increment by 1
start with 1
minvalue 1
maxvalue 9999
nocycle
nocache
;

alter sequence emp_seq
increment by 1001
;

insert into emp01 values(
emp_seq.nextval, '이순신', sysdate
);

select * from emp01;

commit;



select * from employees;

select employee_id, emp_name, job_id, hire_date from employees
order by hire_date desc;

-- 현재까지 입사한 일수를 함께 출력하시오(소수점 올림
select employee_id, emp_name, hire_date, ceil(sysdate-hire_date)||'일' as period 
from employees
order by hire_date desc;

select emp_name from employees;

-- 퀴즈: 직급과 사번을 합쳐서 출력하시오
select employee_id||job_id as idname from employees;

select job_id||employee_id from employees;

select substr(job_id,0,2) from employees;

select substr(emp_name,1,3) from employees;

-- substr 문자열 자르기 함수, substr(대상,시작위치,개수)
select substr('abcde',2,3) from dual;

-- 퀴즈
-- job_id 앞에 2개 문자와 사번5자리 00101를 만들어 함께 출력하시오
select job_id, employee_id from employees;

select substr(job_id,0,2)||'00'||employee_id from employees;

select substr(job_id,0,2),employee_id, to_char(employee_id,'00000'),
substr(job_id,0,2)||trim(to_char(employee_id,'00000')) from employees;

select substr(job_id,0,2), employee_id, to_char(employee_id,'00000'),
substr(job_id,0,2)||trim(to_char(employee_id,'00000')) from employees;

-- 날짜함수
select sysdate from dual;

select to_char(sysdate,'yyyy-mm-dd hh24:mi:ss')from dual;


-- 두날짜 사이의 개월수 확인
select months_between(sysdate,hire_date), sysdate-hire_date from employees;

-- 개월수를 추가
select sysdate,add_months(sysdate,2) from dual;

-- 입력한 기준으로 다음번 요일을 알려줌
select next_day(sysdate,'월요일') from dual;

-입력한 기준으로 마지막 일을 알려줌.
select last_day(sysdate) from dual;

select last_day('2024-02-02')from dual;















