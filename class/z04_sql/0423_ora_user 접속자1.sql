select * from students;

-- ��������
select * from students
order by name asc;

-- drop table students;

-- �÷��߰�
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

-- 1���� �� ���� �����͸� ����
update students set total = (kor+eng+math);

-- rank()�� total�̶�� �÷� ��ü�� ������ ���� ���̹Ƿ� ����-> �񱳸� �� �־�� �Ѵ�
update students s1 set rank = (select ranks
from (select no no2, rank() over(order by total desc ) as ranks from students) s2
where s1.no = s2.no2 )
;

-- 1. update ����
update student a set rank = (rank);

-- 2. no,rank() ���� -> table�� �ʹ� �� ��Ī�� ��
(select no,rank() over(order by total desc) ranks from students) b;

-- 3. update ������ rank ������ no �÷����� ��, rank �÷��� �˻�
update students a set rank = (  --rank�� �����ϱ�
(select ranks from (students) b            --(students)�� ranks�� �ٲپ� �־�� ��
where a.no = b.no
);

-- 4. students ���̺��� ranks�� �� �ִ� ���̺��� �־���
update students a set rank = (  --rank�� �����ϱ�
(select ranks from (select no,rank() over(order by total desc) ranks from students) b            
where a.no = b.no)
);

-- ��������
select no,total,rank from students
order by total desc;

-- no ��������
select no,total,rank from students
order by total asc;

select no,kor,eng,math,total,rank from students
order by kor desc, eng asc;

select manager_id from employees
order by manager_id desc;

-- max/min : �ִ�/�ּҰ� ���� �Ͽ� ���
select max(hire_date) -min(hire_date) from employees
order by hire_date desc;

select max(kor)-min(kor) from students;
select max(kor),max(eng),max(math) from students;

-- ���� 1.
-- �Ի��Ϸ� ��������, �÷� �����ȣ, �����, job_id-����, ���� �÷��� ����Ͻÿ�.
select * from employees;
select employee_id, emp_name,job_id,hire_date,salary from employees 
order by hire_date asc;

-- ���� 2. 
-- �޿��� ���� �޴� ������ ����ϵ� ������ ������, ��������� ���������Ͻÿ�.
select emp_name, salary from employees
order by salary, emp_name desc;

-- �����Լ�
-- abs : ���밪
select -10, abs(-10) from dual;

-- floor �Ҽ��� ���� ����
select 34.789, floor(34.789) as f0,round(34.789) as r from dual;
-- round(���,�ڸ���) ex) round(34.178,2) 2�ڸ����� ǥ��
select 34.178,round(34.178), round(34.178,2) from dual;

select * avg from students;
select round(avg,2) from students;

-- ������ �Ҽ��� ��ĭ
select 34.5678, round(34.5678,-1) from students;

-- trunc ������ �ڸ��� ���� ����
select trunc(34.5678,2) from dual;

select trunc(34.5678,-1) from dual;

select trunc(34.5678) from dual;

-- ceil : �ø�
select ceil(34.123) from dual;

-- �������� �ϴ��� �����ؼ� ����Ͻÿ�
select trunc(kor,-1) from students
order by kor;

-- ����, ����, ���� ������ �ϴ��� �����ؼ� ���� ����Ͻÿ�
select trunc(kor,-1), trunc(eng,-1), trunc(math,-1), (kor+eng+math)as t3 from students;

select trunc(kor,-1) ����,trunc(eng,-1) ����, trunc(math,-1) ����,(trunc(kor-1)+trunc(eng-1) + trunc(math-1)) total from students; 

-- mod : ������-> (�־����� ��,������ ��)
select round(100/7,2) from dual;
select mod(10,7) from dual;

-- ������
select 10/7 from dual;

-- ����: �����ȣ�� ¦���� ���� ����Ͻÿ�
-- ���̽� : employee_id%2 =0
select employee_id from employees;

