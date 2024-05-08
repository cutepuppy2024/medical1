select * from employees;

-- ȸ������ ���̺� ����
create table member (
id varchar2(20),
pw varchar2(20),
name varchar2(20),
phone varchar2(20)
);
-- ������ �Է�
insert into member (id,pw,name,phone) values (
'aaa','1111','ȫ�浿','010-1111-1111'
);

insert into member values (
'bbbb','1111','������','010-222-2222'
);

insert into member(id,pw,phone) values(
'ccc','�̼���','010-333-3333'
);

-- �÷��� ���� ����
/*
insert into member values (
'ddd','������','010-444-4444'
);
*/

select id,pw,name,phone from member;

commit;

rollback;

select id, name from member;
select * from member;

insert into member values(
'ddd','1111','������','000-444-4444'
);

select * from member;

rollback;

commit;

select * from member;

update member set pw='2222' where id='ccc';

select * from member;

rollback;

-- ��� ���̺� Ȯ��
select * from tab;

-- ���̺��� Ÿ�� Ȯ��
desc member;

-- ����Ŭ Ÿ��
-- number-����, date-��¥, char-��������, varchar2-��������, clob-��뷮����

-- number : ����, �Ǽ�
-- number(4) : -9999~9999

create table mem (
no number, -- ���� �������� ����.
no2 number(4),
no3 number(4,2)
);

insert into mem (no) values ( 1234567890 );
insert into mem (no2) values(9999);
insert into mem (no2) values(1.11); -- �Ҽ��� �ڸ��� �����Ǿ� ���� �ʾ� 1�� ���̺� ����
insert into mem (no2) values(-9999);
insert into mem (no2) values(-99999);

insert into mem (no3) values(11.11);
insert into mem (no3) values(111); -- �������� 111.00 �̹Ƿ� ����

select * from mem;

commit;

create table mem2 (
 no number(4,2),
 mdate date,
 mdate2 timestamp -- date : ��,��,��,��,��,�ʱ��� ���尡�� = timestamp : �и��ʱ��� ���尡����.
);

insert into mem2(mdate) values ('2024-04-19'); -- 24/04/19 ����Ʈ ���·� ��µ�(�� ������ ������ �ú���(00:00:00)�� ���ԵǾ� ����
insert into mem2(mdate) values(sysdate); -- ����ð� 
insert into mem2(mdate2) values(sysdate);
insert into mem2(mdate, mdate2) values (susdate,susdate+30); 

select * from mem2;
select to_char(mdate,'yyyy-mm-dd hh:mi:ss:ff') from mem2; -- ff�������� �ʴ´�
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
-- char : ��������
insert into mem3 (tel) values('11112222');
insert into mem3 (tel) values('22223333');
insert into mem3 (tel) values('111');
insert into mem3 (tel) values('123456789');
insert into mem3 (tel) values ('ȫ');

-- varchar2 : ��������
insert into mem3 (name) values('11112222');
insert into mem3 (name) values('ȫ�浿'); -- �ѱ� : 3ũ��
insert into mem3 (name) values('�Ż��Ӵ�'); -- 12�ڸ� �ʿ�
INSERT INTO MEM3(NAME) VALUES('AAA');
insert into mem3(name) values('aaa');

commit;

-- �ƹ��ǹ̰� ����select * from mem,mem2; 

select * from mem3 where lower(name)='aaa'; -- sql ������ ��ҹ��� ���о���, �����ʹ� ��ҹ��� ������.
select * from mem3 where name='aaa';
select * from mem3 where name='AAA';

-- select, from 2���� Ű����� ������
-- * ��� �÷��� ���
-- ��ҹ��ڸ� �������� ����(�����ʹ� ������)

select * from mem;
SELECT * FROM MEM;

select emp_name,department_id from employees;

-- distinct : ���� ���� 1���� ���(�ߺ��Ȱ� ����)
select distinct department_id from employees;

select * from departments;
select department_name, department_id from departments;

select * from departments;
select * from employees;
select * from jobs;
select * from products;

select employee_id,emp_name,salary from employees;
select employee_id, job_id,a.* from employees a; -- ���� ������� ��µ�, ��Ī���� ���� a ��������

select * from mem3;
select no,mdate2,tel,name,mdate from mem3;

select * from employees;

-- �����ȣ(emp_id), ����̸�(e name), �޿�(salary), �Ի�����(hire_date)
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
 1,'ȫ�浿',100,100,100,300,100,1
);
insert into stu_score values (
 2,'�̼���',100,100,100,300,100,1
);
insert into stu_score values (
 5,'�豸',100,100,100,300,100,1
);

commit;

select * from stu_score;

-- ��������� number Ÿ���� ��츸 ����

select * from stu_score;

insert into stu_score values (
6,'������', 100,95,96,(100+95+96),(100+95+96)/3,1
);

select * from stu_score;

insert into stu_score values (
7,'ȫ����',100,100,99,(100+100+99),(100+100+99)/3,1
);

-- ��ȣ, �̸�, ��������, ��������-20, ���, ��������-20�� �� ���
select no,name,kor,kor-20,avg,(kor-20+eng+math)/3 from stu_score;

select * from employees;

-- �޷� -> ��ȭȯ�� 1�޷� = 1381.79��
select employee_id,emp_name,salary from employees;

select employee_id,emp_name,salary,salary*1381.79 from employees;

-- ���� * 12  = ���
select employee_id, emp_name, salary, salary*12, salary*12*1381.79 from employees;

-- �������� = ���� + ����*Ŀ�̼�
-- commission_pct
select * from employees;

select employee_id,emp_name,commission_pct, salary+(salary*commission_pct)from employees;

-- nvl(�÷�,0)
select employee_id, emp_name,nvl(commission_pct,0),salary+(salary*nvl(commission_pct,0)) from employees;





