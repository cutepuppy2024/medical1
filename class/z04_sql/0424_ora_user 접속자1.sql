-- trunc ����, round �ݿø�
select sysdate,hire_date,3,round(sysdate-hire_date,3) from employees;

-- ���� sysdate-1, ���� sysdate+1
select sysdate-1 ����, sysdate ����, sysdate+1 ����, sysdate+100 from dual;

-- ���� : ������ m_no�� �������� 1-9999, 1�� ����
-- m_yesterday, m_today, m_tomorrow, m_year ��¥�÷��� ���� ���̺� m_date
-- ����, ����, ����, 1�� �� ��¥�� �����Ͻÿ�

create sequence seq_m_no
start with 1
increment by 1
minvalue 1
maxvalue 9999
nocycle
nocache
;

-- ���̺���� date, timestamp
create table m_date(
m_no number(4),
m_yesterday date,m_today date,m_tomorrow date,m_year date
);

--drop table m_date;

-- 1�� row ����
insert into m_date(m_no,m_yesterday, m_today, m_tomorrow, m_year) values(
seq_m_no.nextval, sysdate-1, sysdate, sysdate+1, sysdate+365
);

-- �˻�
select * from m_date;

-- ȸ������ 1�⵿�� �α����� ������, �������� ȸ������ ����

-- abs ���밪, ceil, round,floor trunc
select abs (hire_date-sysdate) from employees;

-- month ���� �ݿø�
select hire_date,round(hire_date,'month') from employees;

-- ��¥�� ���� �������� ����
select hire_date,trunc(hire_date,'month'), round(hire_date,'month') from employees;

select trunc(hire_date,'month') ������,hire_date from employees
order by hire_date;

select * from channels;

select period,count(period) from kor_loan_status
group by period
order by period;

select period from kor_loan_status
where period = '201111';

select trunc(kor,-1) t_kor, count(trunc(kor,-1)) from students
group by trunc(kor,-1)
order by t_kor;

-- ��¥�� ���� �������� ����
select trunc(hire_date,'month') m_hire_date, count(trunc(hire_date,'month')) from employees
group by trunc(hire_date,'month')
order by m_hire_date;

--drop table stu_score;

select * from stu_score
order by no;

update stu_score set name='������'
where no=10;

select * from stu_score;

update stu_score set avg=(total/3);

-- 2���� ��¥���� �� ������ Ȯ��
select hire_date,floor(months_between(sysdate,hire_date)), trunc(sysdate-hire_date,2) from employees;

-- ���� �߰�
select hire_date, add_months(hire_date,6) from employees;

-- last day
select hire_date, last_day(hire_date), round(hire_date,'ddd') from employees;

-- round d : ���ϱ��� �ݿø� ������ 12��
select sysdate, trunc(sysdate,'d') from employees;

select sysdate, trunc(sysdate,'month') from employees;

-- ��¥�� �������� ������, ó����, ��������
select sysdate ������, trunc(sysdate,'month') ù��,last_day(sysdate) �������� from dual;

-- Ư�� ������ ��¥�� Ȯ��
select sysdate, next_day(sysdate,'�����') from dual;

-- ������ ó����
select sysdate, trunc(sysdate,'d'), next_day(sysdate,'�����') from dual;

-- board ���̺� default �� �Է½� ������ ������ ������ �ڵ��Է� ��
create table board(
bno number(4) primary key, -- �ߺ��� �ȵ�, null ������� ����. �⺻Ű�� ����
id varchar2(30),
btitle varchar2(1000),
bcontent clob, -- varchar2(3000) clob -������, varchar2Ÿ��
bdate date default sysdate,
bhit number default 0,
bgroup number,
bstep number default 0,
bindent number default 0,
bfile varchar2(100)
);

insert into board values (
board_seq.nextval,'aaa','�����Դϴ�','�����Դϴ�', sysdate, 0, board_seq.currval,0,0,'1.jpg'
);

-- default -> �����Ͱ� ���� �ʾƵ� �ڵ��Է�
insert into board(bno,id,btitle,bcontent,bgroup,bfile) values (
board_seq.nextval,'bbb','�̺�Ʈ ��û','�̺�Ʈ�� ��û�մϴ�', board_seq.currval,'2.jpg'
);

select * from board;

-- ����ȯ : number, character, date
select sysdate from dual;
select sysdate, to_char(sysdate,'yyyy-mm--dd hh:mi:ss') from dual;
select to_char(sysdate,'yy/mm/dd') from dual;
select to_char(susdate,'yyyy') from dual;

create sequence seq_mno
increment by 1
start with 1
minvalue 1
maxvalue 9999
nocycle
nocache
;

-- ko20240001 
select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(seq_mno.nextval,'0000')) from dual;

select to_char(sysdate,'dy'), to_char(sysdate,'day') from dual;

select to_char(sysdate,'yyyy-mm-dd hh:mi:ss mon day') from dual;

-- hire_date, yyyy-mm-dd hh:mi:ss mon day

select department_id, emp_name, to_char(hire_date,'yyyy-mm-dd hh:mi:ss mon day') from employees;

