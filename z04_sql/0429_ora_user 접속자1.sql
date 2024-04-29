-- drop table member;
-- ���Ἲ �������� : �������� �ڷᰡ �Էµ��� �ʵ��� �ϱ� ���� ��Ģ
-- not null, unique, primary key, foreign key, check


create table member(
memNo number(4) not null,
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30),
gender varchar2(6) check(gender in('����','����')),
mdate date default sysdate
);


-- ������ �Է�,���,����,���� �κ�
insert into member (memNo,id,pw,name,gender,mdate) values (
member_seq.nextval,'aaa','1111','ȫ�浿','����',sysdate
);
insert into member(memNo,id,pw,name,gender) values(
member_seq.nextval,'bbb','1111','������','����'
);
insert into member values(
member_seq.nextval,'ccc','1111','�̼���','����',sysdate
);

select * from member;

--���̺���� : �Խ��� ���̺���
create table board (
bno number(4) primary key,
id varchar2(30), -- �ܷ�Ű ���
btitle varchar2(1000),
bcontent varchar2(4000),
dbdate date default sysdate,
bgroup number(4),
bstep number default 0,
bindent number default 0,
bhit number default 1,
bfile varchar2(100) default '',
constraint fk_board_id foreign key(id)    -- �ܷ�Ű(foreign key)�� ��Ī: fk_id
references member(id)                     -- member���̺��� primary key id
);

alter

select * from member;

insert into board(bno,id,btitle,bcontent,dbdate,bgroup,bstep,bindent,bhit,bfile) values (
board_seq.nextval,'aaa','�����Դϴ�.','�����Դϴ�',sysdate,board_seq.currval,0,0,1,''
);

insert into board values (
board_seq.nextval,'bbb','�����Դϴ�2.','�����Դϴ�2',sysdate,board_seq.currval,0,0,1,''
);

insert into board(bno,id,btitle,bcontent,bgroup) values (
board_seq.nextval,'aaa','�����Դϴ�.3','�����Դϴ�3',board_seq.currval
);
-- primary key�� �����Ϸ��� foreign key ��ϵǾ� �ִ� �����͸� �켱 ������ ����ؾ� ��.
-- primary key �����Ǹ� ��λ����ϴ� ��� - on delete cascade, ��� �����ϴ� ��� on update cascade

-- ����
delete board where bno=3;

select * from member;
select * from board;

commit;

-- 'aaa'�� primary key�� ��ϵǾ� �����Ƿ� �������� ����
delete member where id='aaa';


-- < DECODE >
select emp_name,department_id,
decode(department_id,
10,'�ѹ���ȹ��',
20,'������',
30,'����/�����',
40,'�λ��'
) as depart_name
from employees
order by department_id asc;

select * from stu_score order by avg desc;

-- decode�� switch/case�� ���� ���� '='�ܿ��� ����� �� ����
-- 90��-A, 80��-B, 70��-C
select avg,
decode(avg,
90,'A',
80,'B',
70,'C'
) as grade
from stu_score order by avg desc;
select job_id,salary from employees;


-- ����
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


-- job_id, clerk�� �� �ִ� job_id�� �˻��Ͻÿ�.
select job_id from employees;

-- LIKE _ �ڸ���, % ��� ��
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

-- case ����, department_id, �̸��� ����Ͻÿ�.
select department_id from employees
order by department_id asc;

select emp_name,department_id,
case
when department_id=10 then '�ѹ���ȹ��'
when department_id=20 then '������'
when department_id=30 then '����/�����'
when department_id=40 then '�λ��'
end as depart_name
from employees
order by department_id asc;


-- ������ ����Ͻÿ�.
-- job_id
-- CLERK���� : salary * 15%,  ad_asst *10%,  rep���� * 5%, man���� * 2%
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

-- ���� ��� ���� 0.15 ����̻� 0.05 �λ��ؼ� ����Ͻÿ�.
select avg(salary) from employees;

select emp_name,salary,
case
when salary >= 6461 then 'down'
when salary < 6461 then 'up'
end as salary_updown
from employees
order by salary asc;

-- employees���� �˻�
select emp_name,salary,
case
when salary >= (select avg(salary) from employees) then salary+(salary*0.15)
when salary < (select avg(salary) from employees) then salary+(salary*0.05)
end as salary_up
from (
employees
)
order by salary_up asc;

-- salary_updown����.
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

-- case 2�� ���
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




-- < rank() �Լ� >
select total,rank, rank() over (order by total desc) as ranks from stu_score;
select no,rank() over (order by total desc) as ranks from stu_score;
select total,rank from stu_score
order by total desc;
update stu_score set rank = 1
where total=291
;

-- 1000�� ������ ���� �Է�
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

-- �÷�2�� no,ranks
select no,rank() over (order by total desc) as ranks from stu_score ;

-- �÷�1��
select ranks from(
select no,rank() over (order by total desc) as ranks from stu_score
)
;

commit;



select department_id,
case
when department_id=10 then '�ѹ���ȹ��'
when department_id=20 then '������'
when department_id=30 then '����/�����'
when department_id=40 then '�λ��'
when department_id=40 then '�λ��'
when department_id=40 then '�λ��'
when department_id=40 then '�λ��'
when department_id=40 then '�λ��'
when department_id=40 then '�λ��'
when department_id=40 then '�λ��'
when department_id=40 then '�λ��'
when department_id=40 then '�λ��'
when department_id=40 then '�λ��'
when department_id=40 then '�λ��'
when department_id=40 then '�λ��'
when department_id=40 then '�λ��'
end as depart_name
from employees
order by department_id asc;
select emp_name,department_id from employees;
select department_id, department_name from departments
;