select employee_id from employees
where mod(employee_id,2)=0;

-- ��
select floor(10/7) form dual;
-- ������ : �������� 0�̸� ¦��, 1�̸� Ȧ��
select mod(10,7) from dual;

-- ����: �й��� 3�� ����ΰ͸� ����Ͻÿ�
select * from students;
select no, name from students
where mod(no,3)=0;

-- ������
create sequence seq_no 
increment by 1 -- ���� 1�� ��
start with 1   -- ������ 1���� ����
minvalue 1     -- �ּҰ� 1
maxvalue 9999  -- �ִ밪 ���� 9999
nocycle        -- ��ȯ���� ����
nocache        -- ĳ�û�� ����
;

-- nextval ��������ȣ 1�� ����
select seq_no.nextval from dual;

-- currval ������ ��ȣ Ȯ��
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
seq_mno.nextval,'aaa','1111','ȫ�浿','010-1111-1111'
);

select * from member;

select 's000'+seq_mno.currval from dual;

select sysdate from dual;
select to_char(sysdate,'yy') from dual;

-- '00000' �ڸ���
select 's'||to_char(seq_mno.nextval,'00000') from dual; -- ������

-- ����
-- �ѱ����б� ko20240001.....
-- ������ seq_kono 1-99999
create sequence seq_kono
increment by 1
start with 1
minvalue 1
maxvalue 99999
nocycle
nocache
;
select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(seq_kono.nextval,'00000')) as stuno from dual;


-- �Խ���
create table board (
bno number(5) primary key,
btitle varchar2(1000),
bcontent varchar2(3000),
id varchar2(30),
bdate date,
bhit number(10)--��ȸ��
);



-- ����
-- ������ �̸�: seq_deptno ����1001, ����10, �ּ�: 1, �ִ�:99999
-- 5�� ������ �� ������
-- cycle -> �ߺ��� ��, ���� ��ȣ�� ���� ����
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
emp_seq.nextval, '�̼���', sysdate
);

select * from emp01;

commit;



select * from employees;

select employee_id, emp_name, job_id, hire_date from employees
order by hire_date desc;

-- ������� �Ի��� �ϼ��� �Բ� ����Ͻÿ�(�Ҽ��� �ø�
select employee_id, emp_name, hire_date, ceil(sysdate-hire_date)||'��' as period 
from employees
order by hire_date desc;

select emp_name from employees;

-- ����: ���ް� ����� ���ļ� ����Ͻÿ�
select employee_id||job_id as idname from employees;

select job_id||employee_id from employees;

select substr(job_id,0,2) from employees;

select substr(emp_name,1,3) from employees;

-- substr ���ڿ� �ڸ��� �Լ�, substr(���,������ġ,����)
select substr('abcde',2,3) from dual;

-- ����
-- job_id �տ� 2�� ���ڿ� ���5�ڸ� 00101�� ����� �Բ� ����Ͻÿ�
select job_id, employee_id from employees;

select substr(job_id,0,2)||'00'||employee_id from employees;

select substr(job_id,0,2),employee_id, to_char(employee_id,'00000'),
substr(job_id,0,2)||trim(to_char(employee_id,'00000')) from employees;

select substr(job_id,0,2), employee_id, to_char(employee_id,'00000'),
substr(job_id,0,2)||trim(to_char(employee_id,'00000')) from employees;

-- ��¥�Լ�
select sysdate from dual;

select to_char(sysdate,'yyyy-mm-dd hh24:mi:ss')from dual;


-- �γ�¥ ������ ������ Ȯ��
select months_between(sysdate,hire_date), sysdate-hire_date from employees;

-- �������� �߰�
select sysdate,add_months(sysdate,2) from dual;

-- �Է��� �������� ������ ������ �˷���
select next_day(sysdate,'������') from dual;

-�Է��� �������� ������ ���� �˷���.
select last_day(sysdate) from dual;

select last_day('2024-02-02')from dual;