-- pm/am : ������� ����/���� ǥ��, hh24 : 24�ð�����
select to_char(sysdate,'pm hh24:mi:ss') from dual;

select * from stu_score;

select to_char(c_date,'yyyy-mm-dd hh:mi:ss day') from stu_score
order by c_date;

-- ��¥���� ��� �����Ͱ� �� �ִ��� ����Ͻÿ�.
select c_date,count(c_date) from stu_score
group by c_date
order by c_date;

-- ������ ��Ģ����(+,-,*,/) �ȵ�. �ڸ���ǥ��, ��ǥǥ��, ��¥���� ��� ǥ��
-- ������ ��Ģ���� ���� �÷��� ��Ģ���� ����, �ڸ���ǥ��(0001-> �ȵ�), ��ǥǥ�� �ȵ�. 0001
-- ��¥�� +,- �����ɰ���, months-between 2���� ��¥ �� ���, ��¥������ �����ؼ� ����� �ȵ�. 

-- ������ �ȿ� �ִ� �����Ͱ� �����̸� �ڵ����� ����ȯ�ؼ� �������.
select 10 a,100 b, (10+100) ab, to_char(100) ,10+'100' from dual;
-- ������ �ȿ� ���ڰ� ������ �ڵ�����ȯ �Ұ�
select 10 a,100 b, (10+100) ab, to_char(100) ,10+'100��' from dual;

-- '0000' ���ڸ��� 0���� ä��, '9999' ���ڸ��� ���ڸ��� ��.
select 12340000, to_char(12340000), length(to_char(12340000,'999,999,999')) from dual;
select length(12340000), to_char(12340000), to_char(12340000,'000,999,999'),
length(to_char(12340000,'999,999,999')) from dual;

-- L�� ��ȭ ǥ��
select 12340000, to_char(12340000,'L999,999,999') from dual;
-- $�� $ǥ��
select 12340000, to_char(12340000,'$999,999,999') from dual;
-- �Ҽ��� �ڸ� ǥ��
select 1234.1234, to_char(1234.1234,'000,999.99') from dual;
-- 10�� �ڸ��� ǥ��
-- ���������ؼ� �ڸ��� Ȯ�� : trim
select length(trim(to_char(12345,'0000000000'))), length(trim(to_char(12345,'999,999'))) from dual;

-- �������� ���� �Լ�
select length('�ȳ��ϼ���') from dual;
select length(1234000) from dual;

-- ����
-- 123,456,789 100,000
-- 123,456,789 100,000 = ��������Ͻÿ�. õ���� ǥ���Ұ�
-- 123,556,789

select 123456789+100000 from dual;
-- 123,456,789 �� ��ǥ�� ���� - replace('123,456,789',',','')
-- Ÿ���� number������ ����
-- ���ϱ⸦ ��
-- ������ Ÿ������ ��ȭ, ��ǥ ǥ��
-- total = '123,456,789'

select (123,456,789)+(100,000) from dual; -- ���� �̷� �������� �����Ͱ� �־���
select replace('123,456,789',',',''), replace('100,000',',','') from dual;
select to_char(to_number(replace('123,456,789',',','')) + to_number(replace('100,000',',','')),'L999,999,999') from dual;

select to_char(123456789+100000, 'L999,999,999') from dual;

select to_number('00001234') from dual;

-- ��¥��
-- ������ +,- d�ȵ�.
select '2024-04-24 11:00:00'-'2024-04-01 01:00:00' from dual;
select to_date('2024-04-24')-to_date('2024-04-01') from dual;
select to_date('2024/04/24')-to_date('2024/04/01') from dual;
select to_date('24/04/24')-to_date('24/04/01') from dual;

-- 2404-04-01 
select to_date('20240424') from dual;
select to_char(to_date('20240424'),'yyyy-mm-dd hh:mi:ss')from dual;

select to_date('2024-04-24 11:00:00') from dual;

select hire_date from employees
where hire_date >=  '20080101'
;

select * from stu_score;

-- �������¶� ��¥���¸� �˻���, +,-���´� ����ȯ�� �־�� ��
select c_date from stu_score
where c_date = '2024/04/05'
;
select sysdate-hire_date from employees;
select trunc(sysdate-to_date('2024/04/01')) from dual;

-- ����
-- 20,000 - 10,000 ������ 10,000 ����Ͻÿ�.
select to_char(to_number('20,000','999,999')-to_number('10,000','999,999'),'99,999') from dual;

-- ����
select commission_pct from employees;
-- �������� = ���� + (����*Ŀ�̼�) �������� �ؼ� ���
-- nvl(������,0)
select salary, salary+(salary*nvl(commission_pct,0)), commission_pct from employees;
select nvl(commission_pct,0) from employees;

-- commission_pct null���� ����Ͻÿ�
--is null
select emp_name, commission_pct from employees
where commission_pct is null;

-- ���� : manager_id null�̸� 0 
select nvl(manager_id,0) from employees
order by manager_id desc;

-- ���� : manager_id null �̸� ceo�� �Է��Ͻÿ�
-- manager_id,�� Ÿ���� ���� -> Ÿ�Ժ������־�� ������ ������ ����
select nvl(to_char(manager_id),'ceo') from employees
order by manager_id desc;