-- < �׷��Լ� > 
--sum,avg,count,max,min  // stddev : ǥ������, variance :�л�

-- ���� ����
select sum(salary) from employees;
-- �������� ���� stu_score
select sum(kor) from stu_score;
-- ��ü �����
select count(*) from employees;
-- �μ����̵� 50�� �����
select count(*) from employees
where department_id = 50
;
-- Ŀ�̼��� �޴� ����� ���� ���Ͻÿ�.
select count(*) from employees
where commission_pct is not null
;
-- Ŀ�̼��� �ִ� ����� �˻��Ͻÿ�.
select emp_name,commission_pct from employees
where commission_pct is not null;
-- 
select employee_id from employees;
select employees.employee_id from employees,departments;
-- ��ü�����
select count(*) from employees;
-- �μ���ȣ 50���� �����
select count(*) from employees
where department_id = 30
;



-- < ���̺� ����(join) >
-- 2�� ���̺� ����

-- employees�� departments ���̺��� ����
-- �Ʒ��� ��� � ���̺��� ������ �;��ϴ��� ã�� ����
select emp_name,department_id,department_name from employees,departments
-- ������ �� ���̺��� ��ġ�� ������ �־�� ��.
select emp_name,employees.department_id,department_name from employees,departments;
-- �ΰ��� ���ٰ� ���ǳ����ָ� ��
select emp_name,employees.department_id,department_name from employees,departments
where employees.department_id = departments.department_id
;



-- �μ��� �׷����� ����� ���
select department_id,count(department_id) from employees
group by department_id
order by department_id
;
-- avg grade
-- stu_score 90���̻� A, 80���̻� B, 70���̻� C, 60���̻� D, 60�� �̸� F
select name, avg,
case
when avg>=90 then 'A'
when avg>=80 then 'B'
when avg>=70 then 'C'
when avg>=60 then 'D'
else 'F'
end as grade
from stu_score;
-- A���� ������� ����Ͻÿ�.
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
-- total ������ 100->100, 91,92,93,94....99->90 81,..89-> 80
-- ����Ͻÿ�.
-- trunc(total,-1)
select trunc(kor,-1),count(*) from stu_score
where trunc(kor,-1)=90
group by trunc(kor,-1)
;
-- trunc(kor,-1)�� group by ���
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

-- �μ��� ��� ������ ���Ͻÿ�.
select department_id, round(avg(salary),2) from employees
group by department_id
order by department_id;

-- CLERK, MEP, MAN �� ���� ����� ���Ͻÿ�

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


-- 1) CLERK ã��
select job_id from employees
where job_id like '%CLERK%';
-- 2) CLERK ī��Ʈ
select job_id,count(job_id) from employees
where job_id like '%CLERK%'
group by job_id;
-- 3) CLERK�� ��µǵ���
select job_id, emp_name, substr(job_id,4,5) from employees
where job_id like '%CLERK%';

select job_id,substr(job_id,4,length(job_id)-3) from employees;

select substr(job_id,4,7) as job_id, count(substr(job_id,4,7)) as c_job_id from employees
group by substr(job_id,4,7)
order by c_job_id;



-- �μ��� �ִ����, �ּҿ���, ��տ����� ����Ͻÿ�
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

-- �μ��� �����, Ŀ�̼��� �޴� ������� ���
select department_id, count(department_id), count(commission_pct) from employees
group by department_id ;




-- having group by ������, where �Ϲ� �÷��� ������
select department_id, round(avg(salary),2) from employees
group by department_id
order by avg(salary);

-- emp_name �ι�° ���ڰ� a�� �����ϴ� ���� ����
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

-- �μ��� �ִ������ 8000 �̻��� �μ�, �ִ������ ����Ͻÿ�
select department_id, max(salary) from employees
group by department_id
having max(salary) >= 8000
order by avg(salary)
;



-- < Join : ���̺� ���� ���� ���� >
-- department_id, department_name �ߺ�
select emp_name, department_id, department_name, salary from employees;
select department_id, department_name from departments;

select count(*) from employees; 
select count(*) from departments;

-- �� ���̺��� Ʃ�� ������ ������ ǥ���� : 107 * 27 -> �ǹ̾��� : Cross Join
select count(*) from employees, departments;

select * from employees, departments;

-- 1) Equi Join : 106�� (null�� �˻����� ����)
-- �� ���̺� �� ���� �÷��� ������ ���ؼ� �ش�Ǵ� �����͸� ���
select employee_id, emp_name, employees.department_id, department_name, salary 
from employees, departments
where employees.department_id = departments.department_id; 

select department_id, department_name from departments;


-- ID ��� ����ڸ��� �ְ� ���� ��
select * from board;
select * from member;

select id, name from member;
select id, btitle, bcontent from board;

update member set name='ȫ����'
where id = 'aaa';


select member.id, name, btitle, bcontent from board, member
where member.id = board.id;

select bno, name, gender, btitle, bcontent, dbdate, bgroup, bstep,bindent,bhit,bfile from board, member
where member.id = board.id;












