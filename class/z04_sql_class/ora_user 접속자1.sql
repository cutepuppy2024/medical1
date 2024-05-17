select * from employees;

-- 회원정보 테이블 생성
create table member (
id varchar2(20),
pw varchar2(20),
name varchar2(20),
phone varchar2(20)
);
-- 데이터 입력
insert into member (id,pw,name,phone) values (
'aaa','1111','홍길동','010-1111-1111'
);

insert into member values (
'bbbb','1111','유관순','010-222-2222'
);

insert into member(id,pw,phone) values(
'ccc','이순신','010-333-3333'
);

-- 컬럼수 부족 에러
/*
insert into member values (
'ddd','강감찬','010-444-4444'
);
*/

select id,pw,name,phone from member;

commit;

rollback;

select id, name from member;
select * from member;

insert into member values(
'ddd','1111','강감찬','000-444-4444'
);

select * from member;

rollback;

commit;

select * from member;

update member set pw='2222' where id='ccc';

select * from member;

rollback;

-- 모든 테이블 확인
select * from tab;

-- 테이블의 타입 확인
desc member;

-- 오라클 타입
-- number-숫자, date-날짜, char-고정문자, varchar2-가변문자, clob-대용량문자

-- number : 정수, 실수
-- number(4) : -9999~9999

create table mem (
no number, -- 길이 지정하지 않음.
no2 number(4),
no3 number(4,2)
);

insert into mem (no) values ( 1234567890 );
insert into mem (no2) values(9999);
insert into mem (no2) values(1.11); -- 소수점 자리가 지정되어 있지 않아 1만 테이블에 들어간다
insert into mem (no2) values(-9999);
insert into mem (no2) values(-99999);

insert into mem (no3) values(11.11);
insert into mem (no3) values(111); -- 실제값은 111.00 이므로 오류

select * from mem;

commit;

create table mem2 (
 no number(4,2),
 mdate date,
 mdate2 timestamp -- date : 년,월,일,시,분,초까지 저장가능 = timestamp : 밀리초까지 저장가능함.
);

insert into mem2(mdate) values ('2024-04-19'); -- 24/04/19 디폴트 형태로 출력됨(이 데이터 값에는 시분초(00:00:00)가 포함되어 있음
insert into mem2(mdate) values(sysdate); -- 현재시간 
insert into mem2(mdate2) values(sysdate);
insert into mem2(mdate, mdate2) values (susdate,susdate+30); 

select * from mem2;
select to_char(mdate,'yyyy-mm-dd hh:mi:ss:ff') from mem2; -- ff지원하지 않는다
select to_char(mdate2,'yyyy-mm-dd hh:mi:ss:ff') from mem2;

select mdate,mdate+30 from mem2;

select * from employees;

select sysdate-hire_date from employees;

create table mem3 (
 no number(4,2), 
 tel char(8),
 name varchar2(9),
 mdate date,
 mdate2 timestamp
);

-- char,varchar2
-- char : 고정문자
insert into mem3 (tel) values('11112222');
insert into mem3 (tel) values('22223333');
insert into mem3 (tel) values('111');
insert into mem3 (tel) values('123456789');
insert into mem3 (tel) values ('홍');

-- varchar2 : 가변문자
insert into mem3 (name) values('11112222');
insert into mem3 (name) values('홍길동'); -- 한글 : 3크기
insert into mem3 (name) values('신사임당'); -- 12자리 필요
INSERT INTO MEM3(NAME) VALUES('AAA');
insert into mem3(name) values('aaa');

commit;

-- 아무의미가 없다select * from mem,mem2; 

select * from mem3 where lower(name)='aaa'; -- sql 구문은 대소문자 구분없음, 데이터는 대소문자 구분함.
select * from mem3 where name='aaa';
select * from mem3 where name='AAA';

-- select, from 2개의 키워드로 구성됨
-- * 모든 컬럼을 출력
-- 대소문자를 구분하지 않음(데이터는 구분함)

select * from mem;
SELECT * FROM MEM;

select emp_name,department_id from employees;

-- distinct : 같은 것은 1번만 출력(중복된것 빼기)
select distinct department_id from employees;

select * from departments;
select department_name, department_id from departments;

select * from departments;
select * from employees;
select * from jobs;
select * from products;

select employee_id,emp_name,salary from employees;
select employee_id, job_id,a.* from employees a; -- 쓰는 순서대로 출력됨, 별칭으로 쓰는 a 설정가능

select * from mem3;
select no,mdate2,tel,name,mdate from mem3;

select * from employees;

-- 사원번호(emp_id), 사원이름(e name), 급여(salary), 입사일자(hire_date)
select employee_id, emp_name, salary, hire_date from employees;

desc employees;

select * from stu_score;

drop table stu_score;

create table stu_score (
 no number,
 name varchar2(30),
 kor number(3),
 eng number(3),
 math number(3),
 total number(3),
 avg number(5,2),
 rank number
);

insert into stu_score values (
 1,'홍길동',100,100,100,300,100,1
);
insert into stu_score values (
 2,'이순신',100,100,100,300,100,1
);
insert into stu_score values (
 5,'김구',100,100,100,300,100,1
);

commit;

select * from stu_score;

-- 산술연산자 number 타입인 경우만 가능

select * from stu_score;

insert into stu_score values (
6,'김유신', 100,95,96,(100+95+96),(100+95+96)/3,1
);

select * from stu_score;

insert into stu_score values (
7,'홍길자',100,100,99,(100+100+99),(100+100+99)/3,1
);

-- 번호, 이름, 국어점수, 국어점수-20, 평균, 국어점수-20을 한 평균
select no,name,kor,kor-20,avg,(kor-20+eng+math)/3 from stu_score;

select * from employees;

-- 달러 -> 원화환산 1달러 = 1381.79원
select employee_id,emp_name,salary from employees;

select employee_id,emp_name,salary,salary*1381.79 from employees;

-- 월급 * 12  = 년봉
select employee_id, emp_name, salary, salary*12, salary*12*1381.79 from employees;

-- 실제월급 = 월급 + 월급*커미션
-- commission_pct
select * from employees;

select employee_id,emp_name,commission_pct, salary+(salary*commission_pct)from employees;

-- nvl(컬럼,0)
select employee_id, emp_name,nvl(commission_pct,0),salary+(salary*nvl(commission_pct,0)) from employees;





